import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Data_Set=pd.read_csv('C:/Users/Komail Butt/Python Data Science Projects/Project_1 Titanic Disaster/Titanic.csv')

# Change the columns’ names as Name, Survived, Gender, Age and Class
Data_Set.columns= ["Name", "Survived", "Sex", "Age", "Class"]

# Total Number of Rows in the Data provided
N_Rows=len(Data_Set)

# Quickly check if some columns have empty Data
Quick_Check_Missing_Data= Data_Set.count()

# Find the first 15 rows in our dataset
First_15= Data_Set.head(15)

# Find the last 15 rows in our dataset
Last_15= Data_Set.tail(15)

# Calculate the average age of passengers
# Avg_Age=Data_Set.mean()

# Find the oldest passenger’s age and name
Name_Max_Age= Data_Set[Data_Set["Age"].max()==Data_Set["Age"]]

# Find the youngest passenger’s age and name
Name_Min_Age= Data_Set[Data_Set["Age"].min()==Data_Set["Age"]]

# How many Classes are there in our Data Set and how many passengers they contain?
Data_Set_Class= Data_Set.groupby("Class")
Groups_In_Classes= Data_Set_Class.groups
People_In_Group_1= len(Data_Set_Class.get_group("1st"))
People_In_Group_2= len(Data_Set_Class.get_group("2nd"))
People_In_Group_3= len(Data_Set_Class.get_group("3rd"))

# Find the total survivors’ count
Data_Set_Survivors= Data_Set.groupby("Survived")
Groups_Survive_Or_Death= Data_Set_Survivors.groups
# So Two Groups are there in Survived Column yes and no

# Number of People Survived
People_Survived= len(Data_Set_Survivors.get_group("yes"))

# Numner of People Dead
People_Dead= len(Data_Set_Survivors.get_group("no"))

# Find the youngest survivor age and name
Survivor= Data_Set_Survivors.get_group("yes")
Youngest_Survivor= Survivor[Survivor["Age"].min()==Survivor["Age"]]

# Find the number of survivors of 3rd class passengers
Third_Group_Survivors= Survivor.groupby("Class") 
Survive_People_Class_Third=len(Third_Group_Survivors.get_group("3rd"))

# Create a pie chart that showed the distribution of passengers by class.
States=np.array([People_In_Group_1,People_In_Group_2,People_In_Group_3])
# States=[People_In_Group_1,People_In_Group_2,People_In_Group_3]
Labels=["Group_1","Group_2","Group_3"]
plt.pie(States, labels = Labels,autopct="%1.1f%%")
plt.show()



# print(Survive_People_Class_Third)
# print(People_Dead)

