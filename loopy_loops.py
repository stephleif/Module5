# loopy_loops.py
"""
# HW 4 - Financial Functions

Create a tuple named pokemon that holds the strings 'picachu', 'charmander', and 'bulbasaur'.
Using index notation, print() the string that located at index 1 in pokemon
Unpack the values of pokemon into the following three new variables with names starter1, starter2, starter3.
Create a tuple using the tuple() built-in, that contains the letters of your name.
Check whether the character i is in your tuple representation of your name.
Write a for loop that prints out the integers 2 through 10, each on a new line, by using the range() function.
Use a while loop that prints out the integers 2 through 10.
Write a for loop that iterates over the string 'This is a simple string' and prints each character.
Using a nested for loop, iterate over the following set ('this', 'is', 'a', 'simple', 'set') and 
print each word, three times.

"""
if __name__ == "__main__":
    pokemon = ('picachu', 'charmander', 'bulbasaur' )
    print(f"{pokemon[1]}")
    starter1 = pokemon[0]
    starter2 = pokemon[1]
    starter3 = pokemon[2]
    myName = input("Please enter your name: ")
    myNameTuple = tuple(myName)
    if 'i' in myNameTuple:
        print("{myName} has an i")
    else:
        print("No i in {myName}")
    for index in range(2,10,1):
        print(f"{index}")
    index = 1
    while index <= 10:
        print(f"{index}")
        index +=1
    for sindex in "This is a simple string":
        print(f"{sindex}")
    myset = {'this', 'is', 'a', 'simple', 'set'}
    for ssindex in myset:
        for index in range(3):
            print(f"{ssindex}")
    print("That's all folks")

    