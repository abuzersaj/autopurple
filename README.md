💥 AutoPurple — AI-Powered Purple Team Agent

Simulate attacks. Detect gaps. Get GPT-powered explanations — in seconds.  
Built by Abuzer Sajid 🧠💣

🧠 What Is AutoPurple?

AutoPurple is a next-gen Purple Teaming tool that lets you:

- Simulate cyberattacks (like Mimikatz, PsExec, etc.)  
- Detect them using Sigma rules + Sysmon/ELK  
- Map them to MITRE ATT&CK  
- Ask GPT-4/5 to explain what happened  
- Export HTML/PDF reports  
- View dashboards and trends over time  

No red team? No blue team? No problem.

 📚 Table of Contents

- What Is AutoPurple?  
- Interface Overview  
- Features  
- Tech Stack  
- Project Structure  
- Local Setup  
- MITRE ATT&CK Integration  
- Deploying  
- License  
- Author  
- Support & Collaboration  

 📸 Interface Overview

- 🔐 `/login` — Simple JWT login  
- 🧪 `/` — Select attack simulation (dropdowns)  
- 📊 `/report` — See result + explanation + MITRE mapping  
- 📈 `/dashboard` — Chart of detection history (success/fail)  


🚀 Features

- ✅ Simulate attacks using predefined templates  
- ✅ Collect and parse logs (Sysmon + ELK)  
- ✅ Match detections using Sigma rules  
- ✅ Map activity to MITRE ATT&CK  
- ✅ Explain results using OpenAI GPT  
- ✅ Export PDF or HTML report  
- ✅ View success/failure dashboard  


 🧰 Tech Stack

| Layer        | Tech                              |
|--------------|----------------------------------|
| Backend      | Flask (Python)                   |
| AI           | OpenAI GPT-4 / GPT-5             |
| Log Parsing  | Sysmon + ELK + Sigma rules       |
| UI           | HTML + Chart.js + Bootstrap      |
| Auth         | Flask-JWT-Extended               |
| Reports      | Jinja2 + WeasyPrint (PDF export) |
| DB (optional)| PostgreSQL / SQLite              |

---

 📁 Project Structure


autopurple/
├── app.py                  # Main entry point
├── auth\_jwt.py             # JWT Login/Auth logic
├── mitre.py                # Maps events to MITRE ATT\&CK
├── tasks.py                # Attack logic + detection logic
├── models.py               # DB models
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   └── report.html
├── config/
│   ├── settings.yaml       # Your real config (ignored)
│   └── settings.example.yaml  # Public-safe config




 🧪 Local Setup

 1. Clone the repo

`bash
git clone https://github.com/abuzersaj/autopurple.git
cd autopurple

 2. Setup virtual environment

`bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
 3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Add your config

Create a `settings.yaml` file inside `/config/`:

```yaml
openai_api_key: "your-openai-key-here"
SECRET_KEY: "your-secret-key"
JWT_SECRET_KEY: "your-jwt-secret"
DATABASE_URI: "sqlite:///autopurple.db"
```

Or copy example config and edit:

```bash
cp config/settings.example.yaml config/settings.yaml
```

# 5. Run the app

```bash
python app.py
```

Open your browser and visit:
`http://localhost:5000`

---

 📊 MITRE ATT\&CK Integration

Each simulation maps to MITRE tactics/techniques such as:

* 🛡️ T1003 – Credential Dumping
* 🔧 T1059 – Command and Scripting Interpreter
* 🌐 T1021 – Remote Services (PsExec)



 📦 Optional: Deploying

Deploy options include:

* 🟣 Render.com
* 🔵 Railway.app
* 🌍 Your own VPS / Cloud server

---

 🛡️ License

This project is licensed under the MIT License.



 🙋‍♂️ Author

Abuzer Sajid
🔗 [LinkedIn](https://www.linkedin.com/in/abuzer-sajidleer)
💼 Cybersecurity Analyst
📧 [abuzersajid@proton.me](mailto:abuzersajid@proton.me)



 🌟 Support & Collaboration

If you liked this project:

* ⭐ Star the repo
* 📬 Share with your team
* 🛠️ Fork and build your own modules
* 🐛 Report issues / suggest improvements

Let’s make Purple Teaming smarter. Together. 💣
