import pandas as pd
from itertools import product

# driver stats (MS = max speed, AC = acceleration)
drivers = [
    {"Name": "Mario", "MS": 7, "AC": 2},
    {"Name": "Luigi", "MS": 6, "AC": 2},
    {"Name": "Peach", "MS": 4, "AC": 3},
    {"Name": "Daisy", "MS": 4, "AC": 3},
    {"Name": "Yoshi", "MS": 4, "AC": 3},
    {"Name": "Toad", "MS": 2, "AC": 4},
    {"Name": "Toadette", "MS": 2, "AC": 4},
    {"Name": "Koopa Troopa", "MS": 2, "AC": 4},
    {"Name": "Bowser", "MS": 10, "AC": 0},
    {"Name": "Donkey Kong", "MS": 8, "AC": 1},
    {"Name": "Wario", "MS": 10, "AC": 0},
    {"Name": "Waluigi", "MS": 8, "AC": 1},
    {"Name": "Rosalina", "MS": 8, "AC": 1},
    {"Name": "Metal Mario", "MS": 10, "AC": 0}
]

# kart stats
karts = [
    {"Name": "Standard Kart", "MS": 3, "AC": 3},
    {"Name": "Pipe Frame", "MS": 1, "AC": 3},
    {"Name": "Mach 8", "MS": 3, "AC": 1},
    {"Name": "Steel Driver", "MS": 4, "AC": 0},
    {"Name": "Cat Cruiser", "MS": 2, "AC": 2},
    {"Name": "Circuit Special", "MS": 3, "AC": 1},
    {"Name": "Tri-Speeder", "MS": 4, "AC": 0},
    {"Name": "Badwagon", "MS": 4, "AC": 0},
    {"Name": "Biddybuggy", "MS": 0, "AC": 7},
    {"Name": "Landship", "MS": 0, "AC": 7},
    {"Name": "Sneeker", "MS": 2, "AC": 2},
    {"Name": "Sports Coupe", "MS": 3, "AC": 1},
    {"Name": "Gold Standard", "MS": 3, "AC": 1},
    {"Name": "Standard Bike", "MS": 1, "AC": 3},
    {"Name": "Comet", "MS": 1, "AC": 5},
    {"Name": "Sport Bike", "MS": 1, "AC": 5},
    {"Name": "The Duke", "MS": 2, "AC": 2},
    {"Name": "Flame Rider", "MS": 1, "AC": 3},
    {"Name": "Varmint", "MS": 1, "AC": 3},
    {"Name": "Mr. Scooty", "MS": 0, "AC": 7},
    {"Name": "Jet Bike", "MS": 1, "AC": 5},
    {"Name": "Yoshi Bike", "MS": 1, "AC": 5},
    {"Name": "Standard ATV", "MS": 4, "AC": 0},
    {"Name": "Wild Wiggler", "MS": 1, "AC": 3},
    {"Name": "Teddy Buggy", "MS": 2, "AC": 2},
    {"Name": "GLA", "MS": 4, "AC": 0},
    {"Name": "W 25 Silver Arrow", "MS": 1, "AC": 3},
    {"Name": "300 SL Roadster", "MS": 2, "AC": 2},
    {"Name": "Blue Falcon", "MS": 1, "AC": 3},
    {"Name": "Tanooki Kart", "MS": 3, "AC": 1},
    {"Name": "B Dasher", "MS": 3, "AC": 1},
    {"Name": "Master Cycle", "MS": 2, "AC": 2}
]

# race duration (in seconds)
T = 30

# calculate total displacement
def calculate_displacement(vmax, a, T):
    a = max(0.1, a)  # ensure minimum acceleration
    t1 = vmax / a  # time to reach max speed
    
    if T <= t1:  # race ends before reaching max speed
        D = 0.5 * a * T**2
    else:  # race includes max speed phase
        D1 = 0.5 * a * t1**2  # displacement during acceleration
        D2 = vmax * (T - t1)  # displacement at max speed
        D = D1 + D2
    return D

# collect data
data = []
for driver, kart in product(drivers, karts):
    vmax = driver["MS"] + kart["MS"]  # max speed
    a = driver["AC"] + kart["AC"]  # total acceleration
    displacement = calculate_displacement(vmax, a, T)  # total displacement
    
    data.append({
        "Driver": driver["Name"],
        "Kart": kart["Name"],
        "Max Speed": vmax,
        "Acceleration": a,
        "Displacement (m)": round(displacement, 2)  # round for readability
    })

# convert to dataframe and save as CSV
df = pd.DataFrame(data)
df.to_csv("Mario_Kart_Displacement.csv", index=False)
print("spreadsheet created: Mario_Kart_Displacement.csv")
