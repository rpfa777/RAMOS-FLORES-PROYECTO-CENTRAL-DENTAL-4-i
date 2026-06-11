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
    ultimo = col.find_one({"id_historial": {"$type": "int"}}, sort=[("id_historial", -1)])
    nuevo_id = (ultimo["id_historial"] + 1) if ultimo else 1
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

@historial_bp.route("/borrar/<int:id_historial>", methods=["POST"])
def borrar(id_historial):
    col.delete_one({"id_historial": id_historial})
    return redirect(url_for('historial.ver_historial'))

@historial_bp.route("/editar/<int:id_historial>")
def editar(id_historial):
    historial = col.find_one({"id_historial": id_historial}, {'_id': 0})
    return render_template('editarhistorial.html', historial=historial)

@historial_bp.route("/actualizar/<int:id_historial>", methods=["POST"])
def actualizar(id_historial):
    col.update_one({"id_historial": id_historial}, {"$set": {
        "paciente":     request.form.get("paciente"),
        "alergias":     request.form.get("alergias"),
        "enfermedades": request.form.get("enfermedades"),
        "medicamentos": request.form.get("medicamentos"),
        "cirugias":     request.form.get("cirugias"),
        "fumador":      request.form.get("fumador"),
        "diagnostico":  request.form.get("diagnostico")
    }})
    return redirect(url_for('historial.ver_historial'))