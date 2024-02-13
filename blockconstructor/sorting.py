"""
  Sorting Module
"""
import pandas as pd


def sortcsv():
    """
      Sort csv file
    """
    file_path = 'mempool.csv'
    df_classeur = pd.read_csv(file_path, sep=",", header = None)
    df_classeur_sorted = df_classeur.sort_values(by= [3, 2], ascending=[False,True] )
    path_Classeur1_sorted = 'newmempool.csv'
    df_classeur_sorted.to_csv(path_Classeur1_sorted, index=False)