from flask import Flask, request, jsonify, render_template
import requests

# Define the Rasa API URL
RASA_API_URL = "http://localhost:5005/webhooks/rest/webhook"

app = Flask(__name__)

# Define route for rendering the index.html template
@app.route("/")
def index():
    return render_template("index.html")

# Define webhook endpoint for handling user messages
@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the user message from the request
    user_message = request.json['message']
    print("User Message:", user_message)

    # Send user message to Rasa and get bot's response
    rasa_response = requests.post(RASA_API_URL, json={"message": user_message})
    rasa_response_json = rasa_response.json()
    print("Rasa Response:", rasa_response_json)

    # Extract bot's response
    bot_response = rasa_response_json[0]["text"] if rasa_response_json else "Sorry, I didn't understand that"

    # Return the bot's response to the user
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(port=5055)
