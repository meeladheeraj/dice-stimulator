import random  
print("This is a dice stimulator")
x = "y"

while x == "y":
    n = random.randint(0,5)

    number =["""
      ----------
      |        |
      |    O   |
      |        |
      ----------
      ""","""
        ----------
        |        |
        | O    O |
        |        |
        ----------
        """ ,"""
        ----------
        |    O   |
        |    O   |
        |    O   |
        ----------
        ""","""
        ----------
        | O    O |
        |        |
        | O    O |
        ----------
        ""","""
        ----------
        | O    O |
        |    O   |
        | O    O |
        ----------
        ""","""
        ----------
        | O    O |
        | O    O |
        | O    O |
        ----------
        """]
    print(number[n])
    x = input("Press y to roll again")
    
