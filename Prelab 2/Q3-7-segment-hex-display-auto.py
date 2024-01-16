from sympy import symbols, Not, And, Or
from sympy.logic.boolalg import truth_table, simplify_logic
from itertools import product

# Redefining the symbols for a 4-bit vector
n3, n2, n1, n0 = symbols('n3 n2 n1 n0')

# Function to define the state of each segment for a given input (n3, n2, n1, n0) for hex digits
def hex_segment_state(n3, n2, n1, n0):
    # Defining each digit's segment pattern (0 to F)
    hex_patterns = {
        0: (1, 1, 1, 1, 1, 1, 0),  # 0
        1: (0, 1, 1, 0, 0, 0, 0),  # 1
        2: (1, 1, 0, 1, 1, 0, 1),  # 2
        3: (1, 1, 1, 1, 0, 0, 1),  # 3
        4: (0, 1, 1, 0, 0, 1, 1),  # 4
        5: (1, 0, 1, 1, 0, 1, 1),  # 5
        6: (1, 0, 1, 1, 1, 1, 1),  # 6
        7: (1, 1, 1, 0, 0, 0, 0),  # 7
        8: (1, 1, 1, 1, 1, 1, 1),  # 8
        9: (1, 1, 1, 1, 0, 1, 1),  # 9
        10: (1, 1, 1, 0, 1, 1, 1), # A
        11: (0, 0, 1, 1, 1, 1, 1), # b
        12: (1, 0, 0, 1, 1, 1, 0), # C
        13: (0, 1, 1, 1, 1, 0, 1), # d
        14: (1, 0, 0, 1, 1, 1, 1), # E
        15: (1, 0, 0, 0, 1, 1, 1), # F
    }
    # Convert the input bits to an integer
    num = n3 * 8 + n2 * 4 + n1 * 2 + n0
    return hex_patterns[num]

# Updated function to generate the truth table for each segment for hexadecimal digits
def generate_hex_truth_table():
    hex_truth_tables = []
    for seg in range(7):  # 7 segments (CA to CG)
        # Generating truth table for each segment
        table = [(inputs, hex_segment_state(*inputs)[seg]) for inputs in product([0, 1], repeat=4)]
        hex_truth_tables.append(table)
    return hex_truth_tables

# Updated function to derive boolean expression for each segment for hexadecimal digits
def derive_hex_boolean_expressions(hex_truth_tables):
    hex_expressions = []
    for seg, table in enumerate(hex_truth_tables):
        # Create an expression for when the segment is on
        expr = Or(*[And(*[var if val else Not(var) for var, val in zip([n3, n2, n1, n0], inputs)]) 
                   for inputs, output in table if output])
        hex_expressions.append(expr)
    return hex_expressions

# Generating the truth tables and the boolean expressions for hexadecimal digits
hex_truth_tables = generate_hex_truth_table()
hex_boolean_expressions = derive_hex_boolean_expressions(hex_truth_tables)

# Simplifying the boolean expressions for hexadecimal digits
hex_simplified_expressions = [simplify_logic(expr) for expr in hex_boolean_expressions]

# Function to print a full truth table including the digit and all segments for hexadecimal digits
def print_full_hex_truth_table(hex_truth_tables):
    segment_labels = ['CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'CG']
    print(f"{'n3':^3} {'n2':^3} {'n1':^3} {'n0':^3} {'Digit':^5}", end=" ")
    for seg in segment_labels:
        print(f"{seg:^3}", end=" ")
    print("\n" + "-" * 57)

    hex_digits = "0123456789ABCDEF"
    for i, inputs in enumerate(product([0, 1], repeat=4)):
        n3, n2, n1, n0 = inputs
        digit = hex_digits[n3 * 8 + n2 * 4 + n1 * 2 + n0]
        states = [table[i][1] for table in hex_truth_tables]
        print(f"{n3:^3} {n2:^3} {n1:^3} {n0:^3} {digit:^5}", end=" ")
        for state in states:
            print(f"{state:^3}", end=" ")
        print()

# Printing the full truth table for hexadecimal digits
print_full_hex_truth_table(hex_truth_tables)

def print_truth_table(hex_truth_tables):
  segment_labels = ['CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'CG']
  for seg, table in zip(segment_labels, hex_truth_tables):
      print(f"Segment {seg}:")
      print(f"{'n3':^3} {'n2':^3} {'n1':^3} {'n0':^3} | {'State':^5}")
      print("-" * 17)
      for inputs, output in table:
          n3, n2, n1, n0 = inputs
          print(f"{n3:^3} {n2:^3} {n1:^3} {n0:^3} | {output:^5}")
      print()

# Printing the truth table
print_truth_table(hex_truth_tables)

# Printing the simplified boolean expressions
print("Simplified Boolean Expressions for each segment:")
segment_labels = ['CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'CG']
for seg, expr in zip(segment_labels, hex_simplified_expressions):
    print(f"{seg}: {expr}")