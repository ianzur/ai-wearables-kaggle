"""ai_wearables_video_gestures dataset."""

import tensorflow as tf
import tensorflow_datasets as tfds

from pathlib import Path

# TODO(ai_wearables_video_gestures): Markdown description  that will appear on the catalog page.
_DESCRIPTION = """
Video Gesture dataset created by 2021 AI Wearables UNT course
"""

# TODO(ai_wearables_video_gestures): BibTeX citation
_CITATION = """
"""


class AiWearablesVideoGestures(tfds.core.GeneratorBasedBuilder):
    
    """DatasetBuilder for ai_wearables_video_gestures dataset."""

    VERSION = tfds.core.Version('1.0.0')
    RELEASE_NOTES = {
        '1.0.0': 'Initial release.',
    }

    def _info(self) -> tfds.core.DatasetInfo:
        """Returns the dataset metadata."""
        # TODO(ai_wearables_video_gestures): Specifies the tfds.core.DatasetInfo object
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict({
                # These are the features of your dataset like images, labels ...
                'video': tfds.features.Video(shape=(None, None, None, 3), dtype=tf.dtypes.uint8, encoding_format="jpeg"),
                'label': tfds.features.ClassLabel(names=["clockwise", "counterclockwise", "down", "up", "left", "right"]),
                'frames': tf.dtypes.int32,
                'id': tf.dtypes.string    
            }),
            # If there's a common (input, target) tuple from the
            # features, specify them here. They'll be used if
            # `as_supervised=True` in `builder.as_dataset`.
            supervised_keys=('video', 'label'),  # Set to `None` to disable
            homepage=None,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager: tfds.download.DownloadManager):
        """Returns SplitGenerators."""
        # requires manual download
        path = dl_manager.download_kaggle_data("handgesturevideoclassification")
        # path = Path.cwd() / "data" / "video"

        # Returns the Dict[split names, Iterator[Key, Example]]
        return {
            'train': self._generate_examples(path / 'train' / 'train'),
            'validation': self._generate_examples(path / 'validation' / 'validation'),
            'test': self._generate_examples(path / 'test' / 'test')
        }

    def _generate_examples(self, path):
        """Yields examples."""  

        for p in path.iterdir():

            # eg. "CLOCKWISE, UP, ..."
            if p.is_dir():

                label = p.stem.lower()

                for example in p.iterdir():

                    if example.is_dir():
                        key = example.stem
                        image_list = sorted(list(example.glob("*.jpg")), key=lambda i: i.stem.split("_")[-1])

                        yield key, {'video': image_list, "label": label, "frames": len(image_list), "id": key}

        