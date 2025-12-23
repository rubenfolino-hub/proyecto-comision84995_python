

# setup.py
from setuptools import setup, find_packages

setup(
    name='mi-programa-clientes',  # Nombre que tendrá el paquete en PyPI/instalación
    version='0.1.0',             # Versión inicial
    author='Tu Nombre',
    author_email='tu.email@ejemplo.com',
    description='Modelamiento de Clientes para una página de compras usando POO.',
    packages=find_packages(where='src'),  # Busca todos los paquetes dentro de la carpeta 'src'
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)




