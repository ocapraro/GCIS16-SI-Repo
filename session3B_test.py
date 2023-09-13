"""
A test program for my week 3 SI session B.
author: Oscar Capraro
"""
import session3B

def test_student_sorter_s1_s2():
  # setup
  s1 = "Alice"
  s2 = "Bob"
  expected = "Alice Bob"

  # invoke
  actual = session3B.student_sorter(s1,s2)

  # analyze
  assert(expected == actual)