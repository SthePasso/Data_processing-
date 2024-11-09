import pandas as pd

#Load the file
file_name = "Student_grade.csv"
#Dataframe 
df = pd.read_csv(file_name)
print(df.head(10)) ## whenever we have df.head() method, then its going to print only first five from the database, if we want more
                        ## then add the number you want 

# Load and read a json
file_jason = "file_jason.json"
df_json = pd.read_json(file_jason)
print(df_json)

## Create 2 nex files (.csv and .json). Read them and print the first 5 lines of this files
# upload in github





