from spark_ingestion import load_spark_data as load_data
from preprocessing import label_data, apply_cleaning, vectorize_text
from sentiment_model import split_data, train_model, evaluate_model, save_model
from clustering import apply_clustering, save_cluster_names

def main():
    print("Cargando datos con PySpark...")
    df = load_data()

    print("Etiquetando sentimientos...")
    df = label_data(df)

    print("Limpiando texto...")
    df = apply_cleaning(df)

    print("Vectorizando texto con TF-IDF...")
    X, vectorizer = vectorize_text(df["clean_text"])

    print("Dividiendo conjuntos de entrenamiento, validación y prueba...")
    X_train, X_val, X_test, y_train, y_val, y_test = split_data(X, df["sentiment"])

    print("Entrenando modelo de sentimiento...")
    model = train_model(X_train, y_train)

    print("Evaluación en validación:")
    evaluate_model(model, X_val, y_val, name="Validación")

    print("Guardando modelo de sentimiento...")
    save_model(model)

    print("Aplicando clustering KMeans...")
    df, clustering_model = apply_clustering(df, X, vectorizer)

    print("Guardando nombres de clústeres...")
    save_cluster_names(clustering_model, vectorizer)

    print("Guardando CSV procesado...")
    df.to_csv("data/df_procesado.csv", index=False)

    print("Pipeline completado con éxito.")

if __name__ == "__main__":
    main()
