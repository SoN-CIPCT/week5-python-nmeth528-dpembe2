#List Exercise
cats =  ['Siamese', 'Tabby', 'Maine Coon', 'Ragdoll', 'American Shorthair', 'Abyssinian']
print("cats")
first_two = cats[:2]
print(f"The first two items in the list are:", *first_two, sep=', ' )
list_length = len(cats)
middle_index = list_length // 2
middle_two_items = cats[middle_index - 1 : middle_index + 1]
print(f"The middle two items in the list are:", *middle_two_items, sep=', ')
print(f"The first and last items in the list are: {cats[0]}, {cats[-1]}")
#Tuple Exercise:
my_tuple = ('taco', 'mashed potatoes', 'beef stew', 'french toast','chef salad')
for item in my_tuple:
print(item)
