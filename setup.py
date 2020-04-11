from distutils.core import setup

setup(
    name="sqlalchemy-mptt stubs",
    url=None,
    author='Neng Ming',
    author_email='ssfdust@gmail.com',
    version="0.1",
    package_dir={'': 'package'},
    package_data={"sqlalchemy_mptt": ["__init__.pyi", "events.pyi", "mixins.pyi"]},
    packages=[
        "sqlalchemy_mptt"
    ]
)
