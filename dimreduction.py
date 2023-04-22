from sklearn.decomposition import PCA

def dimension_reduction(embedding_df,components):
  pca = PCA(n_components=components)
  pca.fit(embedding_df.drop(columns='image'))
  p = pca.transform(embedding_df.drop(columns='image'))
  print('###############################################')
  print('number of pca components',len(pca.components_))
  print('###############################################')
  
  return p

