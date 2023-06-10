
<p align="center">
  <img src="https://github.com/vsg-root/RouteXplorer/assets/108541219/3434f78a-14b6-4a39-863a-54753be87522">
</p>

<br>
<br>

[![Python](https://img.shields.io/badge/Python-3.0%2B-blue.svg)](https://www.python.org/downloads/release/python-300/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Development Status](https://img.shields.io/badge/Development%20Status-Alpha-orange)](https://github.com/vsg-root/RouteXplorer)

RouteXplorer is a Python library developed to solve the Traveling Salesman Problem (TSP) in complete graphs. Its goal is to find the most efficient sequence of visiting nodes in a graph, minimizing the total distance traveled.
<br>

## Install

```python
$ pip install routexplore
```

#### Try your first RouteXplorer program
```python
$ python
```
```python
>>> from routexplore.utils.input_reader import InputReader
>>> from routexplore.algorithms.BruteForceSearch import BruteForceSearch

>>> grafo = InputReader.ler_arquivo(input("Insira o caminho do arquivo: ")) #./experiments/input.txt
>>> melhor_caminho, melhor_distancia = BruteForceSearch.encontrar_melhor_caminho(grafo)
>>> print(" ".join(melhor_caminho))
```

## Key Features

- Efficient Algorithms: RouteXplorer implements a variety of optimized algorithms to solve the Traveling Salesman Problem, allowing you to find solutions quickly and efficiently.

- Flexible Customization: The library offers flexible options to customize the algorithm settings, allowing you to adapt the optimization process to the specific needs of your project.

- Simple Integration: The library is easy to integrate into your existing Python projects, allowing you to leverage its powerful functionality without complications.

## Software Architecture
RouteXplorer's architecture follows an organized structure to facilitate extensibility, maintenance and code reuse. Here is an overview of the project's directory and file structure:

```python
├── experiments
│   ├── algorithms
│   │   ├── Algorithm.py
│   │   ├── BruteForceSearch.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── Algorithm.cpython-310.pyc
│   │       ├── BruteForceSearch.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   ├── execute.py
│   ├── __init__.py
│   ├── input.txt
│   └── utils
│       ├── Grafo.py
│       ├── __init__.py
│       ├── input_reader.py
│       ├── __pycache__
│       │   ├── Grafo.cpython-310.pyc
│       │   ├── __init__.cpython-310.pyc
│       │   ├── input_reader.cpython-310.pyc
│       │   └── Utils.cpython-310.pyc
│       └── Utils.py
├── LICENSE.md
├── README.md
├── requirements.txt
├── setup.py
├── src
│   └── routexplorer
│       └── __init__.py
└── tests
    └── __init__.py
```

- The experiments directory contains files related to running specific experiments or tests, such as different search algorithms.

- The experiments/algorithms directory houses the implementation of the algorithms to solve the Traveling Salesman Problem. Algorithm.py and BruteForceSearch.py are examples of available algorithms. The __init__.py file is required for the directory to be considered a Python package.
The experiments/execute.py directory contains a script file that is responsible for running the desired experiments or tests.

- The experiments/utils directory contains utility files such as Grafo.py, input_reader.py, and Utils.py that provide auxiliary functionality for experiments.

- The src directory contains the main source code for the RouteXplorer library. The src/routexplorer/__init__.py file is an initialization file required for the directory to be considered a Python package.

- The tests directory contains test files to ensure code quality and integrity.

In addition to the directory structure, the LICENSE.md file contains information about the project's use license, while requirements.txt lists the necessary dependencies to run RouteXplorer. setup.py is a setup file used to package and distribute the library.

## Contribution

RouteXplorer is an open source project and we encourage community contributions. If you want to contribute, please follow the guidelines outlined in the repository's CONTRIBUTING.md file.

## License

RouteXplorer is distributed under the MIT license. For more information, see the LICENSE.md file.

I hope this improved README.md provides a clearer view of the software architecture used in the RouteXplorer project!
