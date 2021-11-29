"""ai_wearables_accelerometer_gestures dataset."""

import tensorflow as tf
import tensorflow_datasets as tfds

# TODO(ai_wearables_accelerometer_gestures): Markdown description  that will appear on the catalog page.
_DESCRIPTION = """
Description is **formatted** as markdown.

It should also contain any processing which has been applied (if any),
(e.g. corrupted example skipped, images cropped,...):
"""

# TODO(ai_wearables_accelerometer_gestures): BibTeX citation
_CITATION = """
"""


class AiWearablesAccelerometerGestures(tfds.core.GeneratorBasedBuilder):
    """DatasetBuilder for ai_wearables_accelerometer_gestures dataset."""

    VERSION = tfds.core.Version('1.0.0')
    RELEASE_NOTES = {
        '1.0.0': 'Initial release.',
    }

    def _info(self) -> tfds.core.DatasetInfo:
        """Returns the dataset metadata."""
        # TODO(ai_wearables_accelerometer_gestures): Specifies the tfds.core.DatasetInfo object
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict({
                # These are the features of your dataset like images, labels ...
                'xyz': tfds.features.Tensor(shape=(None, 3), dtype=tf.float32),
                'gesture': tfds.features.ClassLabel(num_classes=20),
                'id': tf.dtypes.int32,
                'user': tf.dtypes.int32,
            }),
            # If there's a common (input, target) tuple from the
            # features, specify them here. They'll be used if
            # `as_supervised=True` in `builder.as_dataset`.
            supervised_keys=('accel', 'label'),  # Set to `None` to disable
            homepage=None,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        """Returns SplitGenerators."""
        # TODO(ai_wearables_accelerometer_gestures): Downloads the data and defines the splits
        path = dl_manager.download_kaggle_data("accelerometer-gesture-classification")

        # TODO(ai_wearables_accelerometer_gestures): Returns the Dict[split names, Iterator[Key, Example]]
        return {
            'train': self._generate_examples(path / 'train.csv'),
            'test': self._generate_examples(path / 'test.csv')
        }

    def _generate_examples(self, path):
        """Yields examples."""
        # TODO(ai_wearables_accelerometer_gestures): Yields (key, example) tuples from the dataset
        
        pd = tfds.core.lazy_imports.pandas
        
        df = pd.read_table(path, sep=",", converters={'x': eval, 'y': eval, 'z': eval})
        
        if 'gesture' not in df.columns:
            df["gesture"] = -1
            
        for row in df.itertuples():
            
            yield row.Index, {
                'xyz': [[x,y,z] for x,y,z in zip(row.x, row.y, row.z)],
                'gesture': row.gesture,
                'id': row.id,
                'user': row.user                
            } 