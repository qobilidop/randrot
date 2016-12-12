# randrot

This Python package provides 2D and 3D random rotation matrix generators. The 2D case is trivial. The 3D case is based on [Arvo 1992](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.53.1357).

## Installation

```bash
pip install git+https://github.com/qobilidop/randrot.git#egg=randrot
```

## Usage

```python
>>> import numpy as np
>>> import randrot
>>> np.random.seed(0)
>>> randrot.generate(2)
matrix([[-0.95333378,  0.30191837],
        [-0.30191837, -0.95333378]])
>>> np.random.seed(0)
>>> randrot.generate(3)
matrix([[ 0.97631838,  0.04135264, -0.21234968],
        [-0.19851343, -0.21892019, -0.95533574],
        [-0.08599329,  0.9748661 , -0.20552675]])
```
