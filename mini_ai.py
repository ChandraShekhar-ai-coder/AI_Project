people = [
    {
        "Name": "Rocky", 
        "Age": 12,
        "Gender": "Boy",
        "Birthplace": "Lucknow",
    }, # <-- Added comma here
    {        
        "Name": "Aman",
        "Age": 14, 
        "Gender": "Boy",
        "Birthplace": "Luciana",
    }, # <-- Added comma here
    {
        "Name": "Amrita",
        "Age": 38, 
        "Gender": "Girl",
        "Birthplace": "London",
    }
]

Name = input("Enter Name: ")
found = False

for person in people:
    if person["Name"].lower() == Name.lower():
        # Fixed: Brought onto one line and properly indented
        print(f'{person["Name"]} is a {person["Age"]}-year-old {person["Gender"]}.')
        # Fixed: Properly indented and added the missing closing quote '
        print(f'born in {person["Birthplace"]}')
        
        found = True
        break

# Fixed: Aligned properly outside the for-loop
if found == False:
    print("person not found")