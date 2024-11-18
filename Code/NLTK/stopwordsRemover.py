import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')

text = "This is an example sentence demonstrating the removal of stopwords."


words = word_tokenize(text)
stop_words = set(stopwords.words('english'))

filtered_words = [word for word in words if word.lower() not in stop_words]

print("Original Words:", words)
print("Filtered Words:", filtered_words)
