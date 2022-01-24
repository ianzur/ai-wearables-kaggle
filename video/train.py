import functools
import os
import logging
from pathlib import Path

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 

import numpy as np
import pandas as pd

import tensorflow_datasets as tfds 
import tensorflow as tf

logger = tf.get_logger()
logger.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# create file handler which logs even debug messages
fh = logging.FileHandler('tensorflow.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)
tf.config.optimizer.set_experimental_options({'layout_optimizer': False})

import ai_wearables_video_gestures.ai_wearables_video_gestures
    
import data_utils
import decoders
import models


def main():
    ds = tfds.load(
        "ai_wearables_video_gestures",
        data_dir="./data",
        decoders={"video": tfds.decode.SkipDecoding()},  # skip decoding for now
        # decoders=tfds.decode.PartialDecoding({'video': False, 'label': True, 'frames': True, 'id': True}),
        with_info=False,
        as_supervised=False,  # set True to only return (video, label) tuple
    )
    
    train = ds["train"]
    val = ds["validation"]
    test = ds["test"]
    
    # df_train = tfds.as_dataframe(train)
    # df_val = tfds.as_dataframe(val)
    # df_test = tfds.as_dataframe(test)
    
    # print(df_train.sort_values("frames").head(10))
    # print(df_val.sort_values("frames").head(10))
    # print(df_test.sort_values("frames").head(10))
    
    batch = 16
    segments = 8
    with tf.device("CPU"):
        train = train.map(functools.partial(decoders.decode_video_segment, num_segments=segments)).batch(batch).prefetch(batch)
        train = train.map(lambda ex : (ex["video"], tf.one_hot(ex["label"], depth=6)))
        
        val = val.map(functools.partial(decoders.decode_video_segment, num_segments=segments)).batch(batch).prefetch(batch)
        val = val.map(lambda ex : (ex["video"], tf.one_hot(ex["label"], depth=6)))
        
        test = test.map(functools.partial(decoders.decode_video_segment, num_segments=segments)).batch(batch).prefetch(batch)
        
    input_shape = (batch, segments, 240, 320, 3)

    model = models.ConvLSTM2D_a(input_shape)
    model.build_graph(input_shape)
    model.compile(optimizer="Adam", loss="categorical_crossentropy", metrics=["accuracy"])
    
    print(model.build_graph(input_shape).summary(line_length=160))
    
    hist = model.fit(
        train,
        validation_data=val,
        epochs=200,  # max number ( early stopping expected )
        verbose=1,
        callbacks=[
            ## Early Stop ##
            # tf.keras.callbacks.EarlyStopping(
            #     monitor="val_loss",
            #     min_delta=0.001,
            #     patience=20,
            #     verbose=0,
            #     mode="auto",
            #     baseline=None,
            #     restore_best_weights=True,
            # ),
            ## Save checkpoints ##
            tf.keras.callbacks.ModelCheckpoint(
                Path.cwd() / "ckpt",  # file path/name to save the model
                monitor="val_loss",
                verbose=0,
                save_best_only=True,
                save_weights_only=True,
                mode="auto",
                save_freq="epoch",  # If save_freq is an integer, it will save after n batches (not epochs)
            ),
            tf.keras.callbacks.TensorBoard()
        ],
    )
    
    with open('submission_video.csv', "w") as f:
        f.write("id,gesture\n")

        for batch in test.as_numpy_iterator():
            results = model.predict(batch["video"])
            
            for example, result in zip(batch["id"], results):               
                f.write(f"{str(example.decode('utf-8'))},{np.argmax(result)}\n")

    print('predictions complete')
    
    print('test set results')
    with tf.device("CPU"):
        test = test.map(lambda ex : (ex["video"], tf.one_hot(ex["label"], depth=6)))
    
    test_metrics = model.evaluate(test)
    print(f"loss={test_metrics[0]}\taccuracy={test_metrics[1]}")
    
    del model            

if __name__ == "__main__":
    
    main()
    
    

