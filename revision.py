name = "Adam El Bajjaj"
#length
print(len(name))
#adam, 0 = pierwsza litera, 4 = ilosc znakow do wyprodukowania
print(name[0:4])
#prints last letters; -9 means that starts on 9th letter from the end. 14 is the amount of characters starting from the beggining
print(name[-9:14])

#split creates an array of each word that was in a string
uh = name.split()
print (str(uh))
usernm = uh[0]
print(usernm)
print(name.lower)

array = {"adam":"el bajjaj", "maria":"szczech-nuro", "justyna":"szczech", "mohammed":"el bajjaj"}
nm = input ("name: ")
sr = input ("surname: ")
#if nm is in array and if sr is in array AND it maches nm
if nm in array and sr in array[nm]:
    print("hi")
else:
    print("no")

#prewitten sentence with fill in the gaps
order = input("order: ")
age = input("age :")
#you can put numbers in pherimphesis to show which variable goes in which place
yes = "I am {0} years old and my order is: {1}."
print(yes.format(age, order))
