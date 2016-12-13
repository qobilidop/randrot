import numpy as np
import pytest

import randrot


valid_dims = [2, 3]
invalid_dims = [1, 4]


def test_dimension():
    for dim in invalid_dims:
        with pytest.raises(ValueError):
            randrot.generate(dim)


def test_orthogonality():
    def orthogonal(m):
        return np.allclose(m.T * m, np.eye(*m.shape))
    for dim in valid_dims:
        assert orthogonal(randrot.generate(dim))
