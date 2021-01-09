# listy_lo.py
"""
Module 5 Homework


In the second file, called listy_lo.py and do the following within the file:

Create a list named food with two elements 'rice' and 'beans'.
Append the string 'broccoli' to food using .append().
Add the strings 'bread' and 'pizza' to food using .extend().
Print the first two items in the food list using print() and slicing notation.
Print the last item in food using print() and index notation.
Create a list called breakfast from the string "eggs,fruit,orange juice" using the split() method.
Verify that breakfast has 3 elements using the len built-in.
prompts the user for a floating-point value until they enter stop. 
Store their entries in a list, and then find the average, min, and max of their entries and 
print them those values.
"""

if __name__ == "__main__":
    food = ['rice','beans']
    food.append('broccoli')
    food.extend(['bread','pizza'])
    print(f"{food[0:1]}")
    myfood = "eggs,fruit,orange juice"
    breakfast = myfood.split(",")
    if len(breakfast)==3:
        print("len(breakfast) is 3. Hooray!")
    else:
        print("Code not good.  Beware")

    numlist = []
    while True:
        number = input("Enter a floating point value or stop to stop: ")
        if number.lower() == "stop":
            if len(numlist) > 0:
                print(f"Average: {sum(numlist)/len(numlist)} Minimum: {min(numlist)}")
                print(f" Maximum: {max(numlist)}")
                break
            else:
                print("No floating point numbers enterred.")
                break
        else:
            numlist.append(float(number))
    print("That's all for listy_lo")



