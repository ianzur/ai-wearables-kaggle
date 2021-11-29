
from typing import List

import pandas as pd
import tensorflow as tf
import tensorflow_datasets as tfds

def split_ds(
    ds: tf.data.Dataset,
    train: List[int],
    val: List[int],
    test: List[int],
    by: str = "participant",
):
    """return tf.data.Datasets split by attribute"""

    ds_train = ds.filter(lambda x: tf.math.reduce_any(x[by] == train))
    ds_val = ds.filter(lambda x: tf.math.reduce_any(x[by] == val))
    ds_test = ds.filter(lambda x: tf.math.reduce_any(x[by] == test))

    return ds_train, ds_val, ds_test


def tfds2pd(ds: tf.data.Dataset, ds_info: tfds.core.DatasetInfo) -> pd.DataFrame:
    """change tf-dataset into pd.Dataframe"""

    # this returns each gesture as a row (accelerometer & time data columns contain lists)
    df = tfds.as_dataframe(ds, ds_info=ds_info)

    # so, explode
    df = df.explode(
        [f"time_stamps/{f}" for f in ds_info.features["time_stamps"].keys()]
        + ["accelerometer"]
    ).reset_index(drop=True)

    # and rename some columns
    df.columns = df.columns.str.replace("time_stamps/", "time_")

    # expand accelerometer data into it's own columns
    df = pd.concat(
        [
            pd.DataFrame(
                df["accelerometer"].to_numpy().tolist(),
                columns=["_".join(("accel", s)) for s in ["x", "y", "z"]],
            ),
            df.loc[:, df.columns != "accelerometer"],
        ],
        axis=1,
    )

    return df
