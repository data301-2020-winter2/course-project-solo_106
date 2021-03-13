import pandas as pd

def save_to_csv(df):
    print("File will be saved to ../data/processed")
    user_input = input("Enter file name with .csv :")
    df.to_csv("../data/processed/" + user_input, index=False)
    print("Done")
