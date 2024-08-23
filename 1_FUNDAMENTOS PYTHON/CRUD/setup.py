from setuptools import setup

# Este Archivo nos sirve para poder instalar nuestra aplicación en el sistema o entorno virtual
setup(
    name='pv',
    version='0.1',
    py_modules=['pv'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pv=pv:cli
    ''',
)