import os

def mostrar_menu():
    print("\n🚀 ReviewBrain - Menú Principal")
    print("1. Ejecutar pipeline completo (procesamiento + clustering + guardar CSV)")
    print("2. Abrir dashboard Streamlit")
    print("3. Regenerar modelo de sentimiento")
    print("4. Salir")

def ejecutar_pipeline():
    os.system("python src/run_pipeline.py")

def lanzar_dashboard():
    print("🌐 Iniciando Streamlit...")
    os.system("streamlit run Inicio.py")

def regenerar_modelo():
    from src.spark_ingestion import load_spark_data
    from src.preprocessing import label_data, apply_cleaning, vectorize_text
    from src.sentiment_model import split_data, train_model, evaluate_model, save_model

    df = load_spark_data()
    df = label_data(df)
    df = apply_cleaning(df)
    X, _ = vectorize_text(df['clean_text'])
    y = df['sentiment']
    X_train, X_val, X_test, y_train, y_val, y_test = split_data(X, y)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_val, y_val, name="Validación")
    save_model(model)

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            ejecutar_pipeline()
        elif opcion == "2":
            lanzar_dashboard()
        elif opcion == "3":
            regenerar_modelo()
        elif opcion == "4":
            print("👋 Saliendo. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida. Inténtalo de nuevo.")
