from flask import Blueprint, render_template, request, redirect, url_for
from database import db 

medicos_bp = Blueprint('medicos', __name__)
col = db['medicos']

@medicos_bp.route("/")
def ver_medicos():
    lista = list(col.find({}, {'_id': 0}))
    return render_template('medicos.html', medicos=lista)

@medicos_bp.route("/nuevo")
def formulario(): 
    return render_template('formmedicos.html')

@medicos_bp.route("/guardar", methods=["POST"])
def guardar():
    # Busca el último id_medico numérico para autoincrementar
    ultimo = col.find_one({"id_medico": {"$type": "int"}}, sort=[("id_medico", -1)])
    nuevo_id = (ultimo["id_medico"] + 1) if ultimo else 1

    # Insertando los datos estructurados como en tu nueva tabla de médicos
    col.insert_one({
        "id_medico":    nuevo_id,
        "nombre":       request.form.get("nombre"),
        "especialidad": request.form.get("especialidad"),
        "cedula":       request.form.get("cedula"),
        "sala":         request.form.get("sala"),
        "telefono":     request.form.get("telefono"),
        "email":        request.form.get("email")
    })
    return redirect(url_for('medicos.ver_medicos'))