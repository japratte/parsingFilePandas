import pandas as pd

"""
This quick program will parse thru a tab delimited file and help grab
data in rows/columns using pandas.
"""

path_to_csv = "text.file" # <<< input file to parse here

df = pd.read_csv(path_to_csv, delimiter="\t")

for i in range(df.shape[0]):
    
    col = df.iloc[i]
    
    # col."id" will grab items in columns by the selected
    # id from the top line of the tab delim file

    # ex:
    #
    # name = col.names
    # nameList.append(name)
    #
    # will grab an item in the names column of the file
    # and set it as the variable "name", then that variable
    # will be pushed to list "nameList".
    #
    # This will be repeated until the file ends.
    


