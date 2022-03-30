import pytest
from Matrix import Matrix

def test_correctShapeOfNull():
    matrix = Matrix([])
    assert matrix.shape == (0,0)

def test_correctShapeOfValid():
    matrix = Matrix([[1,2],[1,2],[1,2]])
    assert matrix.shape == (3,2)

def test_incorrectTypeOfInput():
    with pytest.raises(TypeError):
        matrix = Matrix([1,2,3])

def test_inconsistentShape():
    with pytest.raises(TypeError):
        matrix = Matrix([[1,2],[1]])

def test_correctMatrixArray():
    matrix = Matrix([[1,2],[1,2],[1,2]])
    assert matrix.array == [[1,2],[1,2],[1,2]]