# Global and Local Variable:-

# ============================================================
# SCOPE = the region of code where a variable can be accessed.
# Python has: Global scope, Local scope (and NO block scope).
# ============================================================


# ------------------------------------------------------------
# 1. GLOBAL SCOPE
# ------------------------------------------------------------
# - Variable created OUTSIDE any function -> global scope.
# - Lives for the whole program, accessible EVERYWHERE in the
#   file (inside and outside all functions).
# - Any function can READ it directly without any keyword.
#
# Example:
#   health = 100          # global variable
#   def show():
#       print(health)     # reading global works -> 100
#   def heal():
#       print(health + 20)  # readable in every function -> 120
#   show()
#   print(health)         # 100 (accessible outside too)


# ------------------------------------------------------------
# 2. LOCAL SCOPE
# ------------------------------------------------------------
# Variable created INSIDE a function -> exists only inside it.
#
# Example:
#   def attack():
#       damage = 15       # local
#       print(damage)     # 15
#   attack()
#   print(damage)         # NameError! not defined outside


# ------------------------------------------------------------
# 3. HOW TO MODIFY A GLOBAL VARIABLE
# ------------------------------------------------------------
# Assigning inside a function creates a NEW local variable,
# it does NOT touch the global one.
#
# Example (the trap):
#   score = 0
#   def wrong():
#       score = 10        # new LOCAL variable!
#   wrong()
#   print(score)          # 0 -> global unchanged
#
# Way 1: 'global' keyword -> declares you mean the global one.
#   score = 0
#   def right():
#       global score      # must be written BEFORE using it
#       score += 10       # now modifies the real global
#   right()
#   print(score)          # 10 -> modified!
#
# Way 2 (BETTER): pass in + return the new value.
#   def add(score):
#       return score + 10
#   score = add(score)    # score is now 20
#
# Note: mutable globals (list/dict) can be CHANGED without
# 'global', because we modify the object, not reassign it:
#   items = []
#   def add_item():
#       items.append("sword")   # works, no 'global' needed


# ------------------------------------------------------------
# 4. BLOCK SCOPE (Python does NOT have it!)
# ------------------------------------------------------------
# In languages like C/Java, variables inside if/for/while die
# with the block. In Python they LIVE ON in the enclosing scope.
#
# Example:
#   if True:
#       x = 5
#   print(x)              # 5 -> works fine in Python!
#
#   for i in range(3):
#       pass
#   print(i)              # 2 -> loop variable still exists!


# ------------------------------------------------------------
# 5. PYTHON CONSTANTS
# ------------------------------------------------------------
# - A constant = a value that should NEVER change.
# - Python has NO true constants! ALL_CAPS naming is just a
#   convention that tells programmers "do not modify this".
# - Define them at the top of the file, in global scope.
# - Safe to use globally because we only READ them.
#
# Example:
#   PI = 3.14159          # constant (by convention)
#   MAX_PLAYERS = 4
#   URL = "https://example.com"
#
#   def area(r):
#       return PI * r ** 2   # reading a constant is fine
#
#   PI = 5                # Python won't stop you... but DON'T!


# ------------------------------------------------------------
# KEY POINTS
# ------------------------------------------------------------
# 1. Global -> outside functions, accessible everywhere.
# 2. Local  -> inside a function, dies when function ends.
# 3. Assignment inside a function makes a LOCAL variable.
# 4. Modify a global: 'global' keyword, or better -> return values.
# 5. Mutable globals (list/dict) can be changed without 'global'.
# 6. NO block scope: if/for/while don't create a new scope.
# 7. Constants: ALL_CAPS convention only, Python can't enforce them.
