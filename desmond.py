name,department,level,course,score
John,Chemical Science,100,CSC101,85
Mary,Computer Science,100,MTH101,78
James,Cyber Security,200,CSC201,91
Grace,Computer Science,200,MTH201,18
David,Computer Science,300,CSC301,75
Sarah,Data Science,300,CSC302,88
Daniel,Agricultural Science,400,CSC401,95
Joy,Computer Science,400,CSC402,45
Peter,Data Science,500,CSC501,82
Esther,Computer Science,500,CSC502,12
Inioluwa,Cyber Security,500,CSC503,100



import pandas as pd
df = pd.read_csv("exam.csv")
maxdept = df[df["department"] == "Data Science"]
highmax = maxdept[maxdept["score"] == 88]
print(highmax[["name", "score","level"]])
