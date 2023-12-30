# Google Gemini Chat Interface

## Overview

A chat interface using the Google Gemini API and Flask for easy interaction with the Gemini language model.

## Prerequisites

- Python 3.10
- Google Gemini API Key

## Getting the Google Gemini API Key

To use this chat interface, you need to obtain an API key from the [Google AI Developer website](https://ai.google.dev/). Follow the instructions on the website to generate your API key.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Shashank-29/GeminiTalk-Flask-Powered-Chat-Interface.git
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
   Make a .env file and add your api key.

    ```bash
    GOOGLE_API_KEY="your-gemini-api-key"
    ```
    
## Usage

1. **Run the Flask application:**

    ```bash
    python app.py
    ```

2. **Enter your questions in the input field and click "Ask the question."**

## Project Structure

- templates/: Contains HTML templates for the Flask app.
- venv/: Virtual environment for Python.
- app.py: Main script for the Flask application.
- requirements.txt: Lists Python dependencies.
