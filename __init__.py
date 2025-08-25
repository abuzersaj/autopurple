from flask import Blueprint, render_template
from utils.mitre import get_heatmap
import os

report_routes = Blueprint('report_routes', __name__)

@report_routes.route('/report')
def report():
    files = os.listdir("reports/storage") if os.path.exists("reports/storage") else []
    latest = sorted(files)[-1] if files else None
    content = ""
    if latest:
        content = open(os.path.join("reports/storage", latest)).read()
    heatmap = get_heatmap()
    return render_template('report.html', html=content, heatmap=heatmap)

@report_routes.route('/dashboard')
def dashboard():
    files = os.listdir("reports/storage") if os.path.exists("reports/storage") else []
    labels, data, colors = [], [], []
    for f in files:
        content = open(os.path.join("reports/storage", f)).read()
        labels.append(f.replace(".html", ""))
        detected = "Detected: True" in content
        data.append(1 if detected else 0)
        colors.append("'rgba(75, 192, 192, 0.6)'" if detected else "'rgba(255, 99, 132, 0.6)'")
    return render_template("dashboard.html", labels=labels, data=data, colors=colors)

def save_report(task, detected, explanation):
    os.makedirs("reports/storage", exist_ok=True)
    filename = f"{task.replace(' ', '_')}.html"
    html = f"<h2>{task}</h2><p>Detected: {detected}</p><p>{explanation}</p>"
    with open(f"reports/storage/{filename}", "w") as f:
        f.write(html)
