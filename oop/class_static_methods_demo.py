class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


def main():
    print("Using static method:")
    result = Calculator.add(5, 3)
    print(f"Result: {result}")

    print("\nUsing class method:")
    result = Calculator.multiply(5, 3)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()