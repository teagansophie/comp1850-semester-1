import pandas 

data = pandas.read_csv("lifestyle_data.csv")

# What data type is `data` as output from the `read_csv()` method?

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students
number_of_students = data.count()
print(f"The number of students is {number_of_students}")

# Find the mean average GPA of the students
average_GPA = data["GPA"].mean()
print(f"The average GPA is {average_GPA}")
# Find the standard deviation of how much sleep students get per day

standard_deviation = data["Sleep_Hours_Per_Day"].std()
print(f"The standard deviation of the students is: {standard_deviation}")

# Find the maximum amount of study hours per day
max_hours = data["Study_Hours_Per_Day"].max()
print(f"The max study hours was: {max_hours}")

# Sort the students by social hours per day ascending (lowest -> highest)
sort_social_hours = data["Social_Hours_Per_Day"].sort_values( ascending = True)

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one
hours_added = data["Sleep_Hours_Per_Day"] + data["Social_Hours_Per_Day"] + data["Study_Hours_Per_Day"] + data["Extracurricular_Hours_Per_Day"] + data["Physical_Activity_Hours_Per_Day"]
print(hours_added)

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.

high_stress = data[data["Stress_Level"] == "High"]
print(f"Students with high stress levels: {high_stress}")

low_stress = data[data["Stress_Level"] == "Low"]
print(f"Students with low stress levels: {low_stress}")

# Can you work out whether having a higher stress level leads to a higher GPA?
# .corr only works on numerical data so need to convert Low into a value 

correlation = data.groupby("Stress_Level")["GPA"].mean()
print(correlation)
