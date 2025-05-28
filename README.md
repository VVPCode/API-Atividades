
# API de Controle de Atividades

## 📑 Descrição

Esta API faz parte de um sistema de gerenciamento escolar, funcionando como um **microsserviço responsável pelo controle de atividades acadêmicas**, vinculadas a um **ID de professor** fornecido pela API principal de gerenciamento escolar.

Permite cadastrar e consultar atividades, facilitando o acompanhamento de tarefas, provas e projetos.

---

## 🚀 Tecnologias Utilizadas

- Python
- Flask (framework web)
- SQLAlchemy (ORM)
- SQLite (banco de dados)
- Docker (containerização)
- Arquitetura MVC (Model-View-Controller)

---

## 🏗️ Arquitetura e Estrutura do Projeto

A API foi construída utilizando o padrão MVC:

```
api-atividades/
│
├── app/
│   ├── __init__.py          # Inicialização da aplicação
│   ├── models/              # Modelos de dados (Atividade)
│   ├── controllers/         # Controladores (Rotas e lógica de negócio)
│   ├── database.py          # Configuração do banco de dados
│   └── config.py            # Configuração geral da aplicação
│
├── Dockerfile               # Configuração do container Docker
├── requirements.txt         # Dependências da aplicação
└── README.md                # Este arquivo
```

---

## 🔗 Integração com o Ecossistema de Microsserviços

| Serviço               | Descrição                                              |
|-----------------------|--------------------------------------------------------|
| API Principal         | Gestão de professores, turmas e alunos.               |
| API de Controle de Atividades | Recebe o ID do professor para validar as atividades criadas. |

🔗 **Validação Externa:** Antes de criar uma atividade, a API consulta a API principal para verificar se o **ID do professor** informado existe.

---

## 🛠️ Rotas da API

### ✅ `GET /atividades`

- **Descrição:** Lista todas as atividades cadastradas.
- **Resposta:** Lista de atividades em JSON.

### ✅ `POST /atividades`

- **Descrição:** Cria uma nova atividade vinculada a um professor.
- **Corpo (JSON):**
```json
{
  "id_professor": 1,
  "descricao": "Trabalho de Matemática",
  "data_entrega": "2025-06-01"
}
```
- **Validação:** Verifica se o `id_professor` existe na API principal.
- **Resposta:** Dados da atividade criada.

---

## 🐳 Executando com Docker

### 📦 Build da imagem
```bash
docker build -t api-atividades .
```

### 🚀 Executar o container
```bash
docker run -d -p 5001:5000 --name atividades api-atividades
```

A API estará disponível em:
```
http://localhost:5001
```

---

## 💻 Executando Localmente (sem Docker)

1. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Rode a aplicação:
```bash
python app
```

A API estará em:
```
http://localhost:5000
```

---

## ⚙️ Configuração

O link da API principal deve ser configurado dentro do arquivo:

```python
API_GERENCIAMENTO_URL = "http://<URL_DA_API_PRINCIPAL>"
```

---

## 🧠 Autor e Créditos

- Desenvolvido por: [Seu Nome]
- Curso: Sistemas de Informação
- GitHub: [Seu GitHub]
- LinkedIn: [Seu LinkedIn]

---

## 📄 Licença

Este projeto é livre para uso educacional.
