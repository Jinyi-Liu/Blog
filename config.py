# /usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-01 15:40:47
# @Author  : Jinyi Liu (jinyi.liu99@gmail.com)
# @Link    : http://home.ustc.edu.cn/~jm123456
import os
class Configuration(object):
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/blog.db' % APPLICATION_DIR
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = '\x90r\x1a\xa2\x87\xd2&{\x13H'
    STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')
    IMAGES_DIR = os.path.join(STATIC_DIR, 'images')
