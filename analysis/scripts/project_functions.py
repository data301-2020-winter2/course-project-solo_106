import pandas as pd
from scripts import data_transform as dt

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

    dt.get_transit_time(df)
    dt.get_planet_radius(df)
    dt.get_gravity(df)
    dt.get_star_radius(df)
    dt.get_star_mass(df)

    return df