import pandas as pd
import glob
import os
import csv

def csv_edit(input_path):

    path = input_path
    csv_files = glob.glob(os.path.join(path, "*.csv"))


    for f in csv_files:
    
        df = pd.read_csv(f)
        name = f.split("\\")[-1]

        df.insert (0, column = "Filename", value = name)
        df.head()

        df.to_csv(f, header = 2, index = False)



def csv_combine(input_path):

    csv_edit(input_path)
    output_path = input_path + "/Combined.csv"
    
    path = input_path
    all_files = glob.glob(path + "/*.csv")
    

    file_list = [pd.read_csv(filename, index_col = None, header = 0) for filename in all_files]
    df = pd.concat(file_list, axis = 0, ignore_index = True)


    df.to_csv(output_path, header = 2, index = False)

    print("Task Completed")

