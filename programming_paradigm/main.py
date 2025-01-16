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
        print(f"The result of the division is  {result} ")

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
if __name__ == "__main__":
    main()
