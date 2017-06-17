# /usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-01 15:44:23
# @Author  : Jinyi Liu (jinyi.liu99@gmail.com)
# @Link    : http://home.ustc.edu.cn/~jm123456

from flask import request, session
from app import app,db
import views
import models
import admin

from entries.blueprint import entries
app.register_blueprint(entries, url_prefix='/entries')

if __name__ == '__main__':
	app.run()