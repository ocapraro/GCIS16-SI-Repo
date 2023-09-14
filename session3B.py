"""
A program for my week 3 SI session B.
author: Oscar Capraro
"""
import random

def student_sorter(s1, s2):
  if(s1<s2):
    return s1+" "+s2
  if(s2<s1):
    return s2+" "+s1

def letter_or_number(character):
  if(character<=chr(57)):
    return "Number"
  if(character>=chr(65)):
    return "Letter"

# def random_letter(capital):
#   if(capital):
#     return(chr(random.randint(65,90)))
#   return(chr(random.randint(97,122)))
  
def main():
  print(student_sorter("Bob", "Alice"))
  print(letter_or_number("c"))
  print(letter_or_number("3"))

if __name__ == "__main__":
  main()