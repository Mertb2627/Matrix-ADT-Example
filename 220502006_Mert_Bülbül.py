class Array2D:
    def __init__(self, numRows, numCols):
        self.numRows = numRows
        self.numCols = numCols
        self.data = [[0] * numCols for _ in range(numRows)]

    def __getitem__(self, item):
        row , col = item
        return self.data[row][col]

    def __setitem__(self, key, value):
        row , col = key
        self.data[row][col] = value

class Matrix:
    def __init__(self, numRows, numCols):
        self.numRows = numRows
        self.numCols = numCols
        self.data = Array2D(numRows, numCols)

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    def scaleBy(self, item):
        for i in range(self.numRows):
            for a in range(self.numCols):
                self.data[i][a] *= item

    def transpoze(self):
        new = Matrix(self.numCols , self.numRows)
        new.data = Array2D(self.numCols , self.numRows)
        for i in range(self.numRows):
            for a in range(self.numCols):
                new.data[a,i] = self.data[i,a]
        return new

    def __add__(self, other):
        a = "Toplama işlemi için matrislerin boyutları aynı olmalıdır."
        assert self.numRows == other.numRows and self.numCols == other.numCols, print(a)
        sonuç = Matrix(self.numRows, self.numCols)
        sonuç.data = Array2D(self.numRows, self.numCols)
        for i in range(self.numRows):
            for a in range(self.numCols):
                sonuç.data[i, a] = self.data[i, a] + other.data[i, a]
        return sonuç

    def __sub__(self, other):
        a = "Çıkarma işlemi için matrislerin boyutları aynı olmalıdır."
        assert self.numRows == other.numRows and self.numCols == other.numCols, print(a)
        sonuç = Matrix(self.numRows, self.numCols)
        sonuç.data = Array2D(self.numRows, self.numCols)
        for i in range(self.numRows):
            for a in range(self.numCols):
                sonuç.data[i, a] = self.data[i, a] - other.data[i, a]
        return sonuç

    def __mul__(self, other):
        a = "Çarpma işlemi için birinci matristeki sütun sayısı, ikinci matristeki satır sayısına eşit olmalıdır. "
        assert self.numRows == other.numRows and self.numCols == other.numCols, print(a)
        sonuç = Matrix(self.numRows, self.numCols)
        sonuç.data = Array2D(self.numRows, self.numCols)
        for i in range(self.numRows):
            for a in range(self.numCols):
                sonuç.data[i, a] = sum(self.data[i, k] * other.data[k, a] for k in range(self.numCols))
        return sonuç