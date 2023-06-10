
<p align="center">
  <img src="./assets/logo.png">
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

##### Try your first RouteXplorer program
```python
$ python
```
```python
>>> from routexplorer.utils.input_reader import InputReader
>>> from routexplorer.algorithms.BruteForceSearch import BruteForceSearch

>>> # Datas of graph
>>> graph = InputReader.read_file(input("Enter file path: ")) 

>>> # Calculation of the best path and distance
>>> best_path, best_distance = BruteForceSearch.find_best_path(graph, True, True)
```
```bash
file.txt

4 5
0 0 0 0 D
0 A 0 0 0
0 0 0 0 C
R 0 B 0 0
```
```python
$ Enter file path: file/path/file.txt
```
```
100% [■■■■■■■■■■] - Generating permutations
100% [■■■■■■■■■■] - Checking paths
Best path: ['A', 'D', 'C', 'B'] 
Shorter distance: (14)
```

## Key Features

- Efficient Algorithms: RouteXplorer implements a variety of optimized algorithms to solve the Traveling Salesman Problem, allowing you to find solutions quickly and efficiently.

- Flexible Customization: The library offers flexible options to customize the algorithm settings, allowing you to adapt the optimization process to the specific needs of your project.

- Simple Integration: The library is easy to integrate into your existing Python projects, allowing you to leverage its powerful functionality without complications.


## Contribution

RouteXplorer is an open source project and we encourage community contributions. If you want to contribute, please follow the guidelines outlined in the repository's CONTRIBUTING.md file.

## License

RouteXplorer is distributed under the MIT license. For more information, see the LICENSE.md file.
