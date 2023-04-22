from experiment import experiment_loop
from sklearn.cluster import OPTICS
from tensorflow import keras
from embeddings import z_norm

input_shape = 224
model       = keras.applications.ResNet50V2(include_top=False,weights='imagenet',input_shape=(input_shape,input_shape,3),pooling='avg')
algorithm   = OPTICS(min_samples=3, xi=0.05)
components  = 15
epsilon     = 10e-10
norm_func   = z_norm

class_grid, avpop_grid = experiment_loop(model,input_shape,None,[5,25,5],[2,7,1],[0.05,0.1,0.01])