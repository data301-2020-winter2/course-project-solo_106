import pandas as pd
import math

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

def load_and_process(url_or_path_to_csv_file):
    df = (
        pd.read_csv(url_or_path_to_csv_file)
        .drop(columns=["koi_period_err1", "koi_period_err2", "koi_time0bk_err1", "koi_time0bk_err2", "koi_impact_err1",
                       "koi_impact_err2", "koi_duration_err1", "koi_duration_err2", "koi_depth_err1", "koi_depth_err2", 
                       "koi_prad_err1", "koi_prad_err2", "koi_teq_err1", "koi_teq_err2", "koi_insol_err1", "koi_insol_err2",
                       "koi_steff_err1", "koi_steff_err2", "koi_slogg_err1", "koi_slogg_err2", "koi_srad_err1", "koi_srad_err2",
                       "koi_kepmag", "koi_model_snr", "koi_tce_plnt_num", "koi_tce_delivname", "koi_insol", "koi_impact"])
        .rename(columns={"rowid":"id", "kepid":"Kepler id", "kepoi_name":"KOI Name", "Kepler_name":"Kepler Name", "koi_disposition":"Exoplanet Archive Disposition",
                      "koi_pdisposition":"Disposition Using Kepler Data", "koi_score":"Confidence", "koi_fpflag_nt":"Not Transit Like", "koi_fpflag_ss":"Stellar Eclipse",
                      "koi_fpflag_co":"Centroid Offset", "koi_fpflag_ec":"Contamination", "koi_period":"Orbital Period (days)", "koi_time0bk":"Transit Epoch",
                      "koi_duration":"Transit Duration (hours)", "koi_depth":"Transit Depth (parts per million)", "koi_prad":"Planetary Radius (Earth radii)",
                      "koi_teq":"Equilibrium Temperature (Kelvin)", "koi_steff":"Stellar Effective Temperature (Kelvin)", "koi_slogg":"Stellar Surface Gravity (log10(cm s-2)",
                      "koi_srad":"Stellar Radius (solar radii)", "ra":"Right Ascension", "dec":"Declination"})
        )

    get_transit_time(df)
    get_planet_radius(df)
    get_gravity(df)
    get_star_radius(df)
    get_star_mass(df)

    return df


    
def save_to_csv(df):
    print("File will be saved to ../data/processed")
    user_input = input("Enter file name with .csv :")
    df.to_csv("../data/processed/" + user_input, index=False)
    print("Done")