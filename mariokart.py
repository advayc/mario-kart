import pandas as pd
from itertools import product

# wg = weight/speed boost
# ac = acceleration boost
drivers = [
    {"Name": "Mario", "WG": 6, "AC": 2},
    {"Name": "Luigi", "WG": 6, "AC": 2},
    {"Name": "Peach", "WG": 4, "AC": 3},
    {"Name": "Daisy", "WG": 4, "AC": 3},
    {"Name": "Yoshi", "WG": 4, "AC": 3},
    {"Name": "Toad", "WG": 2, "AC": 4},
    {"Name": "Toadette", "WG": 2, "AC": 4},
    {"Name": "Koopa Troopa", "WG": 2, "AC": 4},
    {"Name": "Bowser", "WG": 10, "AC": 0},
    {"Name": "Donkey Kong", "WG": 8, "AC": 1},
    {"Name": "Wario", "WG": 10, "AC": 0},
    {"Name": "Waluigi", "WG": 8, "AC": 1},
    {"Name": "Rosalina", "WG": 8, "AC": 1},
    {"Name": "Metal Mario", "WG": 10, "AC": 0}
]

# all the karts and their stats
karts = [
    {"Name": "Standard Kart", "WG": 2, "AC": 2},
    {"Name": "Pipe Frame", "WG": 1, "AC": 3},
    {"Name": "Mach 8", "WG": 3, "AC": 1},
    {"Name": "Steel Driver", "WG": 4, "AC": 0},
    {"Name": "Cat Cruiser", "WG": 2, "AC": 2},
    {"Name": "Circuit Special", "WG": 3, "AC": 1},
    {"Name": "Tri-Speeder", "WG": 4, "AC": 0},
    {"Name": "Badwagon", "WG": 4, "AC": 0},
    {"Name": "Biddybuggy", "WG": 0, "AC": 7},
    {"Name": "Landship", "WG": 0, "AC": 7},
    {"Name": "Sneeker", "WG": 2, "AC": 2},
    {"Name": "Sports Coupe", "WG": 3, "AC": 1},
    {"Name": "Gold Standard", "WG": 3, "AC": 1},
    {"Name": "Standard Bike", "WG": 1, "AC": 3},
    {"Name": "Comet", "WG": 1, "AC": 5},
    {"Name": "Sport Bike", "WG": 1, "AC": 5},
    {"Name": "The Duke", "WG": 2, "AC": 2},
    {"Name": "Flame Rider", "WG": 1, "AC": 3},
    {"Name": "Varmint", "WG": 1, "AC": 3},
    {"Name": "Mr. Scooty", "WG": 0, "AC": 7},
    {"Name": "Jet Bike", "WG": 1, "AC": 5},
    {"Name": "Yoshi Bike", "WG": 1, "AC": 5},
    {"Name": "Standard ATV", "WG": 4, "AC": 0},
    {"Name": "Wild Wiggler", "WG": 1, "AC": 3},
    {"Name": "Teddy Buggy", "WG": 2, "AC": 2},
    {"Name": "GLA", "WG": 4, "AC": 0},
    {"Name": "W 25 Silver Arrow", "WG": 1, "AC": 3},
    {"Name": "300 SL Roadster", "WG": 2, "AC": 2},
    {"Name": "Blue Falcon", "WG": 1, "AC": 3},
    {"Name": "Tanooki Kart", "WG": 3, "AC": 1},
    {"Name": "B Dasher", "WG": 3, "AC": 1},
    {"Name": "Master Cycle", "WG": 2, "AC": 2}
]

# how long we're racing for (in seconds)
T = 30  # seconds

# uses some basic physics - distance = acceleration * time^2 / 2 during speedup
# then adds constant speed distance if we hit max speed
def calculate_displacement(vmax, a, T):
    # time it takes to reach top speed
    t1 = vmax / a  
    
    # if we don't reach max speed before race ends
    if T <= t1:  
        D = 0.5 * a * T**2
    # if we do hit max speed
    else:  
        # distance covered while speeding up
        D1 = 0.5 * a * t1**2  
        # distance covered at max speed
        D2 = vmax * (T - t1)  
        D = D1 + D2
    return D

# store all the results in this list
data = []
for driver, kart in product(drivers, karts):
    # add up the speed and acceleration bonuses
    vmax = driver["WG"] + kart["WG"]  
    a = driver["AC"] + kart["AC"]  
    
    # calculate how far this combo goes
    displacement = calculate_displacement(vmax, a, T)
    
    # save all the info
    data.append({
        "Driver": driver["Name"],
        "Kart": kart["Name"],
        "Max Speed": vmax,
        "Acceleration": a,
        "Displacement (m)": displacement
    })

# turn our list into a pandas dataframe
df = pd.DataFrame(data)

# put all into an excel file
df.to_excel("Mario_Kart_Displacement.xlsx", index=False)

print("spreadsheet created: Mario_Kart_Displacement.xlsx")
