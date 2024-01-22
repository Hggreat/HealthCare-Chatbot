Introduction
Welcome to my chatbot project! This project is designed to provide first aid recommendations through a conversational interface. The chatbot is built using natural language processing techniques and a neural network for intent recognition.

Technologies Used
Programming Language: Python
Libraries and Frameworks:
nltk for natural language processing
tensorflow and keras for building and training the neural network
json for data storage and retrieval
re for regular expressions
Data Preprocessing:
Tokenization
Stemming (using LancasterStemmer)
Lemmatization (using WordNetLemmatizer)
Data
The chatbot uses a JSON file (data.json) to store intents, patterns, and responses. This data is processed during training to create a model capable of recognizing user intents.

Neural Network Model
The core of the chatbot is a neural network with three layers: two dense layers with ReLU activation functions and a final dense layer with softmax activation. The model is trained using categorical crossentropy loss.

Utility Functions
Bag of Words Function
The bag_of_words function takes a user input and converts it into a numerical representation for the neural network.

Greeting and Thanks Detection Functions
Two functions, is_greeting and is_thanks, are implemented to detect greetings and expressions of gratitude, respectively.

How to Use
Simply run the provided Jupyter Notebook. The chatbot will initiate a conversation, and you can input your questions or seek first aid recommendations. Type "quit" to end the conversation.
