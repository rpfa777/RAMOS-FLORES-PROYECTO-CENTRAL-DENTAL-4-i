from flask import Blueprint, render_template
from database import db

index_bp = Blueprint('index', __name__)

@index_bp.route("/")
def dashboard():
    total_pacientes     = db['pacientes'].count_documents({})
    total_medicos       = db['medicos'].count_documents({})
    total_historial     = db['historial'].count_documents({})
    total_citas         = db['controlcitas'].count_documents({})
    total_facturaciones = db['facturaciones'].count_documents({})

    # Cambiado de 'central.html' a 'index.html'
    return render_template('index.html',
        total_pacientes=total_pacientes,
        total_medicos=total_medicos,
        total_historial=total_historial,
        total_citas=total_citas,
        total_facturaciones=total_facturaciones)