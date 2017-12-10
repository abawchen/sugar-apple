from setuptools import setup, find_packages

setup(
    name='sugar-apple',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['sugar-apple'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        sugar-apple = app.cli.main:cli
        apple = app.cli.main_cli:cli
    ''',
)