from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculo_viagem', methods=['POST'])
def calculo_viagem():
    try:
        distancia = float(request.form['distancia'])
        velocidade_media = float(request.form['velocidade_media'])

        calculo_tempo = round(distancia / velocidade_media, 2)

        return render_template('index.html', calculo_tempo=calculo_tempo)
    except Exception as e:
        distancia = f'Ocorreu um erro inesperado {e}'
        velocidade_media = f'Ocorreu um erro inesperado {e}'
        return render_template('index.html', distancia=distancia, velocidade_media=velocidade_media)

if __name__ == '__main__':
    app.run(debug=True)
