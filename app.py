# /usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-01 15:42:35
# @Author  : Jinyi Liu (jinyi.liu99@gmail.com)
# @Link    : http://home.ustc.edu.cn/~jm123456

from flask import Flask, g, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_login import LoginManager, current_user
from flask_bcrypt import Bcrypt

from config import Configuration


app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager(app)
login_manager.login_view = "login"

@app.before_request
def _before_request():
	g.user = current_user
def _last_page_visited():
	if "current_page" in session:
		session["last_page"] = session["current_page"]
	session["current_page"] = request.path