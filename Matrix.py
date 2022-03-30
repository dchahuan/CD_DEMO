class Matrix:
    def __init__(self, array):
        self.array = array
        if len(array) ==  0:
            self.shape = (0,0)
            return
        if any([not isinstance(x,list) for x in array]):
            raise TypeError('Row must be array')
        ## Check validity of array
        length_0 = len(array[0])
        if any([len(x) != length_0 for x in array]):
            raise TypeError('Rows must be equal size')
        self.shape = (len(array), length_0)

    @property
    def T(self):
        return Matrix([[self.array[j][i] for j in range(self.shape[0])] for i in range(self.shape[1])])
    
    def get_col_as_list(self, col):
        arr = []
        for i in range(self.shape[0]):
            arr.append(self.array[i][col])

        return arr
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Matrix([[other*self.array[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])
        elif isinstance(other, Matrix):

            assert self.shape[1] == other.shape[0], f"{self.shape[1]} must be equal to {other.shape[0]}"

            new_array = [[0 for _ in range(other.shape[1])] for _ in range(self.shape[0])]

            for row in range(self.shape[0]):
                for col in range(self.shape[1]):
                    new_array[row][col] = sum( x*y for x,y in zip(self.array[row], other.get_col_as_list(col)))
            return Matrix(new_array)
        else:
            raise TypeError('Other must be int, float or matrix')

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError('Matrix can only be subtructed by other matrix')
        assert self.shape == other.shape, "Shape between matrix must be the same"
        new_matrix = [[0 for _ in range(self.shape[1])] for _ in range(self.shape[0])]
        for row in range(self.shape[0]):
            for col in range(self.shape[1]):
                new_matrix[row][col] = self.array[row][col] + other.array[row][col]

        return Matrix(new_matrix)

        

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError('Matrix can only be subtructed by other matrix')
        assert self.shape == other.shape, "Shape between matrix must be the same"
        new_matrix = [[0 for _ in range(self.shape[1])] for _ in range(self.shape[0])]
        for row in range(self.shape[0]):
            for col in range(self.shape[1]):
                new_matrix[row][col] = self.array[row][col] - other.array[row][col]

        return Matrix(new_matrix)

    def __repr__(self) -> str:
        return repr(self.array)

    def __str__(self) -> str:
        return str(self.array)

    def __eq__(self, other) -> bool:
        return self.array == other.array

