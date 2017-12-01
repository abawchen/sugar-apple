from setuptools import setup

setup(
    name='sugar-apple',
    version='0.1',
    # packages=find_packages(),
    include_package_data=True,
    py_modules=['sugar-apple'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        sugar-apple = apple.main:cli
        apple = apple.main_cli:cli
    ''',
)