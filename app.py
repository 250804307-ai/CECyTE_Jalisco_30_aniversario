from flask import Flask, render_template, request

app = Flask(__name__)

mensajes = []

@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        semestre = request.form.get('semestre')
        mensaje = request.form.get('mensaje')
        if nombre and mensaje:
            mensajes.append({'nombre': nombre, 'semestre': semestre, 'mensaje': mensaje})
    return render_template('index.html', mensajes=mensajes)

if __name__ == '__main__':
    app.run(debug=True)