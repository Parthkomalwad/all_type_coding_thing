t = int(input())
entry_people = []
exit_people = []
maxi = 0
for i in range(t):
    entry_people.append(int(input()))
for i in range(t):
    exit_people.append(int(input()))
no_of_people_on_cruise = 0
for i in range(t):
    no_of_people_on_cruise = no_of_people_on_cruise + \
        (entry_people[i] - exit_people[i])
    if(no_of_people_on_cruise > maxi):
        maxi = no_of_people_on_cruise
print(maxi)
