"""
  Sorting Module
"""
import pandas as pd
import csv


def sortcsv():
    """
      Sort csv file
    """
    file_path = 'mempool.csv'
    df_classeur = pd.read_csv(file_path, sep=",", header = None)
    df_classeur_sorted = df_classeur.sort_values(by= [3, 2], ascending=[False,True] )
    path_Classeur1_sorted = 'newmempool.csv'
    df_classeur_sorted.to_csv(path_Classeur1_sorted, index=False)


def sortcsv2():
    """
    Sort csv file by two values
    """
    try:
        file_path = 'mempool.csv'
        newfile_path = 'newmempool.csv'
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            data = list(csv_reader)
        sorted_data = sorted(data, key=lambda row: (-int(row[1]), row[2]))
        with open(newfile_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(sorted_data)   
    except Exception as e:
        print("An error occurred:", e)
