import pytest
from Matrix import Matrix


def test_multIdentity():
    matrix_identity = Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    matrix_2 = Matrix([[3,6,7,8],[9,1,2,0],[5,2,1,0],[2,2,1,1]])

    new_matrix = matrix_identity*matrix_2

    assert new_matrix.array == matrix_2.array

def test_multRegular():

    matrix_identity = Matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    matrix_2 = Matrix([[3,6,7,8],[9,1,2,0],[5,2,1,0],[2,2,1,1]])

    new_matrix = matrix_identity*matrix_2

    assert new_matrix.array == [[44, 22,18,12],[120, 66, 62, 48], [196,110,106,84],[272,154,150,120]]


def test_multInt():

    matrix = Matrix([[3,6,7,8],[9,1,2,0],[5,2,1,0],[2,2,1,1]])

    new_matrix = matrix * 2

    assert new_matrix.array == [[6,12,14,16],[18,2,4,0],[10,4,2,0],[4,4,2,2]]


def test_invalidDimMult():
    with pytest.raises(AssertionError):
        matrix_identity = Matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
        matrix_2 = Matrix([[3,6,7,8],[9,1,2,0],[5,2,1,0],[2,2,1,1], [1,2,3,4]])

        new_matrix = matrix_identity*matrix_2

def test_invalidDataType():
    with pytest.raises(TypeError):
        matrix_2 = Matrix([[3,6,7,8],[9,1,2,0],[5,2,1,0],[2,2,1,1], [1,2,3,4]])

        new_matrix = matrix_2 * "a"
