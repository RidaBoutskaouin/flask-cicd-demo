# Flask CI/CD Demo

Automated deployment pipeline demonstrating DevOps best practices with Flask, Docker, and GitHub Actions.

## 🚀 Features

- RESTful API with Flask
- Automated testing with pytest
- Docker containerization
- CI/CD pipeline with GitHub Actions
- Health monitoring endpoint

## 📋 Prerequisites

- Python 3.11+
- Docker & Docker Compose
- Git

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/RidaBoutskaouin/flask-cicd-demo
cd flask-cicd-demo
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run locally:
```bash
python app/main.py
```

## 🐳 Docker Usage

Build and run with Docker Compose:
```bash
docker-compose up --build
```

Access the API at `http://localhost:5000`

## 🧪 Testing

Run tests:
```bash
pytest tests/ -v
```

## 📡 API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /api/info` - Project information

## 🔄 CI/CD Pipeline

The pipeline automatically:
1. Runs tests on every push
2. Builds Docker image if tests pass
3. Ready for deployment integration

## 👨‍💻 Author

**Rida** - DevOps & Cloud Engineering Student

## 📝 License

MIT License