# ReciclaMais Web App

Aplicação web desenvolvida como Minimum Viable Product (MVP) para otimizar o fluxo de coleta e triagem de materiais recicláveis da Cooperativa ReciclaMais, eliminando gargalos logísticos decorrentes de agendamentos descentralizados.

---

## Alinhamento ODS & Requisitos
- **ODS 12:** Consumo e Produção Responsáveis (Meta 12.5 - Redução de resíduos via reciclagem).
- **Acessibilidade (RNF04):** Conformidade WCAG 2.1 AA (áreas de toque $\ge 48\text{ px}$, contraste otimizado e feedback multimodal).
- **Segurança (RNF01 / RNF02):** Proteção contra CSRF, sanitização de dados e gerenciamento seguro de sessões.

---

## Arquitetura e Pilha Tecnológica
- **Padrão:** Monolítico em Camadas (MVC)
- **Backend:** Python 3.12 com Flask
- **ORM e Banco de Dados:** SQLAlchemy e SQLite
- **Validação de Formulários:** Flask-WTF

---

## Instruções de Instalação e Execução

### 1. Clonar o Repositório
```bash
git clone [https://github.com/seu-usuario/reciclamais-web-app.git](https://github.com/seu-usuario/reciclamais-web-app.git)
cd reciclamais-web-app
```

### 2. Configurar o ambiente virtual python
```bash
python -m venv venv
# No Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# No Linux/macOS:
source venv/bin/activate
```

### 3. Instalar as dependencias
```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação Localmente
```Bash
flask run`
```
### Executando os Testes Automatizados
Para verificar a integridade do sistema através da suíte de testes unitários e de integração:

```Bash
pytest
```