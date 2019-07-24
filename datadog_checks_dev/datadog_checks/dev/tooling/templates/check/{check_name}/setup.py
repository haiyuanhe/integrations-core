{license_header}from codecs import open  # To use a consistent encoding
from os import path

from setuptools import setup

HERE = path.dirname(path.abspath(__file__))

# Get version info
ABOUT = {{}}
with open(path.join(HERE, 'datadog_checks', '{check_name}', '__about__.py')) as f:
    exec(f.read(), ABOUT)

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


CHECKS_BASE_REQ = 'datadog-checks-base>=4.2.0'


setup(
    name='datadog-{check_name}',
    version=ABOUT['__version__'],
    description='The {check_name_cap} check',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='datadog agent {check_name} check',

    # The project's main homepage.
    url='https://github.com/DataDog/integrations-{repo_choice}',

    # Author details
    author='{author}',
    author_email='{email_packages}',

    # License
    license='BSD-3-Clause',

    # See https://pypi.org/classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Monitoring',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    # The package we're going to ship
    packages=['datadog_checks.{check_name}'],

    # Run-time dependencies
    install_requires=[CHECKS_BASE_REQ],

    # Extra files to ship with the wheel package
    include_package_data=True,
)
