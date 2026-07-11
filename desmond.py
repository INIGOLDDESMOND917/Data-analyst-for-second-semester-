import pandas as pd
df = pd.read_csv("exam.csv")
df.columns = df.columns.str.strip()
for department in df["department"].unique():
    dept = df[df["department"] == department]
    highest = dept.loc[dept["score"].idxmax()]
    lowest = dept.loc[dept["score"].idxmin()]
    print("Department:", department)
    print("\nHighest Score")
    print("Name:", highest["name"])
    print("Course:", highest["course"])
    print("Score:", highest["score"])
    print("\nLowest Score")
    print("Name:", lowest["name"])
    print("Course:", lowest["course"])
    print("Score:", lowest["score"])
    print("\nStudents with at least 20%")
    print(dept[dept["score"] >= 20][["name", "course", "score"]])
    print("\fStudents with at least 80%")
    print(dept[dept["score"] >= 80][["name", "course", "score"]])