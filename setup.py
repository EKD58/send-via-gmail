#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Sending mail via gmail.
setup
"""

from setuptools import setup

setup(
	name = "sendviagmail",
	version = "0.1",
	packages=["sendviagmail"],
	dependency_links = [],
	install_requires=[],
	extras_require={},
	package_data = {},
	author="EKD58",
	author_email = "LuckyIkedaY@gmail.com",
	description = "The familiar example program in Python",
	license = "BSD",
	keywords= "example documentation tutorial",
	url = "https://github.com/EKD58/send-via-gmail",
	entry_points = {
		"console_scripts": [
			"sendviagmail_in_python = sendviagmail.main:main",
		],
		"gui_scripts": []
	}
)
