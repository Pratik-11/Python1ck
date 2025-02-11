#implement read csv from file

csv_file = """Name,Age,Department
Alice,30,HR
Bob,25,Engineering
Charlie,35,Marketing
Diana,28,Sales
"""
data = csv_file.split();
print(len(data))
columns = len(data[0].split(","));
# for(i in range(len(data)))
# for(eachrow in data)