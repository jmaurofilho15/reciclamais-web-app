from app import create_app

# Instancia a aplicação utilizando o padrão Application Factory
app = create_app()

if __name__ == "__main__":
    # Execução local de desenvolvimento (porta padrão 5000)
    app.run(host="0.0.0.0", port=5000, debug=True)