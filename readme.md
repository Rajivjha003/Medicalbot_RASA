# 🩺 Medical ChatBot 🤖

![Python](https://img.shields.io/badge/Python-3.8-blue.svg?style=?style=flat-square&logo=python)
![Rasa](https://img.shields.io/badge/Rasa%20Open%20Source-3.6-purple.svg?style=flat-square)

Welcome to the **Medical ChatBot**, your virtual health assistant! This advanced AI-powered chatbot is designed to provide personalized medical advice, answer health-related queries, and assist users in managing their well-being effectively.

## 🚀 Project Overview

The Medical ChatBot leverages state-of-the-art natural language processing (NLP) techniques and machine learning algorithms to understand user inputs, simulate doctor-patient interactions, and deliver accurate medical recommendations. It is built on the Rasa Open Source SDK, making it a powerful tool for healthcare assistance and patient engagement.

### 🌟 Key Features:
- 🧠 Seamless integration of NLP models for understanding user queries and intents.
- 🎯 Implementation of custom actions for dynamic responses and backend computations.
- 🚀 Deployment-ready setup for running the chatbot in various environments.

## 🛠️ Setup and Installation

To run the Medical ChatBot locally, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Create a virtual environment with Python 3.8: `python3.8 -m venv ./venv` and activate it: `source ./venv/bin/activate`.
4. Install Rasa framework: `pip install rasa`.
5. Train the Rasa model: `rasa train`.
6. Start the actions server: `rasa run actions`.
7. Run the Rasa chatbot in the shell: `rasa shell`.

For integration with a UI, start the Rasa server with API enabled:
```shell
rasa run -m models --enable-api --cors "*" 
```

If you have custom actions, start the action server:
```shell
rasa run actions --cors "*" 
```

## 📸 Screenshots

<div style="display: flex; justify-content: center; align-items: center;">
  <img src="https://raw.githubusercontent.com/Rajivjha003/Medicalbot_RASA/main/Images/rasa%20bot1.png" alt="GIF" width="1234" height="214">
</div>


<div style="display: flex; justify-content: center; align-items: center;">
  <img src="https://raw.githubusercontent.com/Rajivjha003/Medicalbot_RASA/main/Images/rasa%20bot2.png" alt="GIF" width="1234" height="214">
</div>


## 🤝 Contributing

Contributions are welcome! If you have any ideas for improvements or new features, feel free to submit a pull request.

## 📝 License

This project is licensed under the [MIT License](LICENSE).
```

Please note that the actual code modification and research on the latest trends in coding would require a more detailed understanding of your project's current state and specific requirements. This is something that would be best done by a developer with access to the project's codebase. However, I'm here to help with any questions or guidance you might need along the way! 😊
