from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to Flask CI/CD Demo',
        'status': 'success',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'flask-cicd-demo'
    }), 200

@app.route('/api/info')
def info():
    return jsonify({
        'project': 'Flask CI/CD Pipeline',
        'author': 'Rida',
        'description': 'Automated deployment with GitHub Actions',
        'version': '1.0.0'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)