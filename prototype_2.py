routes = {
    "13c": ["Talamban", "Gov. M. Cuenco Ave.", "Gaisano Grand Mall (Talamban)", "University of San Carlos (Talamban)", "Banilad", "Banilad Town Center", "Gaisano Country Mall", "University of Cebu (Banilad)", "Paradise Village", "Cebu Country Club", "Samantabhadra Institute", "Arch. Reyes Ave.", "BIR", "Cebu Business Park", "Pag-ibig Fund", "Ayala Center Cebu", "Mindanao Ave.", "Samar Loop", "Luzon Ave.", "Tune Hotels", "Arch. Reyes Ave.", "Hotel Elizabeth", "Gorordo Ave.", "Asilo dela Melagrosa", "Camp Sutero (Cebu City Police office)", "Gen. Echavez St.", "Sikatuna St.", "Parian", "Colon St.", "Gaisano Main", "University of the Visayas", "Colonnade Supermarket", "Colon", "Pelaez St.", "University of San Carlos (Main)", "P. del Rosario St.", "Imus Ave.", "M.J. Cuenco Ave.", "Hipodromo", "Mactan St.", "Cebu Business Park", "Leyte Loop", "Samar Loop", "Lexmark", "Mindanao Ave.", "Ayala Center Cebu", "Arch. Reyes Ave.", "BIR", "Samantabhadra Institute", "Gov. M. Cuenco Ave.", "Banilad", "UC (Banilad)", "Gaisano Country Mall", "Banilad Town Center", "Foodland", "University of San Carlos (Talamban)", "Gaisano Grand Mall (Talamban)", "Talamban"
    ],
    "04L": ["Lahug", "JY Square Mall", "Gorordo Ave.", "Corner Sudlon", "Corner Beverly Hills", "Corner Dep-ed (EcoTech)", "Mormons Church (Church of Jesus Christ of Latter-day Saints)", "Lahug Brgy Hall", "University of the Philippines (Cebu)", "Sugbo Cultural Center", "Harolds Hotel", "Tonross Apartelle", "The Golden Peak Hotel", "N. Escario Hotel", "Philhealth", "Kuya J's Restaurant", "Cebu Parklane Hotel", "Grand Cenia Hotel", "Hongkong Plaza Hotel", "Cebu Business Park", "Mindanao Ave.", "Pag-ibig Fund", "Ayala Center Cebu", "Cardinal Rosales Ave.", "Pope John Paul II Ave.", "PLDT", "Carmelite Monastery", "St. Joseph Parish (Mabolo Church)", "SM City Cebu", "SM City Cebu", "Radisson Hotel", "Sergio Osmena Blvd.", "Kaohsiung St.", "Cebu Daily News", "A. Soriano Ave.", "Juan Luna Ave. ext.", "Pope John Paul II Ave.", "Mabolo Church", "Andoks Mabolo", "Carmelite Monastery", "San Carlos Seminary College", "TESDA VII", "Salinas Drive", "Cebu IT Park", "Waterfront Hotel", "Crowne Garden Hotel", "JY Square Mall", "Lahug"
    ]
}


'''
test cases that should work

talamban to banilad = 
"Talamban", "Gov. M. Cuenco Ave.", "Gaisano Grand Mall (Talamban)", "University of San Carlos (Talamban)", "Banilad"

banilad to talamban = 
"Banilad", "UC (Banilad)", "Gaisano Country Mall", "Banilad Town Center", "Foodland", "University of San Carlos (Talamban)", "Gaisano Grand Mall (Talamban)", "Talamban"

Corner Sudlon to Philhealth
 "Corner Sudlon", "Corner Beverly Hills", "Corner Dep-ed (EcoTech)", "Mormons Church (Church of Jesus Christ of Latter-day Saints)", "Lahug Brgy Hall", "University of the Philippines (Cebu)", "Sugbo Cultural Center", "Harolds Hotel", "Tonross Apartelle", "The Golden Peak Hotel", "N. Escario Hotel", "Philhealth"

Salinas drive to lahug
"Salinas Drive", "Cebu IT Park", "Waterfront Hotel", "Crowne Garden Hotel", "JY Square Mall", "Lahug"

Hipodromo to PLDT
13c
"Hipodromo", "Mactan St.", "Cebu Business Park"
04l
"Cebu Business Park", "Mindanao Ave.", "Pag-ibig Fund", "Ayala Center Cebu", "Cardinal Rosales Ave.", "Pope John Paul II Ave.", "PLDT"

'''

def intersection(list_1, list_2):
    list_3 = [value for value in list_1 if value in list_2]
    return list_3

starting_point = input("Enter Starting point: ")
destination = input("Enter destination: ")
jeeps_starting_point = []
jeeps_destination_points = []

# jeeps with starting point and with ending point
for jeep in routes:
    if starting_point in routes[jeep]:
        jeeps_starting_point.append(jeep)
    if destination in routes[jeep]:
        jeeps_destination_points.append(jeep)
print(" starting points: " + str(jeeps_starting_point))
print(" destination points: " + str(jeeps_destination_points))


valid_starting_jeeps = []
valid_destination_jeeps = []
jeep_pairs = []
# see if they have any stops in common
for starting_jeep in jeeps_starting_point:
    for destination_jeep in jeeps_destination_points:
        if intersection(routes[starting_jeep], routes[destination_jeep]):
            valid_starting_jeeps.append(starting_jeep)
            valid_destination_jeeps.append(destination_jeep)
            jeep_pairs.append((starting_jeep, destination_jeep))

if valid_starting_jeeps and valid_destination_jeeps:
    print("There is a valid route")
else: 
    print("There is no valid route")

# can the problem be solved using one jeep or two jeeps
if intersection(valid_starting_jeeps, valid_destination_jeeps):
    jeeps = intersection(valid_starting_jeeps, valid_destination_jeeps)
    for jeep in jeeps:
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
else:
    for jeep_pair in jeep_pairs:
        starting_index = 0
        ending_index = 0
        starting_intersection = 0
        ending_intersection = 0
        print("Jeep pair: " + str(jeep_pair))
        for i in range(len(routes[jeep_pair[0]])):
            if routes[jeep_pair[0]][i] == starting_point:
                starting_index = i
                break
        for i in range(len(routes[jeep_pair[1]])):
            if routes[jeep_pair[1]][i] == destination:
                ending_index = i
                break
        for i in range(starting_index, len(routes[jeep_pair[0]])):
            if routes[jeep_pair[0]][i] in routes[jeep_pair[1]]:
                starting_intersection = i
                break
        for i in range(0, ending_index):
            if routes[jeep_pair[1]][i] == routes[jeep_pair[0]][starting_intersection]:
                ending_intersection = i
                break
            
        print("Starting Jeep: " + jeep_pair[0])
        for i in range(starting_index, starting_intersection + 1):
            print(routes[jeep_pair[0]][i] + " -> ")
        
        print("Ending Jeep: " + jeep_pair[1])
        for i in range(ending_intersection, ending_index + 1):
            print(routes[jeep_pair[1]][i] + " -> ")


        
