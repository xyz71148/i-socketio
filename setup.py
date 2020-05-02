"""
Flask-SocketIO
--------------

Socket.IO integration for Flask applications.
"""
import re
from setuptools import setup

with open('i-socketio/__init__.py', 'r') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        f.read(), re.MULTILINE).group(1)

setup(
    name='i-socketio',
    version=version,
    url='https://github.com/xyz71148/i-socketio.git',
    license='MIT',
    author='tommy',
    author_email='xyz71148@gmail.com',
    description='Socket.IO integration for Flask applications',
    long_description=__doc__,
    packages=['i-socketio'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.9',
        'python-socketio>=4.3.0'
    ],
    tests_require=[
        'coverage'
    ],
    test_suite='test_socketio',
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
