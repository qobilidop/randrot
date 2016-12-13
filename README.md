# randrot

[![Build Status](https://travis-ci.org/qobilidop/randrot.svg?branch=master)](https://travis-ci.org/qobilidop/randrot)

Python random rotation matrix generators (currently in 2D and 3D).

Generate uniformly distributed random rotation matrices in 2D and 3D. The 2D case is trivial. The 3D case is based on an algorithm described in [Arvo 1992](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.53.1357).

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

## Roadmap

- Generate [uniform random rotation matrices](https://en.wikipedia.org/wiki/Rotation_matrix#Uniform_random_rotation_matrices) in any dimension.

## See also

This project does solve the problem it aims to solve. But it's rather simple and featureless. Actually I also use this project to learn to make a Python package. There are more mature Python packages which provide the same functionalities:

- [pyquaternion](http://kieranwynn.github.io/pyquaternion/) is a full-featured Python module for representing and using quaternions. It has the functionalities to [create random quaternion](http://kieranwynn.github.io/pyquaternion/#random), [access matrix form](http://kieranwynn.github.io/pyquaternion/#accessing-matrix-form) and much more.
