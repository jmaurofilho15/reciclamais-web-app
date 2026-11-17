# tests/test_app.py
import pytest
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
    # Atualizado para o namespace 'main.' do Blueprint
    response_index = client.get('/' )
    assert response_index.status_code == 200

    response_form = client.get('/formulario')
    assert response_form.status_code == 200

    response_status = client.get('/status')
    assert response_status.status_code == 200

    response_gestao = client.get('/gestao')
    assert response_gestao.status_code == 200

def test_fluxo_completo_doacao_e_gestao(client):
    # 1. Enviar formulário de doação
    dados_doacao = {
        "tipo_material": "Plástico PET",
        "nome": "Sr. Roberto Mendes",
        "telefone": "(11) 98765-4321",
        "cep": "01001-000",
        "endereco": "Rua Exemplo, 123",
        "referencia_volume": "2 sacos grandes na portaria"
    }
    
    response_post = client.post('/formulario', data=dados_doacao, follow_redirects=True)
    assert response_post.status_code == 200
    assert b"#REC-" in response_post.data

    # 2. Verificar se o pedido consta na gestão da cooperativa
    response_gestao = client.get('/gestao')
    assert response_gestao.status_code == 200
    assert b"Sr. Roberto Mendes" in response_gestao.data

    # 3. Obter o pedido salvo para testar a conclusão
    with client.application.app_context():
        pedido = PedidoColeta.query.first()
        pedido_id = pedido.id

    # 4. Executar a conclusão da coleta (rota POST /concluir/<id>)
    response_concluir = client.post(f'/concluir/{pedido_id}', follow_redirects=True)
    assert response_concluir.status_code == 200
    assert b"Coletado" in response_concluir.data