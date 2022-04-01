from ...matrix.Matrix import Matrix

def test_checkTranspose():
    matrix = Matrix([[1,2,3],[4,5,6]])

    assert matrix.T == Matrix([[1,4],[2,5],[3,6]])