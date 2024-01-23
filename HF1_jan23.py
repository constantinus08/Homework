class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    @classmethod
    def input_fraction(cls):
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        return cls(numerator, denominator)

    def output_fraction(self):
        print(f"{self.numerator}/{self.denominator}")

    @classmethod
    def add(cls, fraction1, fraction2):
        result_numerator = fraction1.numerator * fraction2.denominator + fraction2.numerator * fraction1.denominator
        result_denominator = fraction1.denominator * fraction2.denominator
        return cls(result_numerator, result_denominator)

    @classmethod
    def subtract(cls, fraction1, fraction2):
        result_numerator = fraction1.numerator * fraction2.denominator - fraction2.numerator * fraction1.denominator
        result_denominator = fraction1.denominator * fraction2.denominator
        return cls(result_numerator, result_denominator)

    @classmethod
    def multiply(cls, fraction1, fraction2):
        result_numerator = fraction1.numerator * fraction2.numerator
        result_denominator = fraction1.denominator * fraction2.denominator
        return cls(result_numerator, result_denominator)

    @classmethod
    def divide(cls, fraction1, fraction2):
        result_numerator = fraction1.numerator * fraction2.denominator
        result_denominator = fraction1.denominator * fraction2.numerator
        return cls(result_numerator, result_denominator)

# Example usage
fraction1 = Fraction.input_fraction()
fraction2 = Fraction.input_fraction()

Fraction.output_fraction(fraction1)
Fraction.output_fraction(fraction2)

sum_fraction = Fraction.add(fraction1, fraction2)
difference_fraction = Fraction.subtract(fraction1, fraction2)
product_fraction = Fraction.multiply(fraction1, fraction2)
quotient_fraction = Fraction.divide(fraction1, fraction2)

print("Sum:")
sum_fraction.output_fraction()

print("Difference:")
difference_fraction.output_fraction()

print("Product:")
product_fraction.output_fraction()

print("Quotient:")
quotient_fraction.output_fraction()
