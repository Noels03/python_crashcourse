#####for loop to print the tuple#####
#### a tuple  is like a list but can not be modified ####
buffets = ('watermelon', 'mixed vegetables', 'eggs', 'mashed potatoes', 'thai rice')
for buffet in buffets:
        print(buffet)

##### will reject item assignment#####
#buffets[0] = 'eggplant'

###### writes over the tuple and redefines the entire thing #####
buffets = ('watermelon', 'cake', 'potstickers', 'mashed potatoes', 'thai rice')
print("\nModified dimensions:")
for buffet in buffets:
    print(buffet)
