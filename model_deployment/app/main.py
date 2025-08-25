from fastapi import FastAPI
import polars as pl
from sentence_transformers import SentenceTransformer
from sklearn.metrics import DistanceMetric
import numpy as np
from app.functions import returnSearchResultsIndexes



# define model name
model_name = 'multi-qa-mpnet-base-dot-v1'
model_path = "app/data/" + model_name

# load the model
model = SentenceTransformer(model_path)

# load video index
df = pl.scan_csv('app/data/video-index.csv')

# create distance metric object
dist_name = 'euclidean'
dist = DistanceMetric.get_metric(dist_name)

# create FastAPI object
app = FastAPI()

# API operations 
@app.get("/")
def health_check():
    return {'health_check': 'OK'}

@app.get("/info")
def info():
    return{'name':'yt-search', 'description':'Semantic search for Kurzgesagt channel'}

@app.get('/search')
def search(query:str):
    idx_result = returnSearchResultsIndexes(query,df,model,dist)
    return df.select(['title','video_id']).collect()[idx_result].to_dict(as_series=False)

