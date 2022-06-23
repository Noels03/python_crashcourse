#names = ['Mikaela', 'William aka Wilfred', 'Anthony']
#print(names[2])

#message = f"I am friends with {names[0]}"
#print(message)

###########Guest list to a dinner party##############

from email import message


guest_list = ['Isaac Newton', 'Saddartha Gutthama', 'Boose', 'Mik']
#to remove an element from list
guest_list.remove('Mik')
#to add an element to list
guest_list.insert(3, 'Oscar')
guest_list.insert(0, 'Kane')
guest_list.insert(2, 'Rob')
#adds to the end of a list
guest_list.append('Nina')
#message = f"Dearly beloved soul, Nohely Garcia-Franco has cordially invited you, {guest_list}, to a dinner party"
#print(guest_list[3])
#message = f"Dearly beloved soul, do to unfortunate circumstances, only 2 people may attend my dinner party."
#print(message)

invited_guest = guest_list.pop(0)
print(f"I'm sorry {invited_guest}, there is no room for you at the dinner party")
invited_guest = guest_list.pop(-1)
print(f"I'm sorry {invited_guest}, there is no room for you at the dinner party")
invited_guest = guest_list.pop(1)
print(f"I'm sorry {invited_guest}, there is no room for you at the dinner party")
invited_guest = guest_list.pop(2)
print(f"I'm sorry {invited_guest}, there is no room for you at the dinner party")
invited_guest = guest_list.pop(2)
print(f"I'm sorry {invited_guest}, there is no room for you at the dinner party")

message1 = f"Congratulations {guest_list[0]}! You are still invited to the dinner party"
message2 = f"Congratulations {guest_list[1]}! You are still invited to the dinner party"

print(message1)
print(message2)

del guest_list[0]
del guest_list[0]

print(guest_list)

