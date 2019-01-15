from flask import render_template, Flask, session

from .module.auth import auth_blueprint
from .module.settings import settings_blueprint


app = Flask(__name__)

@app.route("/")
def index():
        return render_template('index.html', title="Home", user=session)

app.register_blueprint(auth_blueprint)
app.register_blueprint(settings_blueprint)

