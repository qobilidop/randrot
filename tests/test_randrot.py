import numpy as np

import randrot


def test_orthogonality():
    for dim in [2, 3]:
        m = randrot.generate(dim)
        orthogonal = np.allclose(m.T * m, np.eye(dim))
        assert orthogonal is True
