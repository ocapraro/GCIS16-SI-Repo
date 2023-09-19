"""
A test file for session4A.py
author: Oscar Capraro
seed:1
output:E, S, Z, Y
"""
import session4A
import random

def test_random_letter_lower():
  # Setup
  random.seed(1)
  capital = False
  expected = "e"

  # Invoke
  actual = session4A.random_letter(capital)

  # Analyze
  assert(expected == actual)