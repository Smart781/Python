from generator import table_generator
table = [
    ["Name", "Age", "City"],
    ["Ivan", "25", "Moscow"],
    ["Andrew", "33", "Saint-Petersburg"],
    ["Ilya", "38", "Orenburg"]
]

with open("table.tex", "w") as file:
    file.write(table_generator(table))
