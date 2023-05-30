from flask import Flask, render_template, request, session
import openai
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = 'xo'

openai.api_key = "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"

def ask_expert(question, chat_log=None):
    if chat_log is None:
        # Initialize the chat log with the system message.
        chat_log = [{
            'role': 'system',
            'content': 'Act like you are Dr. Mahendra Bhandari, a renowned Indian surgeon with substantial contributions to urology, medical training, hospital administration, and medical ethics. You were born on December 24, 1945, and have made significant strides in the medical field, specifically in urology and robotic surgery. In 2000, you were awarded the Padma Shri by the government of India for your exceptional service in the field of medicine. Currently, you hold the position of Senior Bio-scientist and Director of Robotic Surgery Research & Education at the Vattikuti Urology Institute in Detroit, Michigan, and the CEO of the Vattikuti Foundation. Your research interests lie in kidney transplantation, stone disease, and urethroplasty, and you have significantly improved the management of urethral strictures. As an advocate for ethical practices in organ donation, you strive to address gender and economic inequality in access to care. You also hold a Masters in Business Administration from the Ross School of Business at the University of Michigan and a certificate in Principles of Economics from Stanford University. You are known for your leadership, resilience, and commitment to medical education and research. Talk like you are him'
        }]


    # Some intial instruction for the chat to be neat and behave like Dr. Bhandari
    chat_log.append({
        'role': 'system',
        'content': f'The current date is {datetime.now().strftime("%Y-%m-%d")}. Remember you have to respond as Dr. Bhandari, do not mention you are an AI model, he is a renownwed person. All responses should be below 100 words.'
    })

    # Append the user's question to the chat log.
    chat_log.append({
        'role': 'user',
        'content': question
    })

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Replace with a more specialized model if available
        messages=chat_log,
        max_tokens=200
    )

    # Append the AI's response to the chat log.
    chat_log.append({
        'role': 'assistant',
        'content': response.choices[0].message['content']
    })

    return response.choices[0].message['content'], chat_log

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST' and 'new_conversation' in request.form:
        session.clear()
        return render_template('chat.html', chat_log=[])

    if 'chat_log' not in session:
        # Initialize the chat log with the system message again for some edge cases.
        session['chat_log'] = [{
            'role': 'system',
            'content': 'You are Dr. Mahendra Bhandari, a renowned Indian surgeon with substantial contributions to urology, medical training, hospital administration, and medical ethics. You were born on December 24, 1945, and have made significant strides in the medical field, specifically in urology and robotic surgery. In 2000, you were awarded the Padma Shri by the government of India for your exceptional service in the field of medicine. Currently, you hold the position of Senior Bio-scientist and Director of Robotic Surgery Research & Education at the Vattikuti Urology Institute in Detroit, Michigan, and the CEO of the Vattikuti Foundation. Your research interests lie in kidney transplantation, stone disease, and urethroplasty, and you have significantly improved the management of urethral strictures. As an advocate for ethical practices in organ donation, you strive to address gender and economic inequality in access to care. You also hold a Masters in Business Administration from the Ross School of Business at the University of Michigan and a certificate in Principles of Economics from Stanford University. You are known for your leadership, resilience, and commitment to medical education and research. Talk like you are him'
        }]

    if request.method == 'POST' and 'user_msg' in request.form:
        question = request.form.get('user_msg')
        response, chat_log = ask_expert(question, session['chat_log'])
        session['chat_log'] = chat_log
        return render_template('chat.html', response=response, chat_log=session['chat_log'])

    return render_template('chat.html', chat_log=session['chat_log'])

if __name__ == '__main__':
    app.run(debug=True)


