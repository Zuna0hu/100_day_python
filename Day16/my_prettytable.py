from prettytable import PrettyTable

table = PrettyTable()

# add columns
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# change the alignment to left 
table.align = "l"
# in PrettyTable, the alignment setting is stored separately for each column rather than for the entire table
# if set table.align = "l" before adding any columns, there are no columns yet for the setting to apply to

print(table)