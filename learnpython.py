# Concept No. 1: FUNCTIONS 
print("print is a function, functions do things. You know something is a function typically when you see ()")

# Concept No. 2: VARIABLES
myVariable = "Variables are simply containers which hold values"

# Concept No. 3: LISTS
myList = ["Lists", "are", "like", "variables", "but","contain", "many", "values"]

# Concept No. 4 DATA TYPES
"I am a string, a basic data type (human readable text used in a computer programs)"
5000  # 5000 is a number, a basic data type"

# Concept No. 5 LOOPS
for x in range(13):
  print ("I am a loop, I do things over and over again...") # this particular loop is called a 'for-loop'

keepRunning = True
while keepRunning == True:
  print("I am a while-loop, I run while a certain condition is true")
  keepRunning = False

  # Concept No. 6 IF-STATEMENTS
  # If-Statements allow us to make decisions in our code. It is like a fork in the road.
  mood = "bored"
  if mood == "bored":    
    print("Your students are bored, please stop talking.")
  else:
    print("What an exciting lesson on Python!")

  # Concept No. 7 OBJECT-ORIENTED PROGRAMMING

#Classes are Blue-Prints for creating Objects
class Instructor:
  def __init__(self, name, age):
    self.name = name
    self.age = age
   
# Instantiate an Object: create an instance of the classs "Instruction"
chris = Instructor("Chris", 31)
print(chris.name)
print(chris.age)
