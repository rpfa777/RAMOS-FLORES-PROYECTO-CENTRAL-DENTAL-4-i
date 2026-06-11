from flask import Blueprint, render_template, request, redirect, url_for
from database import db

pacientes_bp = Blueprint('pacientes', __name__)
col = db['pacientes']

@pacientes_bp.route("/")
def ver_pacientes():
    lista = list(col.find({}, {'_id': 0}))
    return render_template('pacientes.html', pacientes=lista)

@pacientes_bp.route("/nuevo")
def formulario():
    return render_template('formpacientes.html')

@pacientes_bp.route("/guardar", methods=["POST"])
def guardar():
    ultimo = col.find_one({"id_paciente": {"$type": "int"}}, sort=[("id_paciente", -1)])
    nuevo_id = (ultimo["id_paciente"] + 1) if ultimo else 1
    col.insert_one({
        "id_paciente":     nuevo_id,
        "nombre_completo": request.form.get("nombre_completo"),
        "f_nacimiento":    request.form.get("f_nacimiento"),
        "genero":          request.form.get("genero"),
        "telefono":        request.form.get("telefono"),
        "correo":          request.form.get("correo"),
        "rfc":             request.form.get("rfc"),
        "aseguradora":     request.form.get("aseguradora")
    })
    return redirect(url_for('pacientes.ver_pacientes'))

@pacientes_bp.route("/borrar/<int:id_paciente>", methods=["POST"])
def borrar(id_paciente):
    col.delete_one({"id_paciente": id_paciente})
    return redirect(url_for('pacientes.ver_pacientes'))

@pacientes_bp.route("/editar/<int:id_paciente>")
def editar(id_paciente):
    paciente = col.find_one({"id_paciente": id_paciente}, {'_id': 0})
    return render_template('editarpaciente.html', paciente=paciente)

@pacientes_bp.route("/actualizar/<int:id_paciente>", methods=["POST"])
def actualizar(id_paciente):
    col.update_one({"id_paciente": id_paciente}, {"$set": {
        "nombre_completo": request.form.get("nombre_completo"),
        "f_nacimiento":    request.form.get("f_nacimiento"),
        "genero":          request.form.get("genero"),
        "telefono":        request.form.get("telefono"),
        "correo":          request.form.get("correo"),
        "rfc":             request.form.get("rfc"),
        "aseguradora":     request.form.get("aseguradora")
    }})
    return redirect(url_for('pacientes.ver_pacientes'))