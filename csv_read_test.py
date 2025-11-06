# Open the CSV file for reading
filename = "products.csv"

with open(filename, mode="r") as file:
    for line in file:

        row = line.strip().split(",")
        print(row)
