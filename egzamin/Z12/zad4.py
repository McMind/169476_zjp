class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise NotImplementedError
        return ComplexNumber(self.real * other, self.imag * other)

    def __rmul__(self, other):
        if not isinstance(other, (int, float)):
            raise NotImplementedError
        return ComplexNumber(other * self.real, other * self.imag)

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            raise NotImplementedError
        if other == 0:
            raise ZeroDivisionError
        return ComplexNumber(self.real / other, self.imag / other)

    def __repr__(self):
        return f"ComplexNumber({self.real}, {self.imag})"


z = ComplexNumber(3,4)
print(z)
print(z * 2)
print(.5 * z)
print(z / 4)