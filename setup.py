import os

from setuptools import find_packages, setup

os.system("pre-commit run")

setup(
    name="routexplorer",
    version="0.0.0",
    description="Biblioteca para Otimização de Rotas em Grafos Completos.",
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["routexplorer = routexplorer.__main__:main"]},
    install_requires=[
        # TODO Dependências do seu projeto
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)
