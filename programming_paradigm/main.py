import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)
    try:
        numerator = float(sys.argv[1])
        denominator = float(sys.argv[2])
        result = safe_divide(numerator, denominator)
<<<<<<< HEAD
        print(f"The result of the division is {result}")

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)

        
=======
        print(f"The result of the division is  {result} ")

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
>>>>>>> 575e21b1a5a9eb383caa1afc5fc7392eb2a54734
if __name__ == "__main__":
    main()
