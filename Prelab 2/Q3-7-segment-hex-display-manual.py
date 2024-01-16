from sympy import symbols, Not, Or, And

n3, n2, n1, n0 = symbols('n3 n2 n1 n0')

CA_on = Or(
    And(Not(n3), Not(n2), Not(n1), Not(n0)),  # 0x0
    #And(Not(n3), Not(n2), Not(n1), n0),       # 0x1
    And(Not(n3), Not(n2), n1, Not(n0)),       # 0x2
    And(Not(n3), Not(n2), n1, n0),            # 0x3
    #And(Not(n3), n2, Not(n1), Not(n0)),       # 0x4
    And(Not(n3), n2, Not(n1), n0),            # 0x5
    And(Not(n3), n2, n1, Not(n0)),            # 0x6
    And(Not(n3), n2, n1, n0),                 # 0x7
    And(n3, Not(n2), Not(n1), Not(n0)),       # 0x8
    And(n3, Not(n2), Not(n1), n0),            # 0x9
    And(n3, Not(n2), n1, Not(n0)),            # 0xA
    #And(n3, Not(n2), n1, n0),                 # 0xB
    And(n3, n2, Not(n1), Not(n0)),            # 0xC
    #And(n3, n2, Not(n1), n0),                 # 0xD
    And(n3, n2, n1, Not(n0)),                 # 0xE
    And(n3, n2, n1, n0)                       # 0xF
)

print("CA on")
print('\n')
print("CA Unsimplified:", CA_on)
print('\n')
print("CA Simplified:", CA_on.simplify())
print("\n-----------------------------\n")

CB_on = Or(
  And(Not(n3), Not(n2), Not(n1), Not(n0)),  # 0x0
  And(Not(n3), Not(n2), Not(n1), n0),       # 0x1
  And(Not(n3), Not(n2), n1, Not(n0)),       # 0x2
  And(Not(n3), Not(n2), n1, n0),            # 0x3
  And(Not(n3), n2, Not(n1), Not(n0)),       # 0x4
  #And(Not(n3), n2, Not(n1), n0),            # 0x5
  #And(Not(n3), n2, n1, Not(n0)),            # 0x6
  And(Not(n3), n2, n1, n0),                 # 0x7
  And(n3, Not(n2), Not(n1), Not(n0)),       # 0x8
  And(n3, Not(n2), Not(n1), n0),            # 0x9
  And(n3, Not(n2), n1, Not(n0)),            # 0xA
  #And(n3, Not(n2), n1, n0),                 # 0xB
  #And(n3, n2, Not(n1), Not(n0)),            # 0xC
  And(n3, n2, Not(n1), n0),                 # 0xD
  #And(n3, n2, n1, Not(n0)),                 # 0xE
  #And(n3, n2, n1, n0)                       # 0xF
)

print("CB on")
print('\n')
print("CB Unsimplified:", CB_on)
print('\n')
print("CB Simplified:", CB_on.simplify())
print("\n-----------------------------\n")

CC_on = Or(
  And(Not(n3), Not(n2), Not(n1), Not(n0)),  # 0x0
  And(Not(n3), Not(n2), Not(n1), n0),       # 0x1
  #And(Not(n3), Not(n2), n1, Not(n0)),       # 0x2
  And(Not(n3), Not(n2), n1, n0),            # 0x3
  And(Not(n3), n2, Not(n1), Not(n0)),       # 0x4
  And(Not(n3), n2, Not(n1), n0),            # 0x5
  And(Not(n3), n2, n1, Not(n0)),            # 0x6
  And(Not(n3), n2, n1, n0),                 # 0x7
  And(n3, Not(n2), Not(n1), Not(n0)),       # 0x8
  And(n3, Not(n2), Not(n1), n0),            # 0x9
  And(n3, Not(n2), n1, Not(n0)),            # 0xA
  And(n3, Not(n2), n1, n0),                 # 0xB
  #And(n3, n2, Not(n1), Not(n0)),            # 0xC
  And(n3, n2, Not(n1), n0),                 # 0xD
  #And(n3, n2, n1, Not(n0)),                 # 0xE
  #And(n3, n2, n1, n0)                       # 0xF
)

print("CC on")
print('\n')
print("CC Unsimplified:", CC_on)
print('\n')
print("CC Simplified:", CC_on.simplify())
print("\n-----------------------------\n")

CD_on = Or(
  And(Not(n3), Not(n2), Not(n1), Not(n0)),  # 0x0
  #And(Not(n3), Not(n2), Not(n1), n0),       # 0x1
  And(Not(n3), Not(n2), n1, Not(n0)),       # 0x2
  And(Not(n3), Not(n2), n1, n0),            # 0x3
  #And(Not(n3), n2, Not(n1), Not(n0)),       # 0x4
  And(Not(n3), n2, Not(n1), n0),            # 0x5
  And(Not(n3), n2, n1, Not(n0)),            # 0x6
  #And(Not(n3), n2, n1, n0),                 # 0x7
  And(n3, Not(n2), Not(n1), Not(n0)),       # 0x8
  And(n3, Not(n2), Not(n1), n0),            # 0x9
  #And(n3, Not(n2), n1, Not(n0)),            # 0xA
  And(n3, Not(n2), n1, n0),                 # 0xB
  And(n3, n2, Not(n1), Not(n0)),            # 0xC
  And(n3, n2, Not(n1), n0),                 # 0xD
  And(n3, n2, n1, Not(n0)),                 # 0xE
  #And(n3, n2, n1, n0)                       # 0xF
)

print("CD on")
print('\n')
print("CD Unsimplified:", CD_on)
print('\n')
print("CD Simplified:", CD_on.simplify())
print("\n-----------------------------\n")

CE_on = Or(
  And(Not(n3), Not(n2), Not(n1), Not(n0)),  # 0x0
  #And(Not(n3), Not(n2), Not(n1), n0),       # 0x1
  And(Not(n3), Not(n2), n1, Not(n0)),       # 0x2
  #And(Not(n3), Not(n2), n1, n0),            # 0x3
  #And(Not(n3), n2, Not(n1), Not(n0)),       # 0x4
  #And(Not(n3), n2, Not(n1), n0),            # 0x5
  And(Not(n3), n2, n1, Not(n0)),            # 0x6
  #And(Not(n3), n2, n1, n0),                 # 0x7
  And(n3, Not(n2), Not(n1), Not(n0)),       # 0x8
  #And(n3, Not(n2), Not(n1), n0),            # 0x9
  And(n3, Not(n2), n1, Not(n0)),            # 0xA
  And(n3, Not(n2), n1, n0),                 # 0xB
  And(n3, n2, Not(n1), Not(n0)),            # 0xC
  And(n3, n2, Not(n1), n0),                 # 0xD
  And(n3, n2, n1, Not(n0)),                 # 0xE
  And(n3, n2, n1, n0)                       # 0xF
)

print("CE on")
print('\n')
print("CE Unsimplified:", CE_on)
print('\n')
print("CE Simplified:", CE_on.simplify())
print("\n-----------------------------\n")

CF_on = Or(
  And(Not(n3), Not(n2), Not(n1), Not(n0)),  # 0x0
  #And(Not(n3), Not(n2), Not(n1), n0),       # 0x1
  #And(Not(n3), Not(n2), n1, Not(n0)),       # 0x2
  #And(Not(n3), Not(n2), n1, n0),            # 0x3
  And(Not(n3), n2, Not(n1), Not(n0)),       # 0x4
  And(Not(n3), n2, Not(n1), n0),            # 0x5
  And(Not(n3), n2, n1, Not(n0)),            # 0x6
  #And(Not(n3), n2, n1, n0),                 # 0x7
  And(n3, Not(n2), Not(n1), Not(n0)),       # 0x8
  And(n3, Not(n2), Not(n1), n0),            # 0x9
  And(n3, Not(n2), n1, Not(n0)),            # 0xA
  And(n3, Not(n2), n1, n0),                 # 0xB
  And(n3, n2, Not(n1), Not(n0)),            # 0xC
  #And(n3, n2, Not(n1), n0),                 # 0xD
  And(n3, n2, n1, Not(n0)),                 # 0xE
  And(n3, n2, n1, n0)                       # 0xF
)

print("CF on")
print('\n')
print("CF Unsimplified:", CF_on)
print('\n')
print("CF Simplified:", CF_on.simplify())
print("\n-----------------------------\n")

CG_on = Or(
  #And(Not(n3), Not(n2), Not(n1), Not(n0)),  # 0x0
  #And(Not(n3), Not(n2), Not(n1), n0),       # 0x1
  And(Not(n3), Not(n2), n1, Not(n0)),       # 0x2
  And(Not(n3), Not(n2), n1, n0),            # 0x3
  And(Not(n3), n2, Not(n1), Not(n0)),       # 0x4
  And(Not(n3), n2, Not(n1), n0),            # 0x5
  And(Not(n3), n2, n1, Not(n0)),            # 0x6
  #And(Not(n3), n2, n1, n0),                 # 0x7
  And(n3, Not(n2), Not(n1), Not(n0)),       # 0x8
  And(n3, Not(n2), Not(n1), n0),            # 0x9
  And(n3, Not(n2), n1, Not(n0)),            # 0xA
  And(n3, Not(n2), n1, n0),                 # 0xB
  #And(n3, n2, Not(n1), Not(n0)),            # 0xC
  And(n3, n2, Not(n1), n0),                 # 0xD
  And(n3, n2, n1, Not(n0)),                 # 0xE
  And(n3, n2, n1, n0)                       # 0xF
)

print("CG on")
print('\n')
print("CG Unsimplified:", CG_on)
print('\n')
print("CG Simplified:", CG_on.simplify())
print("\n-----------------------------\n")