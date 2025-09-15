import unicodedata
from a521 import add, subtract, multiply, divide, factorial, reverse_words

# --- add ---
assert add(2, 3) == 5
assert add(-1, 1) == 0

# --- subtract ---
assert subtract(10, 4) == 6

# --- multiply (should fail) ---
assert multiply(3, 4) == 12
assert multiply(0, 999) == 0
assert multiply(2.5, 2) == 5.0
assert multiply(1.5, 3.0) == 4.5

# --- divide ---
assert divide(8, 2) == 4
try:
    divide(1, 0)
    raise AssertionError("Expected ZeroDivisionError")
except ZeroDivisionError:
    pass

# --- factorial (should fail) ---
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
try:
    factorial(-3)
    raise AssertionError("Expected ValueError")
except ValueError:
    pass

# --- reverse_words ---
assert reverse_words("hello world") == "world hello"
assert reverse_words("  a   b  c ") == "  c   b  a "
out = reverse_words("café péru")
assert unicodedata.normalize("NFC", out) == "péru café"

print("All tests completed (some asserts should have failed above).")