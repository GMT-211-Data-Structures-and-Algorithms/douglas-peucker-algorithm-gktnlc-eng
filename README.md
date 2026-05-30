# GMT211 Douglas-Peucker Algorithm

A Python implementation of the Douglas-Peucker line simplification algorithm.

## Installation

```bash
pip install -i https://test.pypi.org/simple/ gmt211-2230674042
```

## Usage

### With a GeoJSON file

```python
from dp import *

input_file = 'antalya.geojson'
out_file = 'out.geojson'
epsilon = 0.01

execute_douglas_peucker(input_file, out_file, epsilon)
```

### With a text file

```python
from dp import *

input_line_file = 'line.txt'
epsilon = 6

input_line = convert_coordinates_to_line(input_line_file)
result_list = douglas_peucker(input_line, epsilon)
print(result_list)
```

## Epsilon Guide

| Epsilon | Approximate Tolerance |
|---------|----------------------|
| 0.001   | ~100 meters          |
| 0.005   | ~500 meters          |
| 0.01    | ~1 km                |
| 0.1     | ~10 km               |

## Running Tests

```bash
python -m unittest unit_test.py -v
```
## Documentation
https://douglas-peucker-algorithm-gktnlc-eng.readthedocs.io/en/latest/

## TestPyPI
https://test.pypi.org/project/gmt211-2230674042/