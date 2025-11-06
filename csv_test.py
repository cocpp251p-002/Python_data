import csv

# Define the CSV file name
filename = "products.csv"

# Adding some simple data to the csv file

data = [
    ["Product No", "Product", "Price"],
    ["1", "Apple", "0.99"],
    ["2", "Banana", "0.59"],
    ["3", "Orange", "0.79"]
]

# Create and write to the CSV file
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)   # write data rows

print(f"{filename} created successfully!")
