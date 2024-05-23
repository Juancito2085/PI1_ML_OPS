### Transformaciones
Hacer las transformaciones para reducir lo maximo posible los datos, tener cuidado con Render por el tema de la cantidad de archivos

#preprocesamiento de la columna 'review'
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string
from textblob import TextBlob

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

#Se pasana a minúsculas todas las reviews en una nueva columna llamada 'prepocesed_review'
df_user_reviews['preprocessed_review'] = df_user_reviews['review'].str.lower()

df_user_reviews['preprocessed_review']=df_user_reviews['preprocessed_review'].astype(dtype='str')
#Se eliminan los signos de puntuación
df_user_reviews['preprocessed_review'] = df_user_reviews['preprocessed_review'].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)))

# Se tokeniza la columna 'prepocesed_review'
df_user_reviews['preprocessed_review']=df_user_reviews['preprocessed_review'].apply(word_tokenize)

#se lematiza la columna 'preprocesed_review'para poder utilizarla en el análisis de sentimientos
df_user_reviews['preprocessed_review']=df_user_reviews['preprocessed_review'].apply(lambda x: [lemmatizer.lemmatize(word) for word in x])
### Featuring Engineering
Hacer una columna de analisis de sentimiento 

### Desarrollo API

