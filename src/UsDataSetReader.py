
from src.DataSetReader import DataSetReader
import pandas as pd
#date,county,state,fips,cases,deaths

class UsDataSetReader(DataSetReader):

    def __init__(self):
        self.df = pd.read_csv("us.csv")

    def display(self):
        print(self.df)

if __name__ == '__main__':
    UsDataSetReader().display()



