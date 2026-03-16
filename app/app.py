from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "DevSecOps Platform - Arsel DIFFO SOUOP",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "status": "running"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/info')
def info():
    return jsonify({
        "project": "devsecops-arsel",
        "stack": ["Python", "Flask", "Docker", "Kubernetes", "Azure"],
        "author": "Arsel DIFFO SOUOP"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
