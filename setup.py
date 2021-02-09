# -*- coding: utf-8 -*-
# Copyright (C) 2020-2021 Greenbone Networks GmbH
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='pheme',
    version='21.4.dev2',
    description='report-generation-service',
    python_requires='==3.*,>=3.7.0',
    author='Greenbone Networks GmbH',
    author_email='info@greenbone.net',
    license='AGPL-3.0-or-later',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
    ],
    entry_points={
        "console_scripts": ["pheme-parameter = pheme.scripts.parameter:main"]
    },
    packages=[
        'pheme',
        'pheme.parser',
        'pheme.templatetags',
        'pheme.templatetags.charts',
        'pheme.transformation',
        'pheme.transformation.scanreport',
        'pheme.version',
    ],
    package_dir={"": "."},
    package_data={"pheme": ["*.sh"]},
    install_requires=[
        'coreapi==2.*,>=2.3.3',
        'django==2.2.2',
        'djangorestframework==3.9.0',
        'pyyaml==5.*,>=5.3.1',
        'rope<0.19,>=0.17',
        'uritemplate==3.*,>=3.0.1',
        'weasyprint<53,>=51',
        'xmltodict==0.*,>=0.12.0',
    ],
    extras_require={
        "dev": [
            "autohooks==2.*,>=2.2.0",
            "autohooks-plugin-black==1.*,>=1.2.0; python_version == \"3.*\" and python_version >= \"3.6.0\"",
            "autohooks-plugin-pylint==1.*,>=1.2.0",
            "black==20.8b1; python_version == \"3.*\" and python_version >= \"3.6.0\"",
            "pontos==0.*,>=0.3.0",
            "pylint==2.*,>=2.6.0",
            "pylint-django==2.*,>=2.3.0",
            "pytest==6.*,>=6.2.0",
            "pytest-cov==2.*,>=2.10.0",
            "pytest-django<5.0,>=3.9",
            "pytest-env==0.*,>=0.6.2",
        ]
    },
)
