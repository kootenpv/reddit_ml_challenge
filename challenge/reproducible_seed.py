# Create a reproducible keras+tf: see https://github.com/keras-team/keras/issues/2280
# Is still only 99% reproducing, but it gets close

import os
import numpy as np
import tensorflow as tf
import random as rn
os.environ['PYTHONHASHSEED'] = '0'

from keras import backend as k

# Running the below code every time
np.random.seed(1)
rn.seed(1)
tf.set_random_seed(1)

sess = tf.Session(graph=tf.get_default_graph())
k.set_session(sess)
