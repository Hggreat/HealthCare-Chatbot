# 🏥 First Aid Chatbot

Welcome to the **First Aid Chatbot** project! This chatbot is designed to provide first aid recommendations through a conversational interface. It leverages **Natural Language Processing (NLP)** techniques and a **neural network** for intent recognition, ensuring accurate and helpful responses.

![Chatbot Illustration](https://cdn-icons-png.flaticon.com/512/4661/4661416.png)

---

## 🚀 Technologies Used

### 🔹 Programming Language
- **Python** 🐍

### 🔹 Libraries & Frameworks
- **NLTK** – Natural language processing
- **TensorFlow & Keras** – Neural network training
- **JSON** – Data storage & retrieval
- **re** – Regular expressions

### 🔹 Data Preprocessing
- **Tokenization**
- **Stemming** (using `LancasterStemmer`)
- **Lemmatization** (using `WordNetLemmatizer`)

---

## 📂 Data Structure
The chatbot uses a **JSON file (`data.json`)** to store:
- **Intents** 🎯
- **Patterns** 📜
- **Responses** 💬

This data is processed during training to create an intelligent model capable of recognizing user intents.

---

## 🧠 Neural Network Model
The chatbot is powered by a **three-layer neural network**:
- **Input Layer** – Processes user input
- **Hidden Layers** – Two dense layers with **ReLU activation**
- **Output Layer** – Softmax activation for intent classification

It is trained using **categorical crossentropy loss** to ensure high accuracy.

![Neural Network Diagram](https://miro.medium.com/max/1000/1*zK_gEjBOtZ7fBg_8E2MzNw.png)

---

## 🔧 Utility Functions

### 🛠️ Bag of Words Function
The `bag_of_words()` function converts user input into a numerical representation that the neural network can understand.

### 👋 Greeting & Thanks Detection
- `is_greeting()` – Identifies greetings like *"Hello!"* or *"Hi there!"*.
- `is_thanks()` – Detects gratitude phrases like *"Thanks!"* or *"Thank you!"*.

---

## 🎯 How to Use

1. **Run the provided Jupyter Notebook** 📓.
2. The chatbot will initiate a conversation 🤖.
3. Enter your questions or first aid concerns 💡.
4. Type **"quit"** to end the conversation ❌.

---

## 📢 Contributing
Got ideas for improvement? Feel free to contribute! Fork the repo, make your changes, and submit a pull request.

---

### ❤️ Support
If you find this chatbot helpful, **give it a ⭐ on GitHub!**

---

Happy chatting! 😊💬

