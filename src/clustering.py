from sklearn.cluster import KMeans
import json

def run_kmeans(X, n_clusters=5, seed=42):
    model = KMeans(n_clusters=n_clusters, random_state=seed, n_init=10)
    model.fit(X)
    return model

def top_terms_per_cluster(model, vectorizer, n_terms=10):
    terms = vectorizer.get_feature_names_out()
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]

    cluster_terms = {}
    for i in range(model.n_clusters):
        top_terms = [terms[ind] for ind in order_centroids[i, :n_terms]]
        cluster_terms[i] = top_terms
    return cluster_terms

def assign_clusters(model, X, df):
    df['cluster'] = model.predict(X)
    return df
def apply_clustering(df, X, vectorizer, n_clusters=5):
    model = run_kmeans(X, n_clusters=n_clusters)
    df = assign_clusters(model, X, df)
    return df, model

def save_cluster_names(model, vectorizer, path='data/cluster_names.json'):
    cluster_names = top_terms_per_cluster(model, vectorizer, n_terms=3)
    names = {str(k): ", ".join(v) for k, v in cluster_names.items()}
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(names, f, indent=4)

