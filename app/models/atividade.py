from database import db

class Atividade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_professor = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    data_atividade = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'id_professor': self.id_professor,
            'descricao': self.descricao,
            'data_atividade': self.data_atividade
        }
