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
    ultimo = col.find_one({"id_factura": {"$type": "int"}}, sort=[("id_factura", -1)])
    nuevo_id = (ultimo["id_factura"] + 1) if ultimo else 1
    col.insert_one({
        "id_factura": nuevo_id,
        "paciente":   request.form.get("paciente"),
        "total":      request.form.get("total"),
        "pagado":     request.form.get("pagado"),
        "saldo":      request.form.get("saldo"),
        "metodo":     request.form.get("metodo")
    })
    return redirect(url_for('facturaciones.ver_facturaciones'))

@facturaciones_bp.route("/borrar/<int:id_factura>", methods=["POST"])
def borrar(id_factura):
    col.delete_one({"id_factura": id_factura})
    return redirect(url_for('facturaciones.ver_facturaciones'))

@facturaciones_bp.route("/editar/<int:id_factura>")
def editar(id_factura):
    factura = col.find_one({"id_factura": id_factura}, {'_id': 0})
    return render_template('editarfacturacion.html', factura=factura)

@facturaciones_bp.route("/actualizar/<int:id_factura>", methods=["POST"])
def actualizar(id_factura):
    col.update_one({"id_factura": id_factura}, {"$set": {
        "paciente": request.form.get("paciente"),
        "total":    request.form.get("total"),
        "pagado":   request.form.get("pagado"),
        "saldo":    request.form.get("saldo"),
        "metodo":   request.form.get("metodo")
    }})
    return redirect(url_for('facturaciones.ver_facturaciones'))