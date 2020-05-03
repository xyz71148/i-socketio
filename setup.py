"""
Flask-SocketIO
--------------

Socket.IO integration for Flask applications.
"""
import re
from setuptools import setup

with open('i_socketio/__init__.py', 'r') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        f.read(), re.MULTILINE).group(1)

setup(
    name='i_socketio',
    version=version,
    url='https://github.com/xyz71148/i-socketio.git',
    license='MIT',
    author='tommy',
    author_email='xyz71148@gmail.com',
    description='Socket.IO integration for Flask applications',
    long_description=__doc__,
    packages=['i_socketio'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.9',
        'flask_socketio',
        'python-socketio>=4.3.0',
        'flask-cors'
    ],
    tests_require=[
        'coverage'
    ],
    test_suite='test_socketio',
    entry_points={
        'console_scripts': [
            'i-sock=i_socketio.api:main'
        ],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
