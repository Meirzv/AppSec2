
from setuptools import setup, Command
import subprocess


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        errno = subprocess.call(['py.test'])
        raise SystemExit(errno)


setup(
    name='Flask-Split',
    version='0.4.0',
    url='http://github.com/meirzv/AppSec2',
    license='MIT',
    author='Janne Vanhala',
    author_email='janne.vanhala@gmail.com',
    description='A/B testing for your Flask application',
    long_description="Hi",
    packages=['app'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'FLASK>=1.1.0',
        'Redis>=2.6.0',
    ],
    cmdclass={'test': PyTest},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
