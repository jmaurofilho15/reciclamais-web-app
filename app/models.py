from datetime import datetime
from app import db

class Doador(db.Model):
    __tablename__ = 'doador'
    id_doador = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    cep = db.Column(db.String(10), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)
    
    pedidos = db.relationship('PedidoColeta', backref='doador', lazy=True)

class PedidoColeta(db.Model):
    __tablename__ = 'pedido_coleta'
    id_pedido = db.Column(db.Integer, primary_key=True)
    id_doador = db.Column(db.Integer, db.ForeignKey('doador.id_doador'), nullable=False)
    tipo_material = db.Column(db.String(50), nullable=False)
    volume_estimado = db.Column(db.String(50), nullable=False, default='Padrão')
    status_pedido = db.Column(db.String(20), nullable=False, default='Pendente')
    data_solicitacao = db.Column(db.DateTime, default=datetime.utcnow)