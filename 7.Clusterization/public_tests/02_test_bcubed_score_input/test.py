import numpy as np
from solution import bcubed_score
import numpy as np
from itertools import product
from sklearn.metrics import silhouette_score as sklearn_silhouette_score
from solution import silhouette_score
import numpy as np
from solution import KMeansClassifier

def test(*args, **kwargs):

    def _check_bcubed_score_corner_test_02():
        true_labels, predicted_labels, answer = np.array([1, 2]), np.array([1, 1]), 2 / 3
        return np.allclose(bcubed_score(true_labels, predicted_labels), answer, atol=1e-10, rtol=0.0)
    
    return _check_bcubed_score_corner_test_02(*args, **kwargs)
