import pandas as pd
df = pd.read_csv("Data.csv")


# data = {}
# print(df)
#
# columns = df.columns[0]
#
# # setting up data dictionary with column names as keys and their values as list
# for x in range(len(df.columns)):
#     data[df.columns[x]] = df[df.columns[x]].tolist()
#
# # Calculating Total Salary
# def calcTotalSalary():
#     global data
#     totalSalary = 0
#     for salary in data["Salary"]:
#         totalSalary += int(salary)
#     return totalSalary
#
# # print(calcTotalSalary())
#
# def anyMissingValues():
#     global data
#     for key in data:
#         for value in data[key]:
#             if pd.isna(value):
#                 return {key: data[key]}
#     return False
#
# # print(anyMissingValues())
#
# # Filtering Data based on department, salary, joining date and experience
# def filterData(department: str = "", salary: int = 0, joiningData: str = "", experience: int = 0):
#     global data


# print(filterData())

totalSalary = df['Salary'].sum()
avgSalary = df['Salary'].mean()
salary_per_dept = df.groupby('Department')['Salary'].sum().to_dict()
groupedByDepartment = df.groupby('Department').size().to_dict()
filterSalary = df[df['Salary'] > 60000].to_dict(orient='records')

groupByDept = df.groupby('Department')

print("groupByDept", groupByDept.get_group('IT'))
# Filter Based on Condition
filterData = df[(df['Department'] == 'IT') & (df["Salary"] > 55000)]

# print("totalSalary: ", totalSalary)
# print("\navgSalary: ", avgSalary)
# print("\nsalary_per_dept: ", salary_per_dept)
# print("\ngroupedByDepartment: ", groupedByDepartment)
# print("\nfilterSalary: ", filterSalary)
# print("\nfilterData: ", filterData)