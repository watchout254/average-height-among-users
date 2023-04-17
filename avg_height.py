print("\t\t\tWelcome to Urefu and ufupi sacco\n")
heights = input("All your heights(cm)separate using space: ")
list = heights.split()
count = 0
for urefu in list:
    count = count+1
print(count)
for i in range(count):
    list[i] = int(list[i])

total = 0
for i in list:
    total = total + i
print(f" Your total is: {total}")
average = total/count
print(f" Your average height is: {round(average)}")

