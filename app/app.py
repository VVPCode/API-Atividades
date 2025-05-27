from flask import Flask
from config import Config
from database import db
from controllers.atividade_controller import atividade_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(atividade_bp)

    @app.route('/')
    def home():
        return "API de Controle de Atividades no ar!"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
