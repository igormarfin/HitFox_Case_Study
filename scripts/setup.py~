#! /usr/bin/env python


from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.bdist_egg import bdist_egg as _bdist_egg


"""
taken from

http://www.niteoweb.com/blog/setuptools-run-custom-code-during-install
http://stackoverflow.com/questions/20194565/running-custom-setuptools-build-during-install
https://github.com/quasiyoke/keys_of_peace/blob/master/setup.py

"""

"""
class bdist_egg(_bdist_egg):
    def run(self):
        self.run_command('build_css')
        _bdist_egg.run(self)
"""

class CustomInstallCommand(install):
    """Customized setuptools install command - prints a friendly greeting."""
    sub_commands = install.sub_commands + [('test', None)]

    def run(self):
        print "Hello, developer, how are you? :)"
        install.run(self)


setup(
    name = "HitFox_Case_Study",
    version = "0.1",
    packages = find_packages(),
#    scripts = ['ProblemA.py'],

    entry_points = {
        'console_scripts': [
#            'ProblemA_python = ProblemA.ProblemA:main' # console app
            'ProblemA_python = ProblemA.ProblemA:mainTkinter',  # window app
            'ProblemB_python = ProblemB.ProblemB:mainTkinter'  # window app
        ]
    },

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ['docutils>=0.3',  'PIL>=1.1.7'
#    'os','sys', 
#    'optparse', 
#    'types',
#    'unittest',
#    'logging','inspect'
    ],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.rst'],
    },

    cmdclass={
         'install': CustomInstallCommand,
    },

# instead of

#    test_suite = 'ProblemB.suite',

# use
# python setup.py test --test-suite='ProblemB.suite'

    tests_require = 'docutils >= 0.3',


    # metadata for upload to PyPI
    author = "Igor Marfin",
    author_email = "me@example.com",
    description = "This is an Example Package",
    license = "GPL",
    keywords = "HitFox Case Study",
    url = "http://example.com/hitfox/",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)











