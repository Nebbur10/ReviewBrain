import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words]
    return " ".join(tokens)

def apply_cleaning(df):
    df['clean_text'] = df['text'].apply(clean_text)
    return df

def vectorize_text(corpus, max_features=5000):
    vectorizer = TfidfVectorizer(max_features=max_features)
    X = vectorizer.fit_transform(corpus)
    return X, vectorizer

def assign_sentiment(rating):
    if rating >= 4:
        return 'positive'
    elif rating <= 2:
        return 'negative'
    else:
        return 'neutral'

def label_data(df, remove_neutral=True):
    df['sentiment'] = df['rating'].apply(assign_sentiment)

    if remove_neutral:
        df = df[df['sentiment'] != 'neutral']
    
    return df
