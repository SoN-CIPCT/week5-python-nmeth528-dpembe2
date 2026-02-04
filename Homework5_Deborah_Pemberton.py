#List Exercise
cats =  ['Siamese', 'Tabby', 'Maine Coon', 'Ragdoll', 'American Shorthair', 'Abyssinian']
print(*cats, sep = ", ")
first_two = cats[:2]
print(f"The first two items in the list are: " + ", ".join(first_two)) 
list_length = len(cats)
middle_index = list_length // 2
middle_two_items = cats[middle_index - 1 : middle_index + 1]
print(f"The middle two items in the list are: " + ", ".join(middle_two_items)) 
print(f"The first and last items in the list are: {cats[0]}, {cats[-1]}")
#Tuple Exercise:
my_tuple = ('taco', 'mashed potatoes', 'beef stew', 'french toast','chef salad')
for item in my_tuple:
   print(f"Original Menu Item:", item)
copied_tuple = tuple(my_tuple)
temporary_list = list(copied_tuple)
temporary_list[0] = "french fries"
temporary_list[3] = "apple pie"
copied_tuple = tuple(temporary_list)
for item in copied_tuple:
      print(f"Revised Menu Item:", item)
