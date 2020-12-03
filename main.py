import tensorflow as tf
import matplotlib
import tensorflow_datasets as tfds

dataset, dataset_info = tfds.load('oxford_flowers102', with_info=True, as_supervised=True)
