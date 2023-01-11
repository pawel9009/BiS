import requests
import pandas as pd
import io

url = 'https://stooq.pl/q/d/l/?s=xaupln&i=d'


def scrap_data(url = url):
    response = requests.get(url)
    df = pd.read_csv(io.StringIO(response.text), header=0)
    return df
