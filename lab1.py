print("taking DNA sequence as user input:")
sequence = input("enter sequence please:")
list_for_compliment = []
#compliment
compliment = ""
for i in sequence:
    if i == "A":
        list_for_compliment.append("T")
    elif i == "T":
        list_for_compliment.append("A")
    elif i == "C":
        list_for_compliment.append("G")
    elif i == "G":
        list_for_compliment.append("C")
    else:
        list_for_compliment.append("N")
#for converting helping list into string again
comp = compliment.join(list_for_compliment)
print("compliment = ",comp)
#reverse compliment
print("reverse compliment")
rev = comp[::-1]
print(rev)

    
                 
