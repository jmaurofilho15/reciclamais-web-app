# app/routes.py
from flask import Blueprint, render_template, redirect, url_for 
from app import db
from app.models import PedidoColeta
from app.forms import ColetaForm
import random

# Criação do Blueprint principal da aplicação
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/formulario', methods=['GET', 'POST'])
def formulario():
    form = ColetaForm()
    if form.validate_on_submit():
        numero_pedido = f"#REC-{random.randint(1000, 9999)}"
        novo_pedido = PedidoColeta(
            tipo_material=form.tipo_material.data,
            nome=form.nome.data,
            telefone=form.telefone.data,
            cep=form.cep.data,
            endereco=form.endereco.data,
            referencia_volume=form.referencia_volume.data,
            numero_pedido=numero_pedido
        )
        db.session.add(novo_pedido)
        db.session.commit()
        return redirect(url_for('main.confirmacao', pedido_id=novo_pedido.id))
    return render_template('formulario.html', form=form)

@main_bp.route('/confirmacao/<int:pedido_id>')
def confirmacao(pedido_id):
    pedido = PedidoColeta.query.get_or_404(pedido_id)
    return render_template('confirmacao.html', pedido=pedido)

@main_bp.route('/status')
def status():
    pedidos = PedidoColeta.query.order_by(PedidoColeta.id.desc()).all()
    return render_template('status.html', pedidos=pedidos)

@main_bp.route('/gestao')
def gestao():
    pedidos = PedidoColeta.query.order_by(PedidoColeta.id.desc()).all()
    return render_template('gestao.html', pedidos=pedidos)

@main_bp.route('/concluir/<int:pedido_id>', methods=['POST'])
def concluir_pedido(pedido_id):
    pedido = PedidoColeta.query.get_or_404(pedido_id)
    pedido.status = 'Coletado'
    db.session.commit()
    return redirect(url_for('main.gestao'))