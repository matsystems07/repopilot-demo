**CmdCalc: A Simple Command Line Calculator**
=============================================

### Overview

CmdCalc is a simple command line calculator that supports basic arithmetic operations, trigonometric functions, exponential and logarithmic functions, and variables.

### Code

```python
# main.py

import math
import re

# Define a dictionary to store variables
variables = {}

def calculate(expression):
    """
    Evaluate a mathematical expression.

    Args:
        expression (str): The mathematical expression to evaluate.

    Returns:
        float: The result of the expression.
    """
    # Replace variables with their values
    for var, value in variables.items():
        expression = expression.replace(var, str(value))

    # Evaluate the expression
    try:
        result = eval(expression, {"math": math})
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    print("CmdCalc: A Simple Command Line Calculator")
    print("----------------------------------------")

    while True:
        # Get user input
        user_input = input(">>> ")

        # Check if the user wants to quit
        if user_input.lower() == "quit":
            break

        # Check if the user wants to assign a variable
        match = re.match(r"(\w+)\s*=\s*(.*)", user_input)
        if match:
            var_name = match.group(1)
            var_value = match.group(2)
            variables[var_name] = calculate(var_value)
            print(f"Variable {var_name} assigned value {variables[var_name]}")
            continue

        # Evaluate the expression
        result = calculate(user_input)
        if result is not None:
            print(f"Result: {result}")

if __name__ == "__main__":
    main()
```

### Usage

1. Run the script using Python: `python main.py`
2. Enter a mathematical expression, such as `2 + 2` or `math.sin(3.14)`
3. Use variables by assigning a value to a variable, such as `x = 5`
4. Use the variable in an expression, such as `x * 2`
5. Type `quit` to exit the calculator

### Example Use Cases

* Basic arithmetic: `2 + 2`, `5 * 3`, `10 / 2`
* Trigonometric functions: `math.sin(3.14)`, `math.cos(0)`, `math.tan(3.14)`
* Exponential and logarithmic functions: `math.exp(2)`, `math.log(10)`, `math.log10(100)`
* Variables: `x = 5`, `y = x * 2`, `x + y`

### Notes

* The `calculate` function uses the `eval` function to evaluate the expression. This can pose a security risk if used with untrusted input.
* The `variables` dictionary stores the values of assigned variables.
* The `main` function runs the command line interface and handles user input.