from flask import Blueprint, request, jsonify
from models.atividade import Atividade
from database import db
import requests
from datetime import datetime


atividade_bp = Blueprint('atividade_bp', __name__)

# URL da API de gerenciamento (ajuste conforme necessário)
API_GERENCIAMENTO_URL = "http://host.docker.internal:5000/professores"

@atividade_bp.route('/atividades', methods=['GET'])
def listar_atividades():
    atividades = Atividade.query.all()
    return jsonify([a.to_dict() for a in atividades]), 200


@atividade_bp.route('/atividades', methods=['POST'])
def criar_atividade():
    dados = request.json
    id_professor = dados.get('id_professor')
    descricao = dados.get('descricao')
    data_atividade = dados.get('data_atividade')

    if not (id_professor and descricao and data_atividade):
        return jsonify({"erro": "Dados incompletos"}), 400

    # Validação se o professor existe na API de gerenciamento
    try:
        response = requests.get(f"{API_GERENCIAMENTO_URL}/{id_professor}")
        if response.status_code != 200:
            return jsonify({"erro": "ID do professor inválido"}), 400
    except requests.exceptions.RequestException:
        return jsonify({"erro": "Erro na comunicação com API de gerenciamento"}), 500

    nova_atividade = Atividade(
        id_professor=id_professor,
        descricao=descricao,
        data_atividade=data_atividade
    )

    db.session.add(nova_atividade)
    db.session.commit()

    return jsonify(nova_atividade.to_dict()), 201
