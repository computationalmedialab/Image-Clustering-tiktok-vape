import numpy as np
import pandas as pd

def image_clustering(embedding_df,principal_cp,algorithm,return_stats=False):
    cluster       = algorithm.fit(principal_cp)
    labels        = cluster.labels_
    classified    = len([x for x in labels if x>=0])
    num_cls       = len(np.unique(labels))
    unique_counts = np.unique(labels, return_counts=True)
    avg_cls       = np.mean(np.where(unique_counts[0] > -1,unique_counts[1],0))
    std_cls       = np.std( unique_counts[1] )
    print('___________________________________________________________________')
    print('number of clusters    : ',num_cls)
    print('classified points     : ',classified)
    print('average cluster pop   : ',avg_cls)
    print('standard deviation    : ',std_cls)
    curr_df = pd.DataFrame()
    curr_df['cluster'] = labels
    df = pd.concat([embedding_df["image"],curr_df["cluster"]], axis=1)
    if return_stats==True:
      dic = {}
      dic['clusters'] = num_cls
      dic['coverage'] = classified
      dic['avg']      = avg_cls
      dic['std']      = std_cls
      return df,dic

    return df,classified, avg_cls