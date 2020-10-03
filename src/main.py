
from src.CountryDataSetReader import CountryDataSetReader
from src.StateDataSetReader import StateDataSetReader
from src.UsDataSetReader import UsDataSetReader

def run():

    while(True):
        cmd = input("please select one dataset：country, all states, all counties: ")
        if(cmd == 'country'):
            UsDataSetReader().display()
        elif( cmd == 'all states'):
            StateDataSetReader().display()
        elif(cmd =="all counties"):
            CountryDataSetReader().display()
        elif(cmd =="quit"):
            print("bye ~")
            break
        else:
            print("invalid input")

if __name__ == '__main__':
    run()