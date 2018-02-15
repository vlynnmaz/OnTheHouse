import flask; from flask import request, render_template

from . import common

site = common.site


@site.route('/user/<username>')
def get_user(username):
    user = common.rdb.get_user(id = None, username = username)
    print (user)
    recipes = common.rdb.search(author=user)
    response = render_template("profile.html", user=user, recipes=recipes)
    return response


@site.route('/user/<username>/profilepic')
@site.route('/user/<username>/profilepic.<ext>')
def get_profile_pic(username, ext=None):
    user = common.rdb.get_user(username=username)
    if user.profile_pic:
        return flask.send_file(user.profile_pic.file_path)
    else:
        path = common.STATIC_DIR.with_child('default_profile_pic.jpg').absolute_path
        return flask.send_file(path)

@site.route('/user')
def user():
    response = render_template("profile-test.html")
    return response
