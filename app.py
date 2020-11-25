from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
db = sqlite3.connect('data.db', check_same_thread=False)

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

@app.route('/usuarios') # nombre ruta
def usuarios():
    usuarios = db.execute('select * from usuarios')
    
    usuarios = usuarios.fetchall()
    return render_template('usuarios/listar.html', usuarios=usuarios )

@app.route('/usuarios/crear', methods=['GET','POST']) # nombre ruta
def crear_usuarios():
    if request.method == 'GET':
        return render_template('usuarios/crear.html')
   
    nombres = request.form.get('nombres')
    apellidos = request.form.get('apellidos')
    email = request.form.get('email')
    password = request.form.get('password')

    cursor = db.cursor()
    cursor.execute("""insert into usuarios(
        nombres,
        apellidos,
        email,
        password
    )values (?,?,?,?)
    """, (nombres, apellidos, email, password))

    db.commit()

    return redirect(url_for('usuarios'))

#-----------------------------------------

@app.route('/usuarios/eliminar', methods=['GET','POST'])
def eliminar():
    if request.method == 'GET':
        return render_template('usuarios/eliminar.html')
    id=request.form.get('id')
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    cursor.execute("""DELETE FROM usuarios where id=?""",(id))
    db.commit()
    return redirect(url_for('usuarios'))
#----------------------------------------
@app.route('/usuarios/editar', methods=['GET','POST'])
def editar():
    if request.method == 'GET':
        return render_template('usuarios/editar.html')
    Id=request.form.get('id')
    NewNombres=request.form.get('nombres')
    NewApellidos=request.form.get('apellidos')
    NewEmail=request.form.get('email')
    NewPassword=request.form.get('password')
    cursor = db.cursor()
    cursor.execute("""UPDATE Usuarios SET
                nombres=?,
                apellidos=?, 
                email=?,
                password=?
                WHERE id=?
    """,(NewNombres,NewApellidos,NewEmail,NewPassword,Id))
    db.commit()
    return redirect(url_for('usuarios'))

app.run(debug=True, port=5100)