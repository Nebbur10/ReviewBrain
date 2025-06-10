import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from src.components.header import render_header
from src.components.footer import render_footer

for key in ["Inicio", "Análisis", "Servicios", "Contacto", "Legal"]:
    st.session_state[key] = False

st.set_page_config(page_title="Análisis", layout="wide")

@st.cache_resource
def load_data():
    df = pd.read_csv("data/df_procesado.csv")
    df["clean_text"] = df["clean_text"].fillna("")
    df["rating"] = df["rating"].astype(float)
    return df

@st.cache_resource
def load_cluster_names():
    with open("data/cluster_names.json") as f:
        return json.load(f)

df = load_data()
cluster_names = load_cluster_names()
df["cluster_name"] = df["cluster"].astype(str).map(cluster_names)

render_header()

st.sidebar.title("🔎 Filtros")
cluster_filter = st.sidebar.multiselect("Clústeres", sorted(df["cluster_name"].unique()), default=sorted(df["cluster_name"].unique()))
sentiment_filter = st.sidebar.multiselect("Sentimiento", ["positive", "negative"], default=["positive", "negative"])
stars_filter = st.sidebar.slider("Estrellas", 1.0, 5.0, (1.0, 5.0), step=0.1)
keyword = st.sidebar.text_input("Buscar palabra clave")
product_names = sorted(df["name"].dropna().unique())
product_filter = st.sidebar.multiselect("Producto", product_names, default=product_names)

df_filtered = df[
    df["cluster_name"].isin(cluster_filter) &
    df["sentiment"].isin(sentiment_filter) &
    df["rating"].between(stars_filter[0], stars_filter[1]) &
    df["name"].isin(product_filter)
]

if keyword:
    df_filtered = df_filtered[df_filtered["text"].str.contains(keyword, case=False, na=False)]

st.title("📊 ReviewBrain")
st.caption("Análisis temático y emocional de opiniones de clientes")

col1, col2, col3 = st.columns(3)
col1.metric("📈 Opiniones filtradas", len(df_filtered))
col2.metric("✅ % positivas", f"{(df_filtered['sentiment'] == 'positive').mean() * 100:.1f}%" if len(df_filtered) > 0 else "0%")
col3.metric("⭐ Valoración media", f"{df_filtered['rating'].mean():.2f}" if len(df_filtered) > 0 else "N/A")

col4, col5, col6 = st.columns(3)
if not df_filtered.empty:
    top_cluster = df_filtered["cluster_name"].value_counts().idxmax()
    polarizado = df_filtered.groupby("cluster_name")["sentiment"].apply(
        lambda x: abs((x == 'positive').mean() - (x == 'negative').mean())
    ).idxmax()
    palabra_mas_usada = df_filtered["clean_text"].str.split().explode().value_counts().idxmax()
else:
    top_cluster = polarizado = palabra_mas_usada = "N/A"

col4.metric("📦 Clúster más frecuente", top_cluster)
col5.metric("🎯 Clúster más polarizado", polarizado)
col6.metric("🗣️ Palabra más usada", palabra_mas_usada)

st.subheader("📊 Distribución de sentimientos por clúster")
if not df_filtered.empty:
    grouped = df_filtered.groupby(["cluster_name", "sentiment"]).size().unstack(fill_value=0)
    st.bar_chart(grouped)
else:
    st.info("No hay datos para mostrar el gráfico.")
    
st.subheader("📦 Opiniones por producto")
if not df_filtered.empty:
    grouped_by_product = df_filtered["name"].value_counts().head(10).sort_values(ascending=True)
    st.bar_chart(grouped_by_product)
else:
    st.info("No hay datos para mostrar las opiniones por producto.")
    
st.subheader("📊 Distribución de sentimientos por producto (top 5)")
if not df_filtered.empty:
    top_products = df_filtered["name"].value_counts().head(5).index
    df_top = df_filtered[df_filtered["name"].isin(top_products)]
    sentiment_by_product = df_top.groupby(["name", "sentiment"]).size().unstack(fill_value=0)
    st.bar_chart(sentiment_by_product)
else:
    st.info("No hay datos para mostrar los sentimientos por producto.")
    
st.subheader("⭐ Valoración media por producto (top 5)")

if not df_filtered.empty:
    mean_ratings = df_filtered.groupby("name")["rating"].mean().sort_values(ascending=False).head(5)

    colors = []
    for val in mean_ratings.values:
        if val < 2.0:
            colors.append("red")
        elif val < 3.0:
            colors.append("orange")
        elif val < 3.5:
            colors.append("gold")
        elif val < 4.5:
            colors.append("lightgreen")
        else:
            colors.append("green")

    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.barh(mean_ratings.index, mean_ratings.values, color=colors)
    ax.invert_yaxis()
    ax.set_xlabel("Valoración media")
    ax.set_title("Valoración media por producto")

    for bar in bars:
        width = bar.get_width()
        ax.text(width + 0.05, bar.get_y() + bar.get_height()/2, f"{width:.2f}", va='center')

    st.pyplot(fig)
else:
    st.info("No hay datos para mostrar las valoraciones medias.")

st.subheader("📈 Porcentaje total de sentimientos")
if not df_filtered.empty:
    sentiment_counts = df_filtered["sentiment"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)
else:
    st.info("No hay datos para mostrar el gráfico circular.")

st.subheader("☁️ Nube de palabras por clúster")
if len(cluster_filter) == 1:
    text = " ".join(df[df["cluster_name"] == cluster_filter[0]]["clean_text"].astype(str))
    wordcloud = WordCloud(width=1000, height=400, background_color="white").generate(text)
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
else:
    st.info("Selecciona un único clúster para ver su nube de palabras.")

st.subheader("📝 Opiniones representativas")
if not df_filtered.empty:
    for i, row in df_filtered.head(5).iterrows():
        st.markdown(f"**📦 {row['name']}**")
        st.markdown(f"**⭐ {row['rating']} – {row['sentiment'].capitalize()}**")
        st.write(f"> {row['text'][:300]}...")

else:
    st.info("No hay opiniones que mostrar con estos filtros.")

st.subheader("📥 Exportar opiniones filtradas")
st.download_button(
    label="⬇️ Descargar CSV",
    data=df_filtered.to_csv(index=False).encode("utf-8"),
    file_name="opiniones_filtradas.csv",
    mime="text/csv"
)

render_footer()