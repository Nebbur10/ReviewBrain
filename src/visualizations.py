import matplotlib.pyplot as plt
from wordcloud import WordCloud

def plot_sentiment_distribution(df):
    grouped = df.groupby(['cluster', 'sentiment']).size().unstack(fill_value=0)
    grouped.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title('Distribución de sentimientos por clúster')
    plt.xlabel('Clúster')
    plt.ylabel('Número de opiniones')
    plt.legend(title='Sentimiento')
    plt.tight_layout()
    plt.show()

def generate_wordcloud(df, cluster_id):
    text = ' '.join(df[df['cluster'] == cluster_id]['clean_text'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Clúster {cluster_id} - Nube de palabras')
    plt.show()

def show_examples(df, cluster_id, n=5):
    print(f'🟦 Ejemplos del clúster {cluster_id}:')
    examples = df[df['cluster'] == cluster_id]['text'].head(n)
    for i, text in enumerate(examples):
        print(f'{i+1}. {text.strip()[:300]}...\n')
