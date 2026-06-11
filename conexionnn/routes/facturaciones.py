from flask import Blueprint, render_template, request, redirect, url_for
from database import db 

facturaciones_bp = Blueprint('facturaciones', __name__)
col = db['facturaciones']

@facturaciones_bp.route("/")
def ver_facturaciones():
    lista = list(col.find({}, {'_id': 0}))
    return render_template('facturaciones.html', facturaciones=lista)

@facturaciones_bp.route("/nuevo")
def formulario(): 
    return render_template('formfacturaciones.html')

@facturaciones_bp.route("/guardar", methods=["POST"])
def guardar():
    # Busca el último id_factura numérico para mantener un orden incremental interno
    ultimo = col.find_one({"id_factura": {"$type": "int"}}, sort=[("id_factura", -1)])
    nuevo_id = (ultimo["id_factura"] + 1) if ultimo else 1

    # Insertando los datos estructurados según tu tabla de Facturaciones
    col.insert_one({
        "id_factura": nuevo_id,
        "paciente":   request.form.get("paciente"),
        "total":      request.form.get("total"),
        "pagado":     request.form.get("pagado"),
        "saldo":      request.form.get("saldo"),
        "metodo":     request.form.get("metodo")
    })
    return redirect(url_for('facturaciones.ver_facturaciones'))