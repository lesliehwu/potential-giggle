#find and replace
words = "It's thanksgiving day. It's my birthday,too!"
print("\nFIND AND REPLACE")
print(words.find("day"))
print(words.replace("day","month"))

#min and max
x = [2,54,-2,7,12,98]
print("\nMIN AND MAX")
print(min(x))
print(max(x))

#first and last
y = ["hello",2,54,-2,7,12,98,"world"]
print("\nFIRST AND LAST")
print(y[0])
print(y[len(y)-1])
new_y = []
new_y.append(y[0])
new_y.append(y[len(y)-1])
print(new_y)


#new list
z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
half = int(len(z)/2)
index_zero = z[:half]
new_z = []
new_z.append(index_zero)
print("\nNEW LIST")
new_z += z[half:]
print(new_z)
