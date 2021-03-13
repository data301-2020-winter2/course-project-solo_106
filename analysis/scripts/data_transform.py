import math
import pandas as pd

def get_transit_time(df):
    arr = []
    for index, value in df["Transit Epoch"].items():
        arr.append(pd.Timestamp("Jan 1 2009 12:00 UTC") + pd.DateOffset(days=value))
    df.insert(13, "Time of First Transit Event", arr)
    
def get_planet_radius(df):
    arr = []
    EARTH_RADIUS = 6371    # using 6371km as Earth radius
    for index, value in df["Planetary Radius (Earth radii)"].items():
        arr.append(value * EARTH_RADIUS)
    df.insert(17, "Planetary Radius (km)", arr)
    
def get_gravity(df):
    arr = []
    for index, value in df["Stellar Surface Gravity (log10(cm s-2)"].items():
        arr.append(math.pow(10, value) / 100)
    df.insert(21, "Stellar Surface Gravity (m/s^2)", arr)
    
def get_star_radius(df):
    SUN_RADIUS = 696340
    arr = []
    for index, value in df["Stellar Radius (solar radii)"].items():
        arr.append(value * SUN_RADIUS)
    df.insert(23, "Stellar Radius (km)", arr)
    
def get_star_mass(df):
    GRAVITIONAL_CONSTANT = 6.67408 * math.pow(10, -11)
    arr = []
    r = df["Stellar Radius (km)"]
    g = df["Stellar Surface Gravity (m/s^2)"]
    size = df.shape[0]
    for i in range(0, size):
        arr.append((g[i] * math.pow(r[i] * 1000, 2)) / GRAVITIONAL_CONSTANT)
    df.insert(24, "Mass of the Star (kg)", arr)