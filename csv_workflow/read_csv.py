#  This script will read CSV files for analysis

# install these 4 python libraries before running the script:
# install pandas (pip install pandas)
# install numpuy (pip install numpy)
# install matplotlib (pip install matplotlib)
# install sqlalchemy pymysql (pip install sqlalchemy pymysql)


def csv_file(file_path):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from sqlalchemy import create_engine,text

    df=pd.read_csv(file_path)
    print("\n✅ file load succesfully ")

    print("\n information about file:")
    print(df.info())

    print("\n shape of file:",df.shape)

    print("\n first 5 rows of file:")
    print(df.head())

    print("\n last 5 ros of file:")
    print(df.tail())

    print("\n random 10 rows of file:")
    print(df.sample(10))

    print(df.describe())
    
    print("\n count emplty values in each column:")
    print(df.isnull().sum())

    df.dropna(subset=["student_id"],inplace=True)
    print("/n✅ all rows with empty student_id removed")

    df.fillna({"math_score":df["math_score"].mean(),
               "reading_score":df["reading_score"].mean(),
               "attendance_percent":df["attendance_percent"].mean(),
               "age":df["age"].mean(),
               "gender":"Not Mentioned"},
               inplace=True)
    print("\n✅ all empty values filled succesfully",
          "/n math_score with mean of the column",
          "/n reading_score with mean of the column",
          "/n attendance_percent with mean of the column",
          "/n age with mean of the column",
          "/n gender with Not Mentioned")
    
    print(df.isnull().sum())
    print("\n count empty values in each column after cleaning:")

    


    

    
    


    
