
from src.DataSetReader import DataSetReader
import pandas as pd
#date,county,state,fips,cases,deaths

class StateDataSetReader(DataSetReader):

    def __init__(self):
        self.df = pd.read_csv("us-states.csv")
        self.df = self.df.drop("fips",axis=1)



    def display(self):
        print(self.df)

if __name__ == '__main__':
    StateDataSetReader().display()



