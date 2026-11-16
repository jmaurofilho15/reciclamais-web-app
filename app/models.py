from app import db
from datetime import datetime

class PedidoColeta(db.Model):
    __tablename__ = 'pedido_coleta'

    id = db.Column(db.Integer, primary_key=True)
    tipo_material = db.Column(db.String(100), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    cep = db.Column(db.String(10), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    numero_pedido = db.Column(db.String(20), nullable=False, unique=True)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<PedidoColeta {self.numero_pedido} - {self.nome}>'