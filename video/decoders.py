""" decoding functions

decode jpg image frames into float tensor

"""

import functools

import tensorflow as tf

def decode_frame(serialized_image):
    """Decodes a single frame."""
    return tf.image.decode_jpeg(
        serialized_image,
        channels=3,
    )


def random_manipulation(example):
    """
    some data manipulation, 
    these should probably be implemented as layers in a preprocessing "model" 
    """

    video = example["video"]

    half = tf.constant(0.5)

    state = tf.random.uniform((2,)) #, minval=0, maxval=1, dtype=tf.dtypes.float32)

    flip_lr = state[0] > half
    flip_ud = state[1] > half
    brightness = tf.random.uniform((), minval=-0.5, maxval=0.5)
    quality = tf.random.uniform((), minval=20, maxval=100, dtype=tf.dtypes.int32)

    if flip_lr:
        video = tf.vectorized_map(
        tf.image.flip_left_right,
        video,
        # fn_output_signature=ds_info.features["video"].dtype,
    )

    if flip_ud:
        video = tf.vectorized_map(
        tf.image.flip_up_down,
        video,
        # fn_output_signature=ds_info.features["video"].dtype,
    )
  
    tf.debugging.assert_type(
        video, tf.dtypes.float32, message=None, name=None
    )
    video = tf.vectorized_map(
        functools.partial(tf.image.adjust_brightness, delta=brightness),
        video,
    )
  
    video = tf.map_fn(
        functools.partial(tf.image.adjust_jpeg_quality, jpeg_quality=quality),
        video,
        parallel_iterations=10
    )

    # TODO: salty boy
    # salt = 

    # TODO: some peppa won't hurt
    # pepper = 

    example["video"] = video
    
    return example


def decode_video(example, window_size, loop, start):
    """ 

    This can be called on a single example in eager execution,
    but was designed to be used with a tf.data.Dataset.map(...) call
    
    params:
        example: dict of Tensors
        window_size: int,
            how many frames do you want?
        start: str
            [start, random, centered], where to start sampling window from
        loop: bool (default=True)
            if window is bigger than n-Frames, loop img sequence to satisfy
    
    Notes:
        starts:
            - begin: at beginning of sequence
            - random: at a random frame
                - if loop required?: start = random((frames - window_size), frames))
                - else: start = random(0, (frames - window_size)), (only loop if required)
            - centered: center window in sequence
                - [center - window_size / 2, center + window_size / 2] 
    
    """
    
    print(type(example))

    video = example["video"]
    frames = tf.cast(example["frames"], dtype=tf.dtypes.int32)

    if start == "centered":
        raise NotImplementedError
        # start = frames - (window_size // 2)
        # pass

    elif start == "random":
        # tf.print("random")

        loops_required = window_size // frames
        if window_size == frames:
            loops_required = 0

        video = tf.repeat(video, [loops_required+1])

        sample_start = tf.random.uniform(
                (),
                minval=0,
                maxval=(frames*(loops_required+1) - window_size),
                dtype=tf.dtypes.int32
                )

        video = video[sample_start:sample_start+window_size]

    elif start == "start":
        # tf.print("start")

        if loop:
            loops_required = window_size // frames
            video = tf.repeat(video, [loops_required+1])
            video = video[0:window_size]
        else:
            video = video[0:window_size]
              
    else:
        raise ValueError("please choose one of: start=[start, random, centered] ")

    # decode frames from jpeg to uint8 tensor
    video = tf.map_fn(
            decode_frame,
            video,
            fn_output_signature=tf.dtypes.uint8,
            parallel_iterations=10,
        )

    # convert to float tensor [0, 1] 
    video = tf.cast(video, tf.dtypes.float32) / 255.

    # pack converted tensor to example
    example["video"] = video

    return example


def decode_video_segment(example: dict, num_segments: int, frames_per_segment: int=1, loop: bool=True) -> dict:
    """Decode requested frames, return tensordict with float tensor representing video

    Args:
        example (dict): tensor dictionary
        num_segments (int): split the image sequence into `num_segments`
        frames_per_segment (int, optional): choose n frames from each segment (chooses the "centered" frame). Defaults to 1.
        loop (bool, optional): [description]. Defaults to True.

    Returns:
        dict: tensor dictionary
        
    """
    
    video = example["video"]
    num_frames = tf.cast(example["frames"], dtype=tf.dtypes.int32)
    
    frames_per_segment = num_frames // num_segments
            
    start = frames_per_segment // 2
    end = frames_per_segment * num_segments
    
    video = video[ start : end : frames_per_segment ]
    
    # decode frames from jpeg to uint8 tensor
    video = tf.map_fn(
            decode_frame,
            video,
            fn_output_signature=tf.dtypes.uint8,
            parallel_iterations=10,
        )

    # convert to float tensor [0, 1] 
    video = tf.cast(video, tf.dtypes.float32) / 255.

    # pack converted tensor to example
    example["video"] = video

    return example