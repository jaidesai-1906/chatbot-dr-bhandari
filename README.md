# Chatbot using GPT 3 and Flask

This is an interactive chatbot (a basic MVP) that imitates the behavior of **Dr. Mahendra Bhandari**, a renowned Indian surgeon. The chatbot uses OpenAI's **GPT-3.5-turbo** model to generate responses based on the user's inputs.

The application utilizes a variety of prompting techniques to ensure that the generated responses are in line with Dr. Bhandari's persona and knowledge. The initial prompt is structured as a system message instructing the assistant to act like Dr. Bhandari. The project also append system messages to the chat log to continually remind the model of the context and the character it needs to maintain.

The chatbot provides an easy and intuitive way to interact with a simulation of Dr. Bhandari, providing responses from his point of view in a conversation.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need Python 3.6 or later to run the chatbot. 

## Quick Start

### Clone the repository:
```bash
git clone https://github.com/jaidesai-1906/chatbot-dr-bhandari.git
cd chatbot-dr-bhandari
```

### Install dependencies:
```bash
pip install -r requirements.txt
```
### Update with your open-ai-key

### Run the application:
```bash
python app.py
```
Then visit `http://localhost:5000` in your browser.

## Project Structure

The project has the following structure:

- `app.py`: This is the main file that runs the Flask application.
- `templates/chat.html`: This file contains the HTML for the chat interface.
- `static/img`: This directory contains the avatar images for the user and Dr. Bhandari.

## Future Work

- **Voice Input and Output**: Incorporating voice input/output functionality would make the chatbot more accessible and interactive. Tools such as Google's Text-to-Speech and Speech-to-Text APIs can be used for this.

- **3D Interactive Figure**: To create a more realistic experience, a 3D interactive figure of Dr. Bhandari could be added. This would require using WebGL or a JavaScript library like three.js for 3D graphics.

- **Improved Model Training**: While the chatbot currently uses the GPT-3 model, future improvements could involve training and fine-tuning the model with more specific data related to Dr. Bhandari and his field of expertise.

- **Multilingual Support**: The chatbot could be expanded to support multiple languages, making it accessible to a wider audience.
