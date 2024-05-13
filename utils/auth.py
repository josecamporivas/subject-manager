import flask_login


def get_current_user():
    usr = flask_login.current_user

    if usr.is_anonymous:
        flask_login.logout_user()
        usr = None

    return usr
