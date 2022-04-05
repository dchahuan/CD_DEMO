import pytest
from matrixCICD.Matrix import Matrix

def test_real_greater():

    assert Matrix([[1,1], [1,2]]) > Matrix([[0,0],[0,0]])
def test_fake_greater():
    
    assert not Matrix([[0,0], [0,0]]) > Matrix([[1,1],[1,1]]) 


def test_real_lesser():
    assert Matrix([[0,0], [0,0]]) < Matrix([[1,1],[1,1]])

def test_fake_lesser():
    assert not Matrix([[1,1], [1,2]]) < Matrix([[0,0],[0,0]])

def test_bad_shape_lesser():
    with pytest.raises(AssertionError):    
        assert Matrix([[1,1], [1,2]]) < Matrix([[0,0],[0,0],[1,2]])

