import numpy as np

class Matrix:
    def __init__(self, list_of_numbers) -> None:
        self.values = np.array(list_of_numbers)

    def determinant(self):
        return round(np.linalg.det(self.values),6)
    
    def multiply(self, b):
        return np.matmul(self.values, b.values)
    
    def add(self, b):
        return self.values + b.values
    
    def substract(self, b):
        return self.values - b.values
    

if __name__=="__main__":
    one = Matrix([[2, 3],[1, 4]])
    two = Matrix([[5, 7], [6, 8]])
    print(one.determinant())
    print(one.multiply(two))
    print(one.add(two))
    print(one.substract(two))