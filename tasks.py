import os
import openai
from flask import Blueprint, request, redirect, render_template
from flask_jwt_extended import jwt_required
from users.models import db
from utils.mitre import get_heatmap
from reports.__init__ import save_report
import yaml

task_routes = Blueprint('task_routes', __name__)

# Load API key from config
cfg = yaml.safe_load(open("config/settings.yaml", 'r'))
openai.api_key = cfg["openai_api_key"]

@task_routes.route('/', methods=['GET', 'POST'])
@jwt_required()
def index():
    if request.method == 'POST':
        task = request.form['template']

        # Simulate detection logic
        detected = task.lower().startswith('run mimikatz')

        # Use OpenAI to generate explanation
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"Explain the cybersecurity implications of the following attack simulation: {task}",
                max_tokens=150,
                temperature=0.5
            )
            explanation = response.choices[0].text.strip()
        except Exception as e:
            explanation = f"(Error fetching explanation: {str(e)})"

        save_report(task, detected, explanation)
        return redirect('/report')

    templates = ["Run Mimikatz", "PsExec Lateral Movement", "Dump LSASS"]
    return render_template('index.html', templates=templates)
