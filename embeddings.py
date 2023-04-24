from tensorflow.keras.preprocessing import image
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import smart_resize
import pandas as pd
import numpy as np


def z_norm(df, epsilon=10e-10):
    return (df-df.mean())/(df.std()+epsilon)

def min_max_norm(df, epsilon=10e-10):
    return (df-df.min())/(df.max()-df.min()+epsilon)

def exp_norm(df, epsilon=10e-10):
    em = df.to_numpy()
    mean = np.mean(em,axis=0)
    lam = 1/(mean+epsilon)
    exfit = lam*np.exp(-lam*em)
    exfit = (exfit - np.min(exfit,axis=0)) / (np.max(exfit,axis=0)-np.min(exfit,axis=0)+epsilon)
    return pd.DataFrame(exfit,index=df.index)

def extract_features(file, model, input_shape):
    img = image.load_img(file)
    img = image.img_to_array(img)
    img = smart_resize(img, (input_shape, input_shape), interpolation='bilinear')
    img = np.expand_dims(img, axis=0)
    features = model.predict(img, use_multiprocessing=True)
    return features.ravel()

def frame_embeddings(data, normalize=None):
    embedding_df = pd.DataFrame.from_dict(data)
    embedding_df = embedding_df.T
    print(embedding_df.shape)
    if normalize is not None : embedding_df = normalize(embedding_df)
    embedding_df['image'] = embedding_df.index
    embedding_df = embedding_df.reset_index()
    embedding_df = embedding_df.drop(['index'], axis=1)
    return embedding_df

def get_embeddings(img_names, model,input_shape, normalize=None):
    data = {}
    for img in img_names:
      feat = extract_features(img, model, input_shape)
      data[img] = feat
    embedding_df = frame_embeddings(data, normalize)
    return embedding_df

