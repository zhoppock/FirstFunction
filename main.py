def first():
  print("winner! ")

def last():
    print("you lose :-( ")

first()
last()

def superAwesomeFunction(first, last):
  print("Hi", first, last + ", you are super and awesome!")

firstName = input("what is your first name? ")
lastName = input("What is your last name? ")
superAwesomeFunction(firstName, lastName)
fullName = (firstName + " " + lastName)
if fullName == "Zachary Hoppock":
  print("Good luck in class!")
elif fullName == "James Burk":
  print("Good luck with Math class!")
elif fullName == "Hingle McKringleberry":
  print("Showboating is a foul!")
else:
  print("That's all I have to say...")