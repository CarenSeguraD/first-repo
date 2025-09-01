dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT',
                'CAT', 'TAT', 'CCC', 'ACG', 'GAA', 'ACC', 'GGA']

item_to_find = "GAA"
item_found = False

for dna in dna_sequence:
    if dna == item_to_find:
        item_found = True
        break
if item_found == True:
    print("Item Found!")
else:
    print("Item Not Found!")
