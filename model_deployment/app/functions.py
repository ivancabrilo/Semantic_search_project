import numpy as np
import polars as pl
import sentence_transformers
import sklearn
import sklearn.metrics




def returnSearchResultsIndexes(query: str, index: pl.lazyframe.frame.LazyFrame, model, dist: any) -> np.ndarray:
    """
        Function to return indexes of top search results
    """
    
    # embed query
    query_embedding = model.encode(query).reshape(1, -1)

    # Get column names without triggering schema resolution warning
    column_names = index.collect_schema().names()
    
    # compute distances between query and titles/transcripts
    dist_arr = (
        dist.pairwise(index.select(column_names[4:772]).collect(), query_embedding) +
        dist.pairwise(index.select(column_names[772:]).collect(), query_embedding)
    )

    # search paramaters
    threshold = 40 # eye balled threshold for manhatten distance
    top_k = 5

    # evaluate videos close to query based on threshold
    idx_below_threshold = np.argwhere(dist_arr.flatten()<threshold).flatten()
    # keep top k closest videos
    idx_sorted = np.argsort(dist_arr[idx_below_threshold], axis=0).flatten()

    # return indexes of search results
    return idx_below_threshold[idx_sorted][:top_k]