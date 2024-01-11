from sympy import symbols, Not, Or, And

d2, d1, d0 = symbols('d2 d1 d0')

CA_on = Or(
    And(Not(d2), Not(d1), Not(d0)),  #000
    #And(Not(d2), Not(d1), d0),       #001
    And(Not(d2), d1, Not(d0)),       #010
    And(Not(d2), d1, d0),            #011
    #And(d2, Not(d1), Not(d0)),       #100
    And(d2, Not(d1), d0),            #101
    And(d2, d1, Not(d0)),            #110
    And(d2, d1, d0)                  #111
)

print("CA on")
print('\n')
print("CA Unsimplified:", CA_on)
print('\n')
print("CA Simplified:", CA_on.simplify())
print("\n-----------------------------\n")

CB_on = Or(
  And(Not(d2), Not(d1), Not(d0)),  #000
  And(Not(d2), Not(d1), d0),       #001
  And(Not(d2), d1, Not(d0)),       #010
  And(Not(d2), d1, d0),            #011
  And(d2, Not(d1), Not(d0)),       #100
  # And(d2, Not(d1), d0),            #101
  # And(d2, d1, Not(d0)),            #110
  And(d2, d1, d0)                  #111
)

print("CB on")
print('\n')
print("CB Unsimplified:", CB_on)
print('\n')
print("CB Simplified:", CB_on.simplify())
print("\n-----------------------------\n")

CC_on = Or(
  And(Not(d2), Not(d1), Not(d0)),  #000
  And(Not(d2), Not(d1), d0),       #001
  # And(Not(d2), d1, Not(d0)),       #010
  And(Not(d2), d1, d0),            #011
  And(d2, Not(d1), Not(d0)),       #100
  And(d2, Not(d1), d0),            #101
  And(d2, d1, Not(d0)),            #110
  And(d2, d1, d0)                  #111
)

print("CC on")
print('\n')
print("CC Unsimplified:", CC_on)
print('\n')
print("CC Simplified:", CC_on.simplify())
print("\n-----------------------------\n")

CD_on = Or(
  And(Not(d2), Not(d1), Not(d0)),  #000
  # And(Not(d2), Not(d1), d0),       #001
  And(Not(d2), d1, Not(d0)),       #010
  And(Not(d2), d1, d0),            #011
  # And(d2, Not(d1), Not(d0)),       #100
  And(d2, Not(d1), d0),            #101
  And(d2, d1, Not(d0)),            #110
  # And(d2, d1, d0)                  #111
)

print("CD on")
print('\n')
print("CD Unsimplified:", CD_on)
print('\n')
print("CD Simplified:", CD_on.simplify())
print("\n-----------------------------\n")

CE_on = Or(
  And(Not(d2), Not(d1), Not(d0)),  #000
  # And(Not(d2), Not(d1), d0),       #001
  And(Not(d2), d1, Not(d0)),       #010
  # And(Not(d2), d1, d0),            #011
  # And(d2, Not(d1), Not(d0)),       #100
  # And(d2, Not(d1), d0),            #101
  And(d2, d1, Not(d0)),            #110
  # And(d2, d1, d0)                  #111
)

print("CE on")
print('\n')
print("CE Unsimplified:", CE_on)
print('\n')
print("CE Simplified:", CE_on.simplify())
print("\n-----------------------------\n")

CF_on = Or(
  And(Not(d2), Not(d1), Not(d0)),  #000
  # And(Not(d2), Not(d1), d0),       #001
  # And(Not(d2), d1, Not(d0)),       #010
  # And(Not(d2), d1, d0),            #011
  And(d2, Not(d1), Not(d0)),       #100
  And(d2, Not(d1), d0),            #101
  And(d2, d1, Not(d0)),            #110
  # And(d2, d1, d0)                  #111
)

print("CF on")
print('\n')
print("CF Unsimplified:", CF_on)
print('\n')
print("CF Simplified:", CF_on.simplify())
print("\n-----------------------------\n")

CG_on = Or(
  # And(Not(d2), Not(d1), Not(d0)),  #000
  # And(Not(d2), Not(d1), d0),       #001
  And(Not(d2), d1, Not(d0)),       #010
  And(Not(d2), d1, d0),            #011
  And(d2, Not(d1), Not(d0)),       #100
  And(d2, Not(d1), d0),            #101
  And(d2, d1, Not(d0)),            #110
  # And(d2, d1, d0)                  #111
)

print("CG on")
print('\n')
print("CG Unsimplified:", CG_on)
print('\n')
print("CG Simplified:", CG_on.simplify())
print("\n-----------------------------\n")