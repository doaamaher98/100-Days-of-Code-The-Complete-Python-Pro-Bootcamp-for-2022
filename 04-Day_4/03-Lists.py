'''
Python Lists :-
    its a data structure type
    fruits = [item1, item2], where it can store many data types together in 1 list
'''

states = ["Cairo","Alex","Aswan","Port Said"]

print(states[0])
print(states[-1])

''' Lists can be editted ;) '''
states[2] = "Oksor"
print(states[2])

''' Append("") function is used to increase an element at the end of the list '''
states.append("Asyut")

print(states)

''' Extend([]) function is used to add a list inside the list '''
states.extend(["Ismalia", "Domyat"])

print(states)