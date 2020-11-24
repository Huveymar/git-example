from flask import Flask, render_template, request
app = Flask(__name__)
# rutas
@app.route('/') # / significa la ruta raiz
def index():
    return render_template('index.html')

@app.route('/saludo/<nombre>/<int:edad>') # nombre ruta
def saludar(nombre, edad):                        
    numeros = [1,2,3,4,5,6,7,8,9]
    return render_template('saludo.html', name =nombre, age=edad, numbers = numeros )

@app.route('/contacto', methods=['GET','POST']) # nombre ruta
def contacto():
    #obteniendo formulario de contacto
    if request.method == 'GET':
        return render_template('contacto.html')
    #guardando la informacion de contacto
    nombres = request.form.get('nombres')
    email = request.form.get('email')
    celular = request.form.get('celular')
    observacion = request.form.get('observacion')
    return 'Guardando información ' + nombres
     

@app.route('/sumar') # nombre ruta
def sumar():
    resultado = 2+2
    return 'La suma de 2+2 =' + str(resultado)

app.run(debug=True, port=5100)