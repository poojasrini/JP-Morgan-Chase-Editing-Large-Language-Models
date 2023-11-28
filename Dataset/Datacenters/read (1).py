import tensorflow as tf
import numpy as np

def mapper(example):

    # feature
    feature_map = {'inputs': tf.io.FixedLenFeature([], tf.string, default_value=''),
                   'targets': tf.io.FixedLenFeature([], tf.string, default_value=''),
                   }
    parsed_example = tf.io.parse_single_example(example, features=feature_map)
    
    return parsed_example["inputs"], parsed_example["targets"]
dataset = tf.data.TFRecordDataset(["./fact_classification_sentencetrain-00000-of-00001"])
dataset = dataset.map(map_func=mapper)

# dataset_length = 0

# for _ in dataset:
#     dataset_length += 1

# print("Length of the dataset:", dataset_length)

for inputs, targets in dataset.take(3000000000000):
    inputs = tf.constant(inputs)
    inputs = inputs.numpy().decode('utf-8')
    
    if (targets == b'P112') and (("founder of" in inputs.lower()) or ("founded by" in inputs.lower())):

        print('inputs={}\ntargets={}'.format(inputs, targets) + "\n")
