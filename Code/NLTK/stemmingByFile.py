import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
nltk.download('punkt')
ps = PorterStemmer()
with open("C:\\Users\\Chhaya\\Desktop\\Python\\Code\\NLTK\\input.txt", 'r') as file:
    text = file.read()

words = word_tokenize(text)

stemmed_words = [ps.stem(word) for word in words]
print("Original Words:", words)
print("Stemmed Words:", stemmed_words)
