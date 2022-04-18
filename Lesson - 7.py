#1 Матрица
class Matrix:

    def __init__(self, matrix_data):
        self.matrix = matrix_data

        qty_el = len(self.matrix)
        for stroka in self.matrix:
            self.matrix_size = tuple([(qty_el, len(stroka))])

        if len(self.matrix_size) != 1:
            raise ValueError("Неверный размер матрицы")

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, elem)) for elem in self.matrix])

    def __add__(self, o: "Matrix") -> "Matrix":
        if not isinstance(o, Matrix):
            raise TypeError(f"'{o.__class__.__name__}' "
                            f"Тип объекта не соответствует")
        if self.matrix_size != o.matrix_size:
            raise ValueError(f"Разные размеры матриц")

        result = []

        for item in zip(self.matrix, o.matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])

        return Matrix(result)


matrix1 = Matrix([[4, 4, 4, 4], [5, 5, 5, 5], [10, 10, 10, 10]])
print(matrix1, '\n')

matrix2 = Matrix([[10, 10, 10, 10], [10, 10, 10, 10], [100, 100, 100, 100]])
print(matrix2, '\n')

print(matrix1 + matrix2)

#2 Расчет сумарного расхода
class Cloth:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    @property
    def get_sq_full(self):
        return str(f'Площадь общая ткани: {(self.param_1 / 6.5 + 0.5) + (self.param_2 * 2 + 0.3)}')


class Coat(Cloth):
    def __init__(self, param_1, param_2):
        super().__init__(param_1, param_2)

    def square_c(self):
        return str(f'Плошадь ткани: {self.param_1 / 6.5 + 0.5}')

class Jacket(Cloth):
    def __init__(self, param_1, param_2):
        super().__init__(param_1, param_2)

    def square_j(self):
        return str(f'Плошадь ткани: {round(self.param_2 * 2 + 0.3)}')


coat = Coat(4, 5)
jacket = Jacket(2, 2)
print(coat.get_sq_full)
print(jacket.get_sq_full)
print(coat.square_c())
print(jacket.square_j())

# 3 Органические клетки

class Cell:
    def __init__(self, number_of_cells):
        self.number_of_cells = round(number_of_cells)

    def __add__(self, other):
        return Cell(self.number_of_cells + other.number_of_cells)

    def __sub__(self, other):
        if self.number_of_cells > other.number_of_cells:
            return Cell(self.number_of_cells - other.number_of_cells)
        elif self.number_of_cells - other.number_of_cells <= 0:
            return (f"Не выполнено условие задания")

    def __mul__(self, other):
        return Cell(self.number_of_cells * other.number_of_cells)

    def __truediv__(self, other):
        return Cell(self.number_of_cells // other.number_of_cells)

    def make_order(self, per_row: int):
        rows, tail = self.number_of_cells // per_row, self.number_of_cells % per_row
        return '\n'.join(['*' * per_row] * rows + (['*' * tail] if tail else []))

    def __str__(self) -> str:
        return f"Клетка состоит из {self.number_of_cells} ячеек"

c1 = Cell(20)
print(c1)
c2 = Cell(5)
print(c2)

print(c1 + c2)
print(c1 - c2)
print(c2 - c1)
print(c1 * c2)
print(c1 / c2)
print((c1 * c2).make_order(18))