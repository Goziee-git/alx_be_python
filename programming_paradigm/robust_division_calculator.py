def safe_divide(numerator, denominator):
   try:
      num = float(numerator)
      den = float(denominator)

      result = num / den
      return result

   except ZeroDivisionError:
      return "Error: Cannot divide by zero." 

   except ValueError:
      return "Error: Please enter numeric values only." 

   except Exception as e: # Catch other unexpected errors
      return f"An unexpected error occurred: {e}"
