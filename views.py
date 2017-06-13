# /usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-01 15:43:48
# @Author  : Jinyi Liu (jinyi.liu99@gmail.com)
# @Link    : http://home.ustc.edu.cn/~jm123456

from app import app
from flask import render_template,request
@app.route('/')
def homepage():
    name = request.args.get('name')
    number = request.args.get('number')
    return render_template('homepage.html',name = name, number = number)