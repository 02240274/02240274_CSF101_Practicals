generated_number = [0,1,2,3,4,5,6,7,8,9]
newstack = []
index = 9

while index > -1:
    newstack.append(generated_number[index])
    index = index - 1

    print(newstack)  
