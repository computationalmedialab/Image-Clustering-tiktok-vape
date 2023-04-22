from embeddings import get_embeddings
from dimreduction import dimension_reduction
from clustering import image_clustering
from sklearn.cluster import OPTICS
import numpy as np

img_names = ["list/of/paths/to/images"]

def experiment(model,input_shape,normalize,components,algorithm):
  embedding_df = get_embeddings(img_names, model,input_shape,normalize)
  principal_cp = dimension_reduction(embedding_df,components)
  df,classes,avg_pop = image_clustering(embedding_df,principal_cp,algorithm)
  return df,classes,avg_pop

def experiment_loop(model,input_shape,normalize,components,min_samples,xi):
  embedding_df = get_embeddings(img_names, model,input_shape,normalize)
  class_grid = []
  avpop_grid = []
  for i in range(components[0],components[1],components[2]):
    crow = []
    prow = []
    principal_cp = dimension_reduction(embedding_df,i)
    for j in range(min_samples[0],min_samples[1],min_samples[2]):
      ccol = []
      pcol = []
      for k in np.arange(xi[0],xi[1],xi[2]):
        algorithm   = OPTICS(min_samples=j, xi=k)
        df,classes,avg_pop = image_clustering(embedding_df,principal_cp,algorithm)
        print(i,j,k)
        ccol.append(classes)
        pcol.append(avg_pop)
      crow.append(ccol)
      prow.append(pcol)
    class_grid.append(crow)
    avpop_grid.append(prow)
  return class_grid, avpop_grid


def stats_experiment_loop(model,input_shape,normalize,components,min_samples,xi):
  embedding_df = get_embeddings(model,input_shape,normalize)
  grid = []
  for i in range(components[0],components[1],components[2]):
    row = []
    principal_cp = dimension_reduction(embedding_df,i)
    for j in range(min_samples[0],min_samples[1],min_samples[2]):
      col = []
      for k in np.arange(xi[0],xi[1],xi[2]):
        algorithm   = OPTICS(min_samples=j, xi=k)
        df,stats = image_clustering(embedding_df,principal_cp,algorithm,return_stats=True)
        print(i,j,k)
        stats['stats']=str(i)+'_'+str(j)+'_'+str(k)
        col.append(stats)
      row.append(col)
    grid.append(row)
  return grid