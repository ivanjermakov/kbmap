import os
from setuptools import setup, find_packages, Command


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')


with open('README.md') as f:
    long_description = f.read()

setup(
    name='kbmap',
    version='1.1.0',
    packages=find_packages(),
    url='https://github.com/ivanjermakov/kbmap',
    license='MIT',
    author='Ivan Ermakov',
    author_email='ivanjermakov1@gmail.com',
    description='Linux keyboard mapping utility',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3',
    install_requires=['evdev', 'click'],
    scripts=['bin/kbmap'],
    cmdclass={
        'clean': CleanCommand
    }
)
