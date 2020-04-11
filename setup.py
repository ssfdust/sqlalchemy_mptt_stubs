from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sqlalchemy-mptt-stubs",
    url="https://github.com/ssfdust/sqlalchemy_mptt_stubs",
    author='Neng Ming',
    author_email='ssfdust@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.2",
    package_dir={'': 'package'},
    package_data={"sqlalchemy_mptt": ["__init__.pyi", "events.pyi", "mixins.pyi"]},
    packages=[
        "sqlalchemy_mptt"
    ]
)
