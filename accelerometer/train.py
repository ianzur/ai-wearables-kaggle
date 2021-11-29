
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


def format(example):
    
    xyz = example["xyz"]
    gesture = example["gesture"]
    
    # pad with zeros to max length (51)
    xyz = tf.expand_dims(tf.pad(xyz, [[0, 51-tf.shape(xyz)[0]], [0,0]]), -1)
    # one hot encode gesture label (20 classes)
    gesture = tf.one_hot(gesture, 20)
    
    example["xyz"] = xyz
    example["gesture"] = gesture
    
    return example


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
    
    # create validation set
    train = train_ds.filter(lambda x: tf.math.reduce_any(x["user"] == [0,1,2,3,4]))
    val = train_ds.filter((lambda x: tf.math.reduce_any(x["user"] == [5,6])))
    
    train = train.map(format).batch(batch_size)
    train = train.map(lambda x: (x["xyz"], x["gesture"]))
    
    val = val.map(format).batch(batch_size)
    val = val.map(lambda x: (x["xyz"], x["gesture"]))

    # only format data, don't create tuple
    test = test_ds.map(format).batch(batch_size)
    
    data_shape = (batch_size, 51, 3, 1)
    
    # for elem in val.as_numpy_iterator():
    #     print(elem[0].shape)
    #     break
    
    model = models.ConvLSTM1D_a(data_shape)
    model.build_graph(data_shape)
    model.compile(optimizer="Adam", loss="categorical_crossentropy", metrics=["accuracy"])
    
    hist = model.fit(
        train,
        validation_data=val,
        epochs=400,  # max number ( early stopping expected )
        verbose=1,
        callbacks=[
            ## Early Stop ##
            tf.keras.callbacks.EarlyStopping(
                monitor="val_loss",
                min_delta=0.001,
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
    
    with open('submission_accel.csv', "w") as f:
        f.write("id,gesture\n")

        for batch in test.as_numpy_iterator():
            results = model.predict(batch["xyz"])
            
            for example, result in zip(batch["id"], results):               
                f.write(f"{example},{np.argmax(result)}\n")
        

if __name__ == "__main__":
    
    main()