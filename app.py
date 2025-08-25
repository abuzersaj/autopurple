from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from users.models import db, User
from users.auth_jwt import auth_jwt, init_jwt
from utils.tasks import task_routes
from reports import report_routes
import yaml

# Load config
cfg = yaml.safe_load(open("config/settings.yaml", 'r'))

app = Flask(__name__)
app.config['SECRET_KEY'] = cfg["SECRET_KEY"]
app.config['JWT_SECRET_KEY'] = cfg["JWT_SECRET_KEY"]
app.config['SQLALCHEMY_DATABASE_URI'] = cfg["DATABASE_URI"]

db.init_app(app)
jwt = JWTManager(app)

admin = Admin(app, name='AutoPurple Admin', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))

app.register_blueprint(auth_jwt)
app.register_blueprint(task_routes)
app.register_blueprint(report_routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
