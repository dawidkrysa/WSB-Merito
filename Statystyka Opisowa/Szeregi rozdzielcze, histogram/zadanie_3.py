import matplotlib.pyplot as plt
import numpy as np

# Busiest North American Airports. Based on the total passenger traffic,
# the airports in the following list are the 20 busiest airports in
# North America in 2018 (The World Almanac).
#
# a. Which is busiest airport in terms of total passenger traffic?
#    Which is the least busy airport in terms of total passenger traffic?
# b. Using a class width of 10, develop a frequency distribution of the data
#    starting with 30–39.9, 40–49.9, 50–59.9, and so on.
# c. Prepare a histogram. Interpret the histogram.

airport = np.array(
    [
        "Boston Logan (BOS)",
        "Charlotte Douglas (CLT)",
        "Chicago O'Hare (ORD)",
        "Dallas/Ft. Worth (DFW)",
        "Denver (DEN)",
        "Detroit Metropolitan (DTW)",
        "Hartsfield-Jackson Atlanta (ATL)",
        "Houston George Bush (IAH)",
        "Las Vegas McCarran (LAS)",
        "Los Angeles (LAX)",
        "Miami (MIA)",
        "Minneapolis/St. Paul (MSP)",
        "New York John F. Kennedy (JFK)",
        "Newark Liberty (EWR)",
        "Orlando (MCO)",
        "Philadelphia (PHL)",
        "Phoenix Sky Harbor (PHX)",
        "San Francisco (SFO)",
        "Seattle-Tacoma (SEA)",
        "Toronto Pearson (YYZ)",
    ]
)

passengers_m = np.array(
    [
        36.3,
        44.4,
        78,
        65.7,
        58.3,
        34.4,
        104.2,
        41.6,
        47.5,
        80.9,
        44.6,
        37.4,
        59.1,
        40.6,
        41.9,
        36.4,
        43.3,
        53.1,
        45.7,
        44.3,
    ]
)


print("""---------------------------------------------------------------
a. Which is busiest airport in terms of total passenger traffic?
   Which is the least busy airport in terms of total passenger traffic?
---------------------------------------------------------------""")
busy_airport = np.argmax(passengers_m)
least_busy_airport = np.argmin(passengers_m)
print(f"Busiest airport: {airport[busy_airport]}")
print(f"Least busy airport: {airport[least_busy_airport]}")


print("""
---------------------------------------------------------------
b. Using a class width of 10, develop a frequency distribution of the data
   starting with 30–39.9, 40–49.9, 50–59.9, and so on.
---------------------------------------------------------------""")
granice = np.arange(30, 120, 10)  # 30, 40, ..., 110

print(f"{'Przedział':<12} {'Liczebność':>10}")
for lo in granice[:-1]:
    n = np.sum((passengers_m >= lo) & (passengers_m < lo + 10))
    przedzial = f"{lo}-{lo + 9.9}"
    print(f"{przedzial:<12} {n:>10}")


print("""
---------------------------------------------------------------
c. Prepare a histogram. Interpret the histogram.
---------------------------------------------------------------""")
plt.hist(passengers_m, bins=granice.tolist(), edgecolor="black")
plt.xticks(granice)
plt.xlabel("Ruch pasażerski (mln)")
plt.ylabel("Liczba lotnisk")
plt.title("20 najbardziej ruchliwych lotnisk Ameryki Północnej, 2018")
plt.show()

print("""Interpretacja:
Rozkład jest asymetryczny, prawostronnie skośny. Można zaobserwować, że najwięcej lotnisk
ma ruch pasażerski w przedziale od 40 do 49,9 mln pasazerów. Wraz ze wzrostem ruchu pasażerskiego
maleje liczba lotnisk, która takowy posiada. Przedział 90-99,9 jest pusty, a lotnisko w Atlancie
znacząco odstaje od pozostałych lotnisk. 
""")
