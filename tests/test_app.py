import pytest
from flask import url_for
from app import create_app, db
from app.models import PedidoColeta

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()

def test_rotas_principais(client):
    with client.application.app_context():
        # Uso explícito de url_for com o namespace do Blueprint 'main.'
        assert client.get(url_for('main.index')).status_code == 200
        assert client.get(url_for('main.formulario')).status_code == 200
        assert client.get(url_for('main.status')).status_code == 200
        assert client.get(url_for('main.gestao')).status_code == 200

def test_fluxo_completo_doacao_e_gestao(client):
    with client.application.app_context():
        url_form = url_for('main.formulario')
        url_gestao = url_for('main.gestao')

    # 1. Enviar formulário de doação
    dados_doacao = {
        "tipo_material": "Plástico PET",
        "nome": "Sr. Roberto Mendes",
        "telefone": "(11) 98765-4321",
        "cep": "01001-000",
        "endereco": "Rua Exemplo, 123",
        "referencia_volume": "2 sacos grandes na portaria"
    }
    
    response_post = client.post(url_form, data=dados_doacao, follow_redirects=True)
    assert response_post.status_code == 200
    assert b"#REC-" in response_post.data

    # 2. Verificar se o pedido consta na gestão da cooperativa
    response_gestao = client.get(url_gestao)
    assert response_gestao.status_code == 200
    assert b"Sr. Roberto Mendes" in response_gestao.data

    # 3. Obter o pedido salvo para testar a conclusão
    with client.application.app_context():
        pedido = PedidoColeta.query.first()
        pedido_id = pedido.id
        url_concluir = url_for('main.concluir_pedido', pedido_id=pedido_id)

    # 4. Executar a conclusão da coleta
    response_concluir = client.post(url_concluir, follow_redirects=True)
    assert response_concluir.status_code == 200
    assert b"Coletado" in response_concluir.data