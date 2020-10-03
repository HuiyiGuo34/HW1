
from src.DataSetReader import DataSetReader
import pandas as pd
#date,county,state,fips,cases,deaths

class CountryDataSetReader(DataSetReader):

    def __init__(self):
        self.df = pd.read_csv("us-counties.csv")
        self.df = self.df.drop("state",axis=1).drop("fips",axis=1)



    def display(self):
        print(self.df)

if __name__ == '__main__':
    CountryDataSetReader().display()



