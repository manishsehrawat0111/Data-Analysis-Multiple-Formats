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

    engine=create_engine(
        "mysql+pymysql://pandas:pandas@localhost/pandasdb",
        echo=True)
    
    with engine.connect() as conn:
        result=conn.execute(text("select database();"))
        print("\n connected to :",result.fetchone())

    df.to_sql("students_performance_data",
              con=engine,
              if_exists ="replace",
              index=False)
    print("\n✅ data exported to mysql pandasdb database succesfully")

    print(pd.read_sql("select * from students_performance_data limit 10;",engine))
    
    # visualization 

    # participation on the bases gender for compatative exam
    
    column1=df.groupby("gender")["math_score"].mean()
    labels=column1.index
    
    fig,axs=plt.subplots(1,2,figsize=(10,4))
    
    # pie plot
    axs[0].pie(column1,colors=["pink","blue","orange","skyblue"],labels=labels,
            autopct="%1.1f%%",startangle=90,shadow=True)
    axs[0].set_title("participation on bases gender for compative exam")

    # bar plot
    axs[1].bar(labels,column1,color=["pink","blue","orange","skyblue"])
    axs[1].set_title("participation on babses gander for compative exam")
    axs[1].set_xlabel("gender")
    axs[1].set_ylabel("mean of genders")
    axs[1].grid()
    
    plt.tight_layout()
    plt.show()

    # comparision of math_score,reading_score,attendance_score on the bases gender for comptative exam

    column1=df.groupby("gender")["math_score"].mean()
    column2=df.groupby("gender")["reading_score"].mean()
    column3=df.groupby("gender")["attendance_percent"].mean()
    labels=column1.index

    fig,axs=plt.subplots(1,2,figsize=(14,5))
    # line plot
    axs[0].plot(labels,column1,color="blue",linestyle="-",marker="o",label="mean of math_score")
    axs[0].plot(labels,column2,color="yellow",linestyle="--",marker="s",label="mean of reading_score")
    axs[0].plot(labels,column3,color="pink",linestyle=":",marker="*",label="mean of attendance_percent")
    axs[0].set_title("mean of math_score,reading_score,attendance_percent")
    axs[0].set_xlabel("gender")
    axs[0].set_ylabel("mean")
    axs[0].legend(loc='upper left', bbox_to_anchor=(1, 1))
    
    # bar plot
    width=0.25
    x=np.arange(len(labels))
    axs[1].bar(x-width,column1,width,color="blue",label="mean of math_score")
    axs[1].bar(x,column2,width,color="yellow",label="mean of reading_score")
    axs[1].bar(x+width,column3,width,color="pink",label="mean of attendance_percent")
    axs[1].set_title("mean of math_score,reading_score,attendance_percent")
    axs[1].set_xlabel("gender")
    axs[1].set_ylabel("mean")
    axs[1].set_xticks(x,labels)
    axs[1].legend(loc='upper left', bbox_to_anchor=(1, 1))

    plt.tight_layout()
    plt.show()
    


    

    
    


    
