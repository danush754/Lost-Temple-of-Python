start = 1 
end = 100
for i in range(start,end+1):
    if(i%3 == 0 and i%5 != 0):
        print("fizz")
        continue
    elif(i%5 == 0 and i%3 != 0):
        print("buzz")
    elif(i%3 == 0 and i%5 == 0):
        print("fizzbuzz")
    else:
        print(i)