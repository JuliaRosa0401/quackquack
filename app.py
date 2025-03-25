from flask import Flask, request, render_template
import requests

app= Flask(__name__)
API_ENDPOINT ='https://random-d.uk/api/random'

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    nome = request.form.get('nome', None)

    if not nome:
        return render_template('index.html', erro="Você precisa informar um nome!")

    response = requests.get(API_ENDPOINT)

    if response.status_code == 200:
        data = response.json()
        url_imagem = data['url'] 
        print(f"URL da imagem: {url_imagem}")
        return render_template('index.html', nome=nome, url_imagem=url_imagem)
    else:
        print(response.status_code)
        return render_template('index.html', erro="Erro no sistema! O pato foi nadar!")    


if __name__ == '__main__':
    app.run(debug=True)