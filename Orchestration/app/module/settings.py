from flask import session, render_template,Blueprint, request, redirect

import database

settings_blueprint = Blueprint('settings_blueprint', __name__, template_folder='templates')


@settings_blueprint.route("/showSettings")
def showSettings():

    element = "cms"

    entries = database.getEntries(element)
    nbr_entries = database.getNbrEntries(element)

    reach_min_entries = False;
    reach_max_entries = False;

    min_entries = 4
    max_entries = 5

    if (nbr_entries >= max_entries):
        reach_max_entries = True;

    if (nbr_entries >= min_entries):
        reach_min_entries = True;

    print entries

    return render_template('settings/index.html', title="UCS", entries=entries, reach_max_entries=reach_max_entries,
                           reach_min_entries=reach_min_entries, min_entries=min_entries)

