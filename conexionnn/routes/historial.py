from flask import Blueprint, render_template, request, redirect, url_for
from database import db 

historial_bp = Blueprint('historial', __name__)
col = db['historial']

@historial_bp.route("/")
def ver_historial():
    lista = list(col.find({}, {'_id': 0}))
    return render_template('historial.html', historiales=lista)

@historial_bp.route("/nuevo")
def formulario(): 
    return render_template('formhistorial.html')

@historial_bp.route("/guardar", methods=["POST"])
def guardar():
    # Busca el último id_historial numérico para autoincrementar de forma interna
    ultimo = col.find_one({"id_historial": {"$type": "int"}}, sort=[("id_historial", -1)])
    nuevo_id = (ultimo["id_historial"] + 1) if ultimo else 1

    # Insertando los datos estructurados según tu tabla de Historial Médico
    col.insert_one({
        "id_historial": nuevo_id,
        "paciente":     request.form.get("paciente"),
        "alergias":     request.form.get("alergias"),
        "enfermedades": request.form.get("enfermedades"),
        "medicamentos": request.form.get("medicamentos"),
        "cirugias":     request.form.get("cirugias"),
        "fumador":      request.form.get("fumador"),
        "diagnostico":  request.form.get("diagnostico")
    })
    return redirect(url_for('historial.ver_historial'))