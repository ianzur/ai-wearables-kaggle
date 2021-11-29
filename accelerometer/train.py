
import functools
import os
import logging
from pathlib import Path

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 

import numpy as np
import pandas as pd

import tensorflow_datasets as tfds 
import tensorflow as tf

import ai_wearables_accelerometer_gestures.ai_wearables_accelerometer_gestures

import data_utils
import models


def main():
                  
    ds, ds_info = tfds.load(
        "ai_wearables_accelerometer_gestures",
        data_dir="./data",
        with_info=True,
        as_supervised=False,  # set True to only return (xyz, gesture) tuple
    )
    
    train_ds = ds["train"]
    test_ds = ds["test"]
    
    batch_size = 32
    
    train = train_ds.filter(lambda x: tf.math.reduce_any(x["user"] == [0,1,2,3,4]))
    val = train_ds.filter((lambda x: tf.math.reduce_any(x["user"] == [5,6])))
    
    train = train.map(lambda x: (tf.expand_dims(tf.pad(x["xyz"], [[0, 51-tf.shape(x["xyz"])[0]], [0,0]]), -1), tf.one_hot(x["gesture"], 20))).batch(batch_size)
    val = val.map(lambda x: (tf.expand_dims(tf.pad(x["xyz"], [[0, 51-tf.shape(x["xyz"])[0]], [0,0]]), -1), tf.one_hot(x["gesture"], 20))).batch(batch_size)
    test = test_ds.map(lambda x: (tf.expand_dims(tf.pad(x["xyz"], [[0, 51-tf.shape(x["xyz"])[0]], [0,0]]), -1), tf.one_hot(x["gesture"], 20))).batch(batch_size)
    
    data_shape = (batch_size, 51, 3, 1)
    
    # for elem in val.as_numpy_iterator():
    #     print(elem[0].shape)
    #     break
    
    model = models.ConvLSTM1D_a(data_shape)
    model.build_graph(data_shape)
    model.compile(optimizer="Adam", loss="categorical_crossentropy", metrics=["accuracy"])
    
    with tf.device("CPU"):
        hist = model.fit(
            train,
            validation_data=val,
            epochs=200,  # max number ( early stopping expected )
            verbose=1,
            callbacks=[
                ## Early Stop ##
                tf.keras.callbacks.EarlyStopping(
                    monitor="val_loss",
                    min_delta=0.01,
                    patience=20,
                    verbose=0,
                    mode="auto",
                    baseline=None,
                    restore_best_weights=True,
                ),
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
        
        res = model.predict(test)

        test = ds["test"]
        
        with open('submission_accel.csv', "w") as f:
            f.write("id,gesture\n")

            for item, r in zip(test, res):
                f.write(f"{item['id'].numpy()},{np.argmax(r)}\n")    
        

if __name__ == "__main__":
    
    main()