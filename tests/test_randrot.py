import numpy as np

import randrot


def test_orthogonality():

    def orthogonal(m):
        return np.allclose(m.T * m, np.eye(dim))

    for dim in [2, 3]:
        assert orthogonal(randrot.generate(dim))
