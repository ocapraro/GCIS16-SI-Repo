import random

def random_letter(capital):
  if(capital):
    return(chr(random.randint(65,90)))
  return(chr(random.randint(97,122)))

def random_word():
  return random_letter(True)+random_letter(False)+random_letter(False)+random_letter(False)

def main():
  print("Here's a random word:",random_word())

if __name__ == "__main__":
  main()