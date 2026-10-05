# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey",
    "China": "The yellow river",
    "Egypt": "River Nile"
}

print(rivers)


# Display all the keys
keys = rivers.keys()
print(keys)

# Display all the values
values = rivers.values()
print(values)
# Display all the key:value pairs, as tuples
print(rivers.items())
# Delete an entry from the rivers database
print(rivers.pop("London"))