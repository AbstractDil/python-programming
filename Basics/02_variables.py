# Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). # Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.


# name and are are two variables

name = "Sagar"  # string
age = 24        # integer

print("My name is ", name)
print("My age is ", age)

# here we check the type of the variable

print(type(name))
print(type(age))

#  If you want to specify the data type of a variable, this can be done with casting.

x = str("Hi")
y = int(5)
print(x, y) # hi 5 in the output

# Case sensitive
# If we create two variables "Price" and  "price", then both are different

Price  = 35.87
price = 899

print("Price is:", Price)
print("price is:", price)


# some other examples

var1 = "India" # this is a valid variable name but if write 1var then it will throw an error



# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

