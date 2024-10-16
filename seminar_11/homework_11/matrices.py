"""1. СоздайтеклассMatrixдляработысматрицами.
Реализуйте методы:
○ сложения,
○ вычитания,
○ умножения,
○ транспонирования матрицы.
2. СоздайтенесколькоэкземпляровклассаMatrixипротестируйте
реализованные операции."""

class Matrix:
    def __init__(self, matrix: list[list]):
        self.matrix = matrix
        self.columns_num = len(self.matrix[0])
        self.rows_num = len(self.matrix)

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def transpose(self):
        new_matrix_rows_num = self.columns_num
        new_matrix = [[] for _ in range(new_matrix_rows_num)]

        for i in range(self.rows_num):
            for j in range(self.columns_num):
                new_matrix[j].append(self.matrix[i][j])

        return Matrix(new_matrix)

    def __add__(self, other):
        matrix_2_columns_num = len(other.matrix[0])
        matrix_2_rows_num = len(other.matrix)

        if not (self.columns_num == matrix_2_columns_num and self.rows_num == matrix_2_rows_num):
            raise ValueError("Error! Cannot add matrices of different dimensions.")

        new_matrix = [[] for _ in range(self.rows_num)]

        for i in range(self.rows_num):
            for j in range(self.columns_num):
                new_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])

        return Matrix(new_matrix)

    def __sub__(self, other):
        matrix_2_columns_num = len(other.matrix[0])
        matrix_2_rows_num = len(other.matrix)

        if not (self.columns_num == matrix_2_columns_num and self.rows_num == matrix_2_rows_num):
            raise ValueError("Error! Cannot subtract matrices of different dimensions.")

        new_matrix = [[] for _ in range(self.rows_num)]

        for i in range(self.rows_num):
            for j in range(self.columns_num):
                new_matrix[i].append(self.matrix[i][j] - other.matrix[i][j])

        return Matrix(new_matrix)

    def __mul__(self, other):
        matrix_2_columns_num = len(other.matrix[0])
        matrix_2_rows_num = len(other.matrix)

        if self.columns_num != other.rows_num:
            ValueError('Error! Matrices can be multiplied only if matrix 1 columns = matrix 2 rows!')

        result = [[0 for _ in range(matrix_2_columns_num)] for _ in range(matrix_2_rows_num)]

        # Perform matrix multiplication
        for i in range(self.rows_num):
            for j in range(matrix_2_columns_num):
                for k in range(self.columns_num):  # or range(rows_matrix2) as cols_matrix1 == rows_matrix2
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return result


if __name__ == '__main__':
    """Problem1 Practice Run:"""
    # matrix_1 = Matrix([[2,6],[3,7],[4,8],[5,9]])
    # matrix_2 = Matrix([[2,6],[3,7],[4,8],[5,9]])
    #
    # new_matrix_1 = matrix_1.transpose()
    # added_matrix = matrix_1 + matrix_2
    # subtracted_matrix = matrix_1 - matrix_2
    #
    # mul_matrix1 = Matrix([[3,4,2]])
    # mul_matrix2 = Matrix([[13,9,7,15],[8,7,4,6],[6,4,0,3]])
    # print(mul_matrix1 * mul_matrix2)
    # print(new_matrix_1.matrix)
    # print(added_matrix.matrix)
    # print(subtracted_matrix.matrix)

