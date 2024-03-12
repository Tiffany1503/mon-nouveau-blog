import pandas as pd
from blog.models import Airline

def import_airline_data(csv_file_path):
    df = pd.read_csv(csv_file_path, encoding="latin-1", sep=";")
    
    for index, row in df.iterrows():
        Airline.objects.create(
            name=row['Compagnie'],
            ranking=float(row['Classement']),
            airhelp=float(row['AirHelp Score']),
            ponctualite=float(row['Ponctualité']),
            avis=float(row['Avis Client']),
            service=float(row['Efficacité Service Client'])
        )

path = 'tiffa\projet_info\scrapy_tutorials\LilleBarcelone\classement.csv'
import_airline_data(path)