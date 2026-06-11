from flask import Blueprint, render_template, request, redirect, url_for
from database import db 

controlcitas_bp = Blueprint('controlcitas', __name__)
col = db['controlcitas']

@controlcitas_bp.route("/")
def ver_citas():
    lista = list(col.find({}, {'_id': 0}))
    return render_template('controlcitas.html', citas=lista)

@controlcitas_bp.route("/nuevo")
def formulario(): 
    return render_template('formcontrolcitas.html')

@controlcitas_bp.route("/guardar", methods=["POST"])
def guardar():
    # Busca el último id_cita numérico para mantener un orden incremental interno
    ultimo = col.find_one({"id_cita": {"$type": "int"}}, sort=[("id_cita", -1)])
    nuevo_id = (ultimo["id_cita"] + 1) if ultimo else 1

    # Insertando los datos estructurados según tu tabla de Control de Citas
    col.insert_one({
        "id_cita":     nuevo_id,
        "paciente":    request.form.get("paciente"),
        "fecha":       request.form.get("fecha"),
        "hora":        request.form.get("hora"),
        "motivo":      request.form.get("motivo"),
        "diagnostico": request.form.get("diagnostico"),
        "tratamiento": request.form.get("tratamiento") if request.form.get("tratamiento") else request.form.get("tratamiento")
    })
    return redirect(url_for('controlcitas.ver_citas'))