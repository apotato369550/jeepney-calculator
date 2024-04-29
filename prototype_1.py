routes = {
    "13c": ["Talamban", "Gov. M. Cuenco Ave.", "Gaisano Grand Mall (Talamban)", "University of San Carlos (Talamban)", "Banilad", "Banilad Town Center", "Gaisano Country Mall", "University of Cebu (Banilad)", "Paradise Village", "Cebu Country Club", "Samantabhadra Institute", "Arch. Reyes Ave.", "BIR", "Cebu Business Park", "Pag-ibig Fund", "Ayala Center Cebu", "Mindanao Ave.", "Samar Loop", "Luzon Ave.", "Tune Hotels", "Arch. Reyes Ave.", "Hotel Elizabeth", "Gorordo Ave.", "Asilo dela Melagrosa", "Camp Sutero (Cebu City Police office)", "Gen. Echavez St.", "Sikatuna St.", "Parian", "Colon St.", "Gaisano Main", "University of the Visayas", "Colonnade Supermarket", "Colon", "Pelaez St.", "University of San Carlos (Main)", "P. del Rosario St.", "Imus Ave.", "M.J. Cuenco Ave.", "Hipodromo", "Mactan St.", "Cebu Business Park", "Leyte Loop", "Samar Loop", "Lexmark", "Mindanao Ave.", "Ayala Center Cebu", "Arch. Reyes Ave.", "BIR", "Samantabhadra Institute", "Gov. M. Cuenco Ave.", "Banilad", "UC (Banilad)", "Gaisano Country Mall", "Banilad Town Center", "Foodland", "University of San Carlos (Talamban)", "Gaisano Grand Mall (Talamban)", "Talamban"
    ]
}

'''
test cases

talamban to banilad = 
"Talamban", "Gov. M. Cuenco Ave.", "Gaisano Grand Mall (Talamban)", "University of San Carlos (Talamban)", "Banilad"

banilad to talamban = 
"Banilad", "UC (Banilad)", "Gaisano Country Mall", "Banilad Town Center", "Foodland", "University of San Carlos (Talamban)", "Gaisano Grand Mall (Talamban)", "Talamban"
'''

starting_point = input("Enter Starting point: ")
destination = input("Enter destination: ")
jeep = ""

for route in routes:
    if starting_point in routes[route] and destination in routes[route]:
        jeep = route

starting_point_indexes = []
destination_indexes = []

for i in range(len(routes[jeep])):
    if routes[jeep][i] == starting_point:
        starting_point_indexes.append(i)
    if routes[jeep][i] == destination:
        destination_indexes.append(i)

# difference needs to be positive
# look for the smallest difference

difference = float('inf')
final_start, final_destination = 0, 0

for starting_index in starting_point_indexes:
    print(f"Starting point index: {starting_index}")
    for destination_index in destination_indexes:
        print(f"destination point index: {destination_index}")
        if destination_index - starting_index < difference and destination_index - starting_index > 0:
            difference = destination_index - starting_index
            final_start, final_destination = starting_index, destination_index

print("Result:")
print("Jeep: " + str(jeep))
for i in range(final_start, final_destination + 1):
    print(routes[jeep][i] + " -> ")