import pandas as pd


guitars_dict = {
    "Fender Telecaster": "Baby Blue",
    "Gibson Les Paul": "Sunburst",
    "ESP Eclipse": "Dark Green"
}

guitars = pd.Series(guitars_dict)

guitars.index

guitars.iloc[0]
guitars["Fender Telecaster"] # Access 