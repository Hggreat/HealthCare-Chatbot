import nltk
from nltk.stem import LancasterStemmer , WordNetLemmatizer
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import random
import json
import pickle
import re


nltk.download('punkt')
nltk.download('wordnet')

with open("data.json") as file:
    data = json.load(file)

words = []
labels = []
docs_x = []
docs_y = []

stemmer = LancasterStemmer()
lemmatizer = WordNetLemmatizer()

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])

    if intent["tag"] not in labels:
        labels.append(intent["tag"])

words = [stemmer.stem(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))

labels = sorted(labels)

training = []
output = []

out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []

    wrds = [stemmer.stem(w) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)
    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)

training = np.array(training)
output = np.array(output)

model = Sequential([
    Dense(8, input_shape=(len(training[0]),), activation='relu'),
    Dense(8, activation='relu'),
    Dense(len(output[0]), activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

try:
    model.load_weights("model.h5")
except:
    model.fit(training, output, epochs=1000, batch_size=8, verbose=1)
    model.save_weights("model.h5")

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s = re.sub(r'\b(?:my|your|his|her|its|our|their)\b', '', s, flags=re.IGNORECASE)
    s_words = nltk.word_tokenize(s)
    s_words = [lemmatizer.lemmatize(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return np.array(bag)


def is_greeting(sentence):
    greetings = ["hello", "hi", "hey", "howdy", "hola"]
    for word in greetings:
        if re.search(r'\b' + re.escape(word) + r'\b', sentence, re.IGNORECASE):
            return True
    return False

def is_thanks(sentence):
    thanks_keywords = ["thanks", "thank you", "appreciate it", "grateful"]
    for word in thanks_keywords:
        if re.search(r'\b' + re.escape(word) + r'\b', sentence, re.IGNORECASE):
            return True
    return False

def chat():
    print("Bot: Hi there! I'm here to help you with first aid recommendations. How can I help you?")
    
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            print("Bot: Take care! If you have any more questions, feel free to ask.")
            break

        if "thank you" in inp.lower():
            print("Bot: You're welcome! If you have any more questions, feel free to ask.")
            break

        if is_greeting(inp):
            print("Bot: Hello! How can I assist you today?")
            continue

        results = model.predict(np.array([bag_of_words(inp, words)]))[0]
        results_index = np.argmax(results)
        tag = labels[results_index]

        if results[results_index] > 0.5:
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']
            print("Bot:", random.choice(responses))
        else:
            print("Bot: I didn't get that, try again")
            
            
chat()
