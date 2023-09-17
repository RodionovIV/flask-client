from flask import (
            Flask,
            flash,
            redirect,
            render_template,
            request,
            url_for)

import logging
import settings

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
logging.basicConfig(level=logging.INFO, filename="log.log",filemode="w")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    response = None
    if request.method == 'POST':
        message = request.form['message']
        version = request.form['model_version']
        logging.info(f"MESSAGE: {message}")
        if message:
            if '?' in message:
                response="Вопрос"
            else:
                response = f"Ответ {version}"
        else:
            response = "Введите сообщение"
    logging.info(f"RESPONSE: {response}")
    return render_template('client.html', response=response, versions=settings.versions)

if __name__=="__main__":
    app.run(debug=True, port=5050)