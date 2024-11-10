import pandas as pd

from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans


# SBERT model for book category grouping
model = SentenceTransformer("all-MiniLM-L6-v2")


def classify_books(column: pd.Series, n_clusters: int = 5) -> pd.Series:
    # vectorize strings
    embeddings = model.encode(column.to_list())
    # clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=10)
    kmeans.fit(embeddings)
    labels = kmeans.labels_
    return pd.Series(labels)