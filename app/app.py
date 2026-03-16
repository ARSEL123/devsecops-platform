from flask import Flask, jsonify, render_template_string
import os
import datetime

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevSecOps Platform — Arsel DIFFO SOUOP</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', sans-serif;
            background: #0f172a;
            color: #e2e8f0;
            min-height: 100vh;
        }
        header {
            background: #1e293b;
            border-bottom: 2px solid #3b82f6;
            padding: 20px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        header h1 { font-size: 1.4rem; color: #3b82f6; }
        header span { font-size: 0.85rem; color: #94a3b8; }
        .badge {
            background: #22c55e;
            color: #fff;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: bold;
        }
        .container { max-width: 1000px; margin: 40px auto; padding: 0 20px; }
        .hero {
            text-align: center;
            padding: 50px 20px;
            background: #1e293b;
            border-radius: 12px;
            margin-bottom: 30px;
            border: 1px solid #334155;
        }
        .hero h2 { font-size: 2rem; margin-bottom: 10px; }
        .hero p { color: #94a3b8; font-size: 1rem; margin-bottom: 20px; }
        .version-tag {
            display: inline-block;
            background: #1d4ed8;
            color: #fff;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 0.85rem;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .card {
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 24px;
        }
        .card h3 {
            font-size: 0.85rem;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 12px;
        }
        .card .value {
            font-size: 1.5rem;
            font-weight: bold;
            color: #3b82f6;
        }
        .card .sub { font-size: 0.8rem; color: #94a3b8; margin-top: 4px; }
        .stack {
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 30px;
        }
        .stack h3 {
            font-size: 0.85rem;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 16px;
        }
        .tags { display: flex; flex-wrap: wrap; gap: 10px; }
        .tag {
            padding: 6px 14px;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: 600;
        }
        .tag-blue { background: #1d4ed8; color: #bfdbfe; }
        .tag-green { background: #15803d; color: #bbf7d0; }
        .tag-purple { background: #6d28d9; color: #ddd6fe; }
        .tag-orange { background: #c2410c; color: #fed7aa; }
        .tag-teal { background: #0f766e; color: #99f6e4; }
        .endpoints {
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 24px;
        }
        .endpoints h3 {
            font-size: 0.85rem;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 16px;
        }
        .endpoint {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 10px 0;
            border-bottom: 1px solid #334155;
        }
        .endpoint:last-child { border-bottom: none; }
        .method {
            background: #15803d;
            color: #bbf7d0;
            padding: 3px 10px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: bold;
            min-width: 50px;
            text-align: center;
        }
        .path { font-family: monospace; color: #7dd3fc; font-size: 0.9rem; }
        .desc { color: #94a3b8; font-size: 0.8rem; margin-left: auto; }
        footer {
            text-align: center;
            padding: 30px;
            color: #475569;
            font-size: 0.8rem;
        }
    </style>
</head>
<body>
    <header>
        <h1>DevSecOps Platform</h1>
        <span>Arsel DIFFO SOUOP — SUPINFO Paris Master 2</span>
        <span class="badge">RUNNING</span>
    </header>

    <div class="container">
        <div class="hero">
            <h2>Plateforme DevSecOps</h2>
            <p>Infrastructure cloud automatisée — Azure Kubernetes Service</p>
            <span class="version-tag">Version {{ version }}</span>
        </div>

        <div class="grid">
            <div class="card">
                <h3>Statut</h3>
                <div class="value" style="color: #22c55e;">Healthy</div>
                <div class="sub">Tous les services opérationnels</div>
            </div>
            <div class="card">
                <h3>Environnement</h3>
                <div class="value">Kubernetes</div>
                <div class="sub">Azure AKS — South Africa North</div>
            </div>
            <div class="card">
                <h3>Uptime</h3>
                <div class="value">{{ uptime }}</div>
                <div class="sub">{{ date }}</div>
            </div>
            <div class="card">
                <h3>Replicas</h3>
                <div class="value">2 pods</div>
                <div class="sub">Haute disponibilité active</div>
            </div>
        </div>

        <div class="stack">
            <h3>Stack technique</h3>
            <div class="tags">
                <span class="tag tag-blue">Python Flask</span>
                <span class="tag tag-blue">Docker</span>
                <span class="tag tag-blue">Kubernetes (AKS)</span>
                <span class="tag tag-green">Terraform</span>
                <span class="tag tag-green">Ansible</span>
                <span class="tag tag-purple">GitHub Actions</span>
                <span class="tag tag-purple">Trivy (Security)</span>
                <span class="tag tag-orange">Azure ACR</span>
                <span class="tag tag-orange">Azure AKS</span>
                <span class="tag tag-teal">Prometheus</span>
                <span class="tag tag-teal">Grafana</span>
            </div>
        </div>

        <div class="endpoints">
            <h3>API Endpoints</h3>
            <div class="endpoint">
                <span class="method">GET</span>
                <span class="path">/</span>
                <span class="desc">Page d'accueil et statut</span>
            </div>
            <div class="endpoint">
                <span class="method">GET</span>
                <span class="path">/health</span>
                <span class="desc">Health check Kubernetes</span>
            </div>
            <div class="endpoint">
                <span class="method">GET</span>
                <span class="path">/info</span>
                <span class="desc">Informations du projet</span>
            </div>
            <div class="endpoint">
                <span class="method">GET</span>
                <span class="path">/api</span>
                <span class="desc">Réponse JSON pure</span>
            </div>
        </div>
    </div>

    <footer>
        Stayer Arsel DIFFO SOUOP — Master 2 Systèmes, Réseaux & Cloud — SUPINFO Paris 2026
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    now = datetime.datetime.now()
    return render_template_string(HTML_TEMPLATE,
        version=os.getenv("APP_VERSION", "1.0.0"),
        uptime="Active",
        date=now.strftime("%d/%m/%Y %H:%M")
    )

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/info')
def info():
    return jsonify({
        "project": "devsecops-arsel",
        "author": "Arsel DIFFO SOUOP",
        "school": "SUPINFO Paris",
        "stack": ["Python", "Flask", "Docker", "Kubernetes", "Azure", "Terraform", "Ansible"],
    })

@app.route('/api')
def api():
    return jsonify({
        "message": "DevSecOps Platform - Arsel DIFFO SOUOP",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "status": "running"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)