# /usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-16 14:38:15
# @Author  : Jinyi Liu (jinyi.liu99@gmail.com)
# @Link    : http://home.ustc.edu.cn/~jm123456

import wtforms
from wtforms import validators
from models import User

class LoginForm(wtforms.Form):
	email = wtforms.StringField("Email",
		validators=[validators.DataRequired(),validators.Email()])
	password = wtforms.PasswordField("Password",
		validators=[validators.DataRequired()])
	remember_me = wtforms.BooleanField("Remember me?",
		default=True)

	def validate(self):
		if not super(LoginForm, self).validate():
			return False

		self.user = User.authenticate(self.email.data, self.password.data)
		if not self.user:
			self.email.errors.append("Invalid email or password.")
			return False
		return True
