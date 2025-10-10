essential_spices = {'cardamon', 'ginger', 'cinnamon'}
optional_spices = {'cloves', 'ginger', 'black pepper'}

# Union of 2 sets
all_spices = essential_spices | optional_spices
print(f'All Spices: {all_spices}')

# gives the common between 2 sets
common_spices = essential_spices & optional_spices
print(f'Common Spices: {common_spices}')

# Printing the values that are only in essential and not in optional
only_in_essential = essential_spices - common_spices
print(f'only in essential: {only_in_essential}')
