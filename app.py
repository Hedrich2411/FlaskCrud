from flask import Flask
from routes.employees import employees
from config import DATABASE_CONNECTION_URI
from pathlib import Path

root_dir = Path(__file__).parent
template_dir = root_dir / 'resources/templates'

app = Flask(__name__,template_folder=template_dir, 
                static_url_path='/static', static_folder='resources/static')

# settings
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.register_blueprint(employees)