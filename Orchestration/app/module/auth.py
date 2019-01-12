from flask import session, render_template,Blueprint, request, redirect

auth_blueprint = Blueprint('auth_blueprint', __name__, template_folder='templates')


@auth_blueprint.route("/signIn")
def signIn():
    return render_template('auth/index.html', title="Home", user=session)


@auth_blueprint.route("/signOut")
def signOut():
    session.clear()
    return render_template('index.html', title="Home", user=session)


@auth_blueprint.route('/validateLogin', methods=['POST'])
def validateLogin():

    session.clear()

    _username = request.form['inputUserID']
    _password = request.form['inputPassword']

    session['pkID'] = "0000001"
    session['username'] = "Admin"
    session['email'] = "admin@admin.com"
    session['is_authenticated'] = "False"

    if _username == "admin" and _password == "admin":
        session['is_authenticated'] = "True"
        return redirect('/')
    else:
        session.pop('is_authenticated', False)
        return render_template('/auth/index.html', title="Sign In", authentication="False")
