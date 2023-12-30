from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import google.generativeai as genai

app = Flask(__name__)
load_dotenv()

# Configure generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize generative model and chat
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])
chat_history = []

@app.route('/')
def index():
    return render_template('index.html', last_bot_response=None)

@app.route('/', methods=['POST'])
def ask_question():
    global chat_history
    show_results = False
    last_bot_response = None
    if request.method == 'POST':
        input_text = request.form['input']
        if input_text:
            response = chat.send_message(input_text)
            chat_history.append(('You', input_text))
            chat_history.extend([('Bot', response.text) ])
            show_results = True
            # Get the last response from the bot
            last_bot_response = response.text

            return render_template('index.html', input=input_text, show_results=show_results, chat_history=chat_history,last_bot_response=last_bot_response )

if __name__ == '__main__':
    app.run(debug=True)
