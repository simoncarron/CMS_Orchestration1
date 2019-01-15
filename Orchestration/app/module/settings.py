from flask import session, render_template,Blueprint, request, redirect

settings_blueprint = Blueprint('settings_blueprint', __name__, template_folder='templates')


@settings_blueprint.route("/settings")
def signIn():
    return render_template('settings/index.html', title="Home", user=session)

