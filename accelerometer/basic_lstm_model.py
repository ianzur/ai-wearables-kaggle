# basic_lstm_model.py

# Data Handling
import pandas as pd
import numpy as np
import os
from ast import literal_eval

# Tensorflow
import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping

# Data Visualization
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns



# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory
import os
for dirname, _, filenames in os.walk('../data/accel/'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

        
# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

# # Define Simulation Parameters

# Length to standardize data to.
# Average is 19.708 samples, 
# max is 51, min is 10
data_truncate_pad_length = 26

# Number of epochs per train iteration.
epochs = 15

# Number of iterations to simulate over.
num_iterations = 5

# Number of gestures in the dataset.
num_gestures = 20

# Number of total users in the training file.
num_train_users = 7

# Create an array of the zero-based gesture IDs.
classes = np.arange( num_gestures )

# ---
# # Define Model Parameters


# Layer parameters.
dropout_rate = 0.0
lstm_units = 16


# Optimizer parameters.
lr = 0.001
model_optimizer = Adam( learning_rate=lr, decay=1e-6 )


# Callback parameters.
monitor = 'loss'
min_delta = 0.001
patience = 20
earlystop_callback = EarlyStopping( monitor=monitor, min_delta=min_delta,
                                    verbose=1, patience=patience,
                                    restore_best_weights=True )
# lstm_callbacks = [earlystop_callback]
lstm_callbacks = None


# Create tuples for model creation later.
model_params = ( dropout_rate, lstm_units, data_truncate_pad_length, model_optimizer )
fit_params = ( epochs, lstm_callbacks )
# ---
# # Define Some Functions to Load and Standardize the Data

def get_gesture_data( path, data_column_headers=None ):
    """
    Load the gesture data from a csv located at 'path'.

    :param path: Location of the gesture data csv file.

    :param data_column_headers: List of data column header names that
    need literal_eval to parse (i.e., the headers for data arrays). If None,
    default to [ 'x', 'y', 'z' ]

    :return: The pandas dataframe holding the gesture data.
    """

    if data_column_headers is None:
        data_column_headers = [ 'x', 'y', 'z' ]

    # Create converter dictionary to literal_eval selected columns.
    converters = {
        header: literal_eval for header in data_column_headers
    }

    return pd.read_csv( path, converters=converters )

def truncate_data( data, length ):
    """
    Truncates x, y, and z data to specified length. If data is less than length,
    it is zero-padded at the end.

    :param data: Pandas dataframe with at least x, y, z columns. Modified
    in place.

    :param length: Length of data to truncate (or pad) to.

    :return: Pandas dataframe with truncated data.
    """
    for idx, row in data.iterrows():
        # If data length is greater than length, truncate.
        # If data length is less than length, zero-pad at end.
        if len( row[ 'x' ] ) > length:
            data.at[ idx, 'x' ] = row[ 'x' ][ :length ]
            data.at[ idx, 'y' ] = row[ 'y' ][ :length ]
            data.at[ idx, 'z' ] = row[ 'z' ][ :length ]
        elif len( row[ 'x' ] ) < length:
            pad_length = length - len( row[ 'x' ] )

            data.at[ idx, 'x' ] = row[ 'x' ][ : ] + ( [ 0 ] * pad_length )
            data.at[ idx, 'y' ] = row[ 'y' ][ : ] + ( [ 0 ] * pad_length )
            data.at[ idx, 'z' ] = row[ 'z' ][ : ] + ( [ 0 ] * pad_length )

    return data

# ---
# # Load and Standardize the Data

# Load in the pre-processed data.
test = get_gesture_data( '/home/ian/Documents/UNT/wearables/kaggle/data/accel/test.csv' )
train = get_gesture_data( '/home/ian/Documents/UNT/wearables/kaggle/data/accel/train.csv' )

# Truncate the data to desired length.
# If data is longer than data_length, truncate
# otherwise zero-pad to end.
train = truncate_data( train, length=data_truncate_pad_length )
test = truncate_data( test, length=data_truncate_pad_length )

# Test data doesn't have labels, so let's go ahead
# and pull out the data now.
X_test = np.array( [ np.array( test[ col ].tolist() ).T for col in [ 'x', 'y', 'z' ] ] ).T

# ---
# # Create Data Structures to Capture Training Information


# These arrays will hold the ground truth
# and predicted labels for the testing
# data split from the provided training data
# so that we can create a confustion matrix
# after training for num_iterations.
cf_matrix_true = np.array( [] )
cf_matrix_pred = np.array( [] )

# Holds the test scores (loss, accuracy)
scores = []

# Holds tuples for train, validation, and
# test user sets that we randomly select at
# each iteration.
user_selections = []

# ---
# # Define a Function to Create the Model

def create_lstm_model( num_classes=20,
                       dropout=0.8, units=128,
                       data_length=19,
                       optimizer=Adam( learning_rate=0.001 )
                     ):
    """
    Create a simple bidirectional LSTM model for classification. Creates a
    bidirectional LSTM layer, dropout, and two dense layers.

    :param num_classes: Number of classes.

    :param dropout: Dropout rate

    :param units: Number of units in LSTM layer.

    :param data_length: Length of time data for LSTM layer input.

    :param optimizer: Optimizer to use for model compilation.

    :return: The compiled model with LSTM, dropout, and two dense layers.
    """

    # Create the model object.
    model = tf.keras.models.Sequential()

    # Add an LSTM layer.
    # Input size is (data_length,3):
    #   data_length time samples from data.
    #   3 dimensions (x, y, z accelerometer data).
    model.add(
        tf.keras.layers.Bidirectional(
            tf.keras.layers.LSTM( units=units, input_shape=[data_length, 3] )
        )
    )

    # Add dropout layer to reduce overfitting.
    model.add( tf.keras.layers.Dropout( rate=dropout ) )

    # Add final dense layers.
    model.add( tf.keras.layers.Dense( units=16, activation='relu' ) )
    model.add( tf.keras.layers.Dense( units=num_classes,
                                      activation='softmax' ) )

    model.compile( loss='sparse_categorical_crossentropy', optimizer=optimizer,
                   metrics=['accuracy'] )

    return model

# ---
# # Define a Function for Training the Model

def train_model( idx, data, model, fit_params,
                 classes=None, num_subjects=7, verbose=1 ):
    """
    Wrapper for training and testing model. Returns the testing loss and
    accuracy and the test and predicted labels for the current iteration.

    :param idx: Current iteration index.

    :param data: Pandas dataframe of gesture data.

    :param model: tf.keras model object to train on.

    :param fit_params: Tupled collection of fit/train parameters.
    Contains: epochs, lstm_callbacks.

    :param classes: List of gesture classes to be used for training. These
    classes are used for mapping labels to range [0,num_classes).

    :param num_subjects: Number of users in the dataset.

    :param verbose: Verbosity of output.
    0 -- no output. 1 -- Only current iteration output. 2 -- Full.

    :return: Returns tuple of test loss/accuracy, test labels, and predicted
    labels.

    """

    # Unpack model fit parameters.
    epochs, callbacks = fit_params

    # Select the training, test, and validation subjects.
    # Get random ordering of subjects.
    subject_list = np.random.permutation( num_subjects )

    # Select the second from last as validation and last user as test.
    train_subjects = subject_list[ :-2 ].tolist()
    test_subjects = subject_list[ -2:-1 ].tolist()
    val_subjects = [ subject_list[ -1 ] ]


    if verbose > 0:
        print( f"============================================================\n"
               f"Iteration {idx+1}:\n"
               f"    Train Subjects:      {train_subjects}\n"
               f"    Validation Subjects: {val_subjects}\n"
               f"    Test Subjects:       {test_subjects}\n" )


    # Split the data into training, testing, and validation data and labels.
    X_train, y_train,     X_test, y_test,    X_val, y_val = train_test_split( data,
                                     train_subjects=train_subjects,
                                     test_subjects=test_subjects,
                                     val_subjects=val_subjects )

    # If selecting validation data, create tuple of data and labels.
    validation_data = (X_val, y_val) if X_val is not None else None


    # Train the model on the training data.
    fit_verbose = 0 if verbose <= 1 else 2 if verbose == 2 else 1
    model.fit( X_train, y_train, epochs=epochs, callbacks=callbacks,
               verbose=verbose, validation_data=validation_data )


    # Test the model to see how well we did.
    score = model.evaluate( X_test, y_test )


    # Return the test scores, test labels, test predictions, and a tuple
    # containing the subjects selected for the train, validation, and testing
    # sets.
    return score, y_test,            np.argmax( model.predict( X_test ), axis=1 ),            ( train_subjects, val_subjects, test_subjects )

# ---
# # Define a Function for Train/Val/Test Splits

def train_test_split( data, train_subjects=None,
                      test_subjects=None,
                      val_subjects=None ):
    """
    Split the given dataframe into test and train data and labels. Data is
    of shape (length, 3) where length is the number of samples in a gesture
    reading (can be arbitrary).

    :param data: Dataframe with at least x, y, z accelerometer data and gesture
    index number.

    :param test_subjects: List of user indexes over [0, 7] to select for test
    data. If None, use test_gestures to split.

    :return: Training data, training labels, testing data, testing labels,
    validation data, validation labels.
    """

    if train_subjects is None or test_subjects is None:
        raise ValueError( "Must provide train and test subjects list." )


    # Define the column we're selecting by.
    # Not useful now, maybe in future updates for more dynamic splitting.
    sel_column = 'user'

    val_subjects = [] if val_subjects is None else val_subjects


    # Split into train and test rows by selecting rows where slected column data
    # is in the provided splitting list (user or gesture).
    test = data[ data[ sel_column ].isin( test_subjects ) ]
    train = data[ data[ sel_column ].isin( train_subjects ) ]


    # Transpose the data so that the shape is
    # (num_samples, sample_length, num_features).
    # For user 6, 7 test, training data is (2450, 19, 3) assuming we
    # truncate length to 19. Test would be (851, 19, 3).
    X_train = np.array( [ np.array( train[ col ].tolist() ).T for col in [ 'x', 'y', 'z' ] ] ).T
    y_train = np.array( train[ 'gesture' ].tolist() )

    X_test = np.array( [ np.array( test[ col ].tolist() ).T for col in [ 'x', 'y', 'z' ] ] ).T
    y_test = np.array( test[ 'gesture' ].tolist() )

    # Shuffle the data.
    train_perm = np.random.permutation( X_train.shape[ 0 ] )
    X_train = X_train[ train_perm ]
    y_train = y_train[ train_perm ]

    test_perm = np.random.permutation( X_test.shape[ 0 ] )
    X_test = X_test[ test_perm ]
    y_test = y_test[ test_perm ]

    if val_subjects is not None:
        val = data[ data[ sel_column ].isin( val_subjects ) ]
        X_val = np.array( [ np.array( val[ col ].tolist() ).T for col in [ 'x', 'y', 'z' ] ] ).T
        y_val = np.array( val[ 'gesture' ].tolist() )

        val_perm = np.random.permutation( X_val.shape[ 0 ] )
        X_val = X_val[ val_perm ]
        y_val = y_val[ val_perm ]
    else:
        X_val = None
        y_val = None

    return X_train, y_train, X_test, y_test, X_val, y_val

# ---
# # Train the Model for the Selected Number of Iterations

for i in range( num_iterations ):
    model = create_lstm_model( num_classes=num_gestures,
                               dropout=dropout_rate,
                               units=lstm_units,
                               data_length=data_truncate_pad_length,
                               optimizer=model_optimizer )

    score, y_test, y_pred,    train_val_test_split = train_model( i, train, model,
                                        fit_params, classes=classes,
                                        num_subjects=num_train_users,
                                        verbose=1 )

    # Save the train, validation, and test users and the test scores
    # for this iteration.
    user_selections.append( train_val_test_split )
    scores.append( score )

    # Predict on the test dataset and save the
    # submission file for this iteration.
    submission = test.assign( gesture=np.argmax( model.predict( X_test ), axis=1 ) )
    submission.to_csv( f"./submission{i}.csv", index=False,
                       columns=[ 'id', 'gesture' ] )

    # Generate data for confusion matrix.
    cf_matrix_true = np.hstack( ( cf_matrix_true, y_test ) )
    cf_matrix_pred = np.hstack( ( cf_matrix_pred, y_pred ) )

    # Logging output for current iteration.
    print( "test loss, test acc: ", score )

# ---
# # Define Helper Functions for Result Output and Confusion Matrix

def print_results_table( scores, data_sels, cf_matrix ):
    """
    Print the results for a number of simulation iterations in a tabular format.

    :param scores: List of tuples from model.evaluate containing test loss and
    test accuracy.

    :param data_sels: List of data set splits at each iteration containing
    training, validation, and test set selections. Each row should be a tuple or
    list of the format (train set, validation set, test set)

    :param cf_matrix: Confusion matrix object from
    sklearn.metrics.confusion_matrix. Used to calculate overall accuracy over
    multiple iterations from the simulation.

    :return: None.
    """

    # Calculate maximum lengths for each of the three data selection sets so 
    # that we can properly set the widths of the train, validation, and test set
    # columns. Creates a three-tuple by finding the max length of the string
    # representation of the lists for train, validation, and test sets at each
    # iteration of the simulation (row of the scores list). If the max length
    # value for a specific column is less than the length of the column header,
    # use the length of the column header instead.
    # First index is train, second is validation, third is test.
    col_headers = [ 'Train Set', 'Validation Set', 'Test Set' ]
    max_lengths = tuple( 
            max( list( map( lambda x: len( str( x[ i ] ) ), data_sels ) ) )
        for i in range( 3 ) )
    max_lengths = [ length if len( col_headers[ i ] ) < length
                    else len( col_headers[ i ] ) 
                    for i, length in enumerate( max_lengths ) ]

    # Pre calculate the strings for the horizontal dividers for the train,
    # validation, and test sets so we're not calculating them at each iteration.
    set_bars = [ '─' * length for length in max_lengths ]


    # Set up widths for the index, accuracy, and loss sections.
    # Does not include single spaces on left and right between vertical pipes.
    index_width = 5
    index_bars = '─' * index_width

    accuracy_width = 8
    accuracy_bars = '─' * accuracy_width

    loss_width = 6
    loss_bars = '─' * loss_width


    # Calculate table width (minus two spaces on either end for spacing)
    table_width = (
        index_width + 3 + accuracy_width + 3 + loss_width + 3 + 
        max_lengths[ 0 ] + 3 + max_lengths[ 1 ] + 3 + max_lengths[ 2 ]
        )

    # Define outer box to go around the table. Makes it nice and clear.
    # Value is equal to top/bottom spacing. Horizontal spacing is double
    # (monospace is more or less 2:1, width:height).
    spacing = 2
    side_spacing = ' ' * 2 * spacing


    # Calculate overall table width including inner table, two inner padding
    # spaces, inner table borders (2), and padding on both sides.
    total_table_width = table_width + 2 + 2 + ( 2 * 2 * spacing )


    # Print top-side outer box.
    for _ in range( spacing ):
        print()
    print( f"{side_spacing}╔{'═' * total_table_width}╗" )
    for _ in range( spacing ):
        print( f"{side_spacing}║{' ' * total_table_width}║" )


    # Define the inner divider lines that go above each output row.
    inner_divider = f"\n{side_spacing}║{side_spacing}╟─{index_bars}─┼─{accuracy_bars}─" +                     f"┼─{loss_bars}─┼─{set_bars[ 0 ]}─┼─{set_bars[ 1 ]}─" +                     f"┼─{set_bars[ 2 ]}─╢{side_spacing}║\n"


    # Print the divider and header information
    print( f"{side_spacing}║{side_spacing}╔═{index_bars.replace( '─', '═' )}═"
           f"╤═{accuracy_bars.replace( '─', '═' )}═"
           f"╤═{loss_bars.replace( '─', '═' )}═"
           f"╤═{set_bars[ 0 ].replace( '─', '═' )}═"
           f"╤═{set_bars[ 1 ].replace( '─', '═' )}═"
           f"╤═{set_bars[ 2 ].replace( '─', '═' )}═╗{side_spacing}║\n"
           f"{side_spacing}║{side_spacing}║ {'Index':>{index_width}} "
           f"│ {'Accuracy':>{accuracy_width}} "
           f"│ {'Loss':>{loss_width}} "
           f"│ {col_headers[ 0 ]:^{max_lengths[ 0 ]}} "
           f"│ {col_headers[ 1 ]:^{max_lengths[ 1 ]}} "
           f"│ {col_headers[ 2 ]:^{max_lengths[ 2 ]}} ║{side_spacing}║", end='' )

    # Iterate through each simulation result and print the data in the row.
    for idx, score in enumerate( scores ):
        # train_str = 

        print( f"{inner_divider}"
               f"{side_spacing}║{side_spacing}║ {idx + 1:>{index_width}d} "
               f"│ {score[ 1 ]:>{accuracy_width}.3f} "
               f"│ {score[ 0 ]:>{loss_width}.3f} "
               f"│ {str(data_sels[ idx ][ 0 ]):^{max_lengths[ 0 ]}} "
               f"│ {str(data_sels[ idx ][ 1 ]):^{max_lengths[ 1 ]}} "
               f"│ {str(data_sels[ idx ][ 2 ]):^{max_lengths[ 2 ]}} ║"
               f"{side_spacing}║", 
               end='' )


    # Prin the border for the bottom of the regular data.
    print( f"\n{side_spacing}║{side_spacing}╠═{index_bars.replace( '─', '═' )}═"
           f"╧═{accuracy_bars.replace( '─', '═' )}═"
           f"╧═{loss_bars.replace( '─', '═' )}═"
           f"╧═{set_bars[ 0 ].replace( '─', '═' )}═"
           f"╧═{set_bars[ 1 ].replace( '─', '═' )}═"
           f"╧═{set_bars[ 2 ].replace( '─', '═' )}═╣{side_spacing}║" )


    # Calculate the overall accuracy and total width of the table and print
    # in its own row at the bottom of the table.
    overall_accuracy = 100 * np.trace( cf_matrix ) / float( np.sum( cf_matrix ) )
    print( f"{side_spacing}║{side_spacing}║ {' ' * table_width} ║{side_spacing}║\n"
           f"{side_spacing}║{side_spacing}║ {f'Total Accuracy: {overall_accuracy:{accuracy_width-1}.2f}%':^{table_width}} "
           f"║{side_spacing}║\n"
           f"{side_spacing}║{side_spacing}║ {' ' * table_width} ║{side_spacing}║" )


    # Print the bottom table outline.
    print( f"{side_spacing}║{side_spacing}╚═{'═' * table_width}═╝{side_spacing}║" )


    # Print bottom-side outer box.
    for _ in range( spacing ):
        print( f"{side_spacing}║{' ' * total_table_width}║" )
    print( f"{side_spacing}╚{'═' * total_table_width}╝" )
    for _ in range( spacing ):
        print()
        
        
        
def make_confusion_matrix(cf,
                          group_names=None,
                          categories='auto',
                          count=True,
                          percent=True,
                          cbar=True,
                          xyticks=True,
                          xyplotlabels=True,
                          sum_stats=True,
                          figsize=None,
                          cmap='Blues',
                          title=None):
    '''
    This function will make a pretty plot of an sklearn Confusion Matrix cm using a Seaborn heatmap visualization.

    Provided by: https://raw.githubusercontent.com/DTrimarchi10/confusion_matrix/master/cf_matrix.py

    Arguments
    ---------
    cf:            confusion matrix to be passed in

    group_names:   List of strings that represent the labels row by row to be shown in each square.

    categories:    List of strings containing the categories to be displayed on the x,y axis. Default is 'auto'

    count:         If True, show the raw number in the confusion matrix. Default is True.

    normalize:     If True, show the proportions for each category. Default is True.

    cbar:          If True, show the color bar. The cbar values are based off the values in the confusion matrix.
                   Default is True.

    xyticks:       If True, show x and y ticks. Default is True.

    xyplotlabels:  If True, show 'True Label' and 'Predicted Label' on the figure. Default is True.

    sum_stats:     If True, display summary statistics below the figure. Default is True.

    figsize:       Tuple representing the figure size. Default will be the matplotlib rcParams value.

    cmap:          Colormap of the values displayed from matplotlib.pyplot.cm. Default is 'Blues'
                   See http://matplotlib.org/examples/color/colormaps_reference.html

    title:         Title for the heatmap. Default is None.

    '''

    # CODE TO GENERATE TEXT INSIDE EACH SQUARE
    blanks = ['' for i in range(cf.size)]

    if group_names and len(group_names) == cf.size:
        group_labels = ["{}\n".format(value) for value in group_names]
    else:
        group_labels = blanks

    if count:
        group_counts = ["{0:0.0f}\n".format(value) for value in cf.flatten()]
    else:
        group_counts = blanks

    if percent:
        group_percentages = ["{0:.2%}".format(value) for value in cf.flatten() / np.sum(cf)]
    else:
        group_percentages = blanks

    box_labels = [f"{v1}{v2}{v3}".strip() for v1, v2, v3 in zip(group_labels, group_counts, group_percentages)]
    box_labels = np.asarray(box_labels).reshape(cf.shape[0], cf.shape[1])

    # CODE TO GENERATE SUMMARY STATISTICS & TEXT FOR SUMMARY STATS
    if sum_stats:
        # Accuracy is sum of diagonal divided by total observations
        accuracy = np.trace(cf) / float(np.sum(cf))

        # if it is a binary confusion matrix, show some more stats
        if len(cf) == 2:
            # Metrics for Binary Confusion Matrices
            precision = cf[1, 1] / sum(cf[:, 1])
            recall = cf[1, 1] / sum(cf[1, :])
            f1_score = 2 * precision * recall / (precision + recall)
            stats_text = "\n\nAccuracy={:0.3f}\nPrecision={:0.3f}\nRecall={:0.3f}\nF1 Score={:0.3f}".format(
                accuracy, precision, recall, f1_score)
        else:
            stats_text = "\n\nAccuracy={:0.3f}".format(accuracy)
    else:
        stats_text = ""

    # SET FIGURE PARAMETERS ACCORDING TO OTHER ARGUMENTS
    if figsize == None:
        # Get default figure size if not set
        figsize = plt.rcParams.get('figure.figsize')

    if xyticks == False:
        # Do not show categories if xyticks is False
        categories = False

    # MAKE THE HEATMAP VISUALIZATION
    plt.figure(figsize=figsize)
    sns.heatmap(cf, annot=box_labels, fmt="", cmap=cmap, cbar=cbar, xticklabels=categories, yticklabels=categories)

    if xyplotlabels:
        plt.ylabel('True label')
        plt.xlabel('Predicted label' + stats_text)
    else:
        plt.xlabel(stats_text)

    if title:
        plt.title(title)

    plt.show()

# ---
# # Print out the Results from the Simulations and Show Confusion Matrix

# Generate the confusion matrix.
cf_matrix = confusion_matrix( cf_matrix_true, cf_matrix_pred )


# Print the results for each simulation run in a tabular format.
print_results_table( scores, user_selections, cf_matrix )


# Plot the confusion matrix.
make_confusion_matrix( cf_matrix, categories=classes,
                       figsize=[8,8])


