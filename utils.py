import json
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image

def save_grid(mat,name):
  with open(name, "w") as fp:
    json.dump(mat, fp)
  return

def read_grid(name):
  with open(name, "r") as fp:
    grid = json.load(fp)
  return grid
  
def show_contour(grid,dim1,dim2):
  if dim1+dim2   == 1: grid = np.mean(grid,axis=2)
  elif dim1+dim2 == 2: grid = np.mean(grid,axis=1)
  elif dim1+dim2 == 3: grid = np.mean(grid,axis=0)

  print(grid.shape)

  X, Y = np.meshgrid(np.linspace(0,1,grid.shape[1]), np.linspace(0,1,grid.shape[0]))
  plt.contourf(X,Y,grid,cmap='gist_rainbow_r')
  plt.show()
  return

def open_image(image):
  image = Image.open(image)
  plt.imshow(image)
  plt.show()
  return

def clust_in_df(df,clust_id):
  return df.loc[df['cluster'] == clust_id]["image"]


def search_stat_grid(grid,ncls,cov,avg,std,return_list=False):
  lis = []
  counter = 1
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      for k in range(len(grid[i][j])):
        #print(grid[i][j][k])
        if ncls[0] > grid[i][j][k]['clusters'] or grid[i][j][k]['clusters'] > ncls[1]:
          continue
        if cov[0] > grid[i][j][k]['coverage'] or grid[i][j][k]['coverage'] > cov[1]:
          continue
        if avg[0] > grid[i][j][k]['avg'] or grid[i][j][k]['avg'] > avg[1]:
          continue
        if std[0] > grid[i][j][k]['std'] or grid[i][j][k]['std'] > std[1]:
          continue
        if return_list == True:
          lis.append(grid[i][j][k])
          continue
        print(counter,grid[i][j][k])
        counter += 1
  if return_list == True: return lis
  return
