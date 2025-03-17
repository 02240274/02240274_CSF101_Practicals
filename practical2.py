nameOfAnimals = ["cats","dogs","monkeys","gorilla"] # Creating a list of animal names
nameOfAnimals.append("chimpanzee")  # Adding a new animal name to the list
print(nameOfAnimals) # Printing the updated list

arrayLength = len(nameOfAnimals) # Getting the length of the list
print(arrayLength)

# Using a for loop to iterate over the list and print each element
for index in range(arrayLength):   # Loop runs from index 0 to arrayLength - 1
    print(nameOfAnimals[index])   # Accessing and printing each animal name by index 
    
