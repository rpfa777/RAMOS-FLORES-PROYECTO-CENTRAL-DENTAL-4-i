from flask import Flask
from database import db

app=Flask(__name__)

from routes.index import index_bp
from routes.pacientes import pacientes_bp
from routes.medicos import medicos_bp
from routes.historial import historial_bp
from routes.controlcitas import controlcitas_bp
from routes.facturaciones import facturaciones_bp

app.register_blueprint(index_bp)
app.register_blueprint(pacientes_bp, url_prefix='/pacientes')
app.register_blueprint(medicos_bp, url_prefix='/medicos')
app.register_blueprint(historial_bp, url_prefix='/historial')
app.register_blueprint(controlcitas_bp, url_prefix='/controlcitas')
app.register_blueprint(facturaciones_bp, url_prefix='/facturaciones')

if __name__ == "__main__":
    app.run(debug=True)