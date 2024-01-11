from sympy import symbols, Not, And, Or
from sympy.logic.boolalg import truth_table, simplify_logic
from itertools import product

# Defining the symbols
d2, d1, d0 = symbols('d2 d1 d0')

# Function to define the state of each segment for a given input (d2, d1, d0)
def segment_state(d2, d1, d0):
    # Defining each digit's segment pattern (0 to 7)
    patterns = {
        0: (1, 1, 1, 1, 1, 1, 0),  # 0
        1: (0, 1, 1, 0, 0, 0, 0),  # 1
        2: (1, 1, 0, 1, 1, 0, 1),  # 2
        3: (1, 1, 1, 1, 0, 0, 1),  # 3
        4: (0, 1, 1, 0, 0, 1, 1),  # 4
        5: (1, 0, 1, 1, 0, 1, 1),  # 5
        6: (1, 0, 1, 1, 1, 1, 1),  # 6
        7: (1, 1, 1, 0, 0, 0, 0),  # 7
    }
    # Convert the input bits to an integer
    num = d2 * 4 + d1 * 2 + d0
    return patterns[num]

# Function to generate the truth table for each segment
def generate_truth_table():
    truth_tables = []
    for seg in range(7):  # 7 segments (CA to CG)
        # Generating truth table for each segment
        table = [(inputs, segment_state(*inputs)[seg]) for inputs in product([0, 1], repeat=3)]
        truth_tables.append(table)
    return truth_tables

# Function to derive boolean expression for each segment
def derive_boolean_expressions(truth_tables):
    expressions = []
    for seg, table in enumerate(truth_tables):
        # Create an expression for when the segment is on
        expr = Or(*[And(*[var if val else Not(var) for var, val in zip([d2, d1, d0], inputs)]) 
                   for inputs, output in table if output])
        expressions.append(expr)
    return expressions

# Generating the truth tables and the boolean expressions
truth_tables = generate_truth_table()
boolean_expressions = derive_boolean_expressions(truth_tables)


# Function to print a full truth table including the digit and all segments
def print_full_truth_table(truth_tables):
    segment_labels = ['CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'CG']
    print(f"{'d2':^3} {'d1':^3} {'d0':^3} {'Digit':^5}", end=" ")
    for seg in segment_labels:
        print(f"{seg:^3}", end=" ")
    print("\n" + "-" * 43)

    for i, inputs in enumerate(product([0, 1], repeat=3)):
        d2, d1, d0 = inputs
        digit = d2 * 4 + d1 * 2 + d0
        states = [table[i][1] for table in truth_tables]
        print(f"{d2:^3} {d1:^3} {d0:^3} {digit:^5}", end=" ")
        for state in states:
            print(f"{state:^3}", end=" ")
        print()

# Printing the full truth table
print_full_truth_table(truth_tables)

# Simplifying the boolean expressions
simplified_expressions = [simplify_logic(expr) for expr in boolean_expressions]

# Function to print the truth table in a readable format
def print_truth_table(truth_tables):
    segment_labels = ['CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'CG']
    for seg, table in zip(segment_labels, truth_tables):
        print(f"Segment {seg}:")
        print(f"{'d2':^3} {'d1':^3} {'d0':^3} | {'State':^5}")
        print("-" * 17)
        for inputs, output in table:
            d2, d1, d0 = inputs
            print(f"{d2:^3} {d1:^3} {d0:^3} | {output:^5}")
        print()

# Printing the truth table
print_truth_table(truth_tables)

# Printing the simplified boolean expressions
print("Simplified Boolean Expressions for each segment:")
segment_labels = ['CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'CG']
for seg, expr in zip(segment_labels, simplified_expressions):
    print(f"{seg}: {expr}")