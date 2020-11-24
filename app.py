from flask import Flask, render_template
app = Flask(__name__)
# rutas
@app.route('/') # / significa la ruta raiz
def index():
    return render_template('index.html')

@app.route('/saludo/<nombre>/<int:edad>') # nombre ruta
def saludar(nombre, edad):                        
    numeros = [1,2,3,4,5,6,7,8,9]
    return render_template('saludo.html', name =nombre, age=edad, numbers = numeros )

@app.route('/contacto') # nombre ruta
def contacto():
    return 'En la pagina de contacto'

@app.route('/sumar') # nombre ruta
def sumar():
    resultado = 2+2
    return 'La suma de 2+2 =' + str(resultado)

app.run(debug=True, port=5100)