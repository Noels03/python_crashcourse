
#####prints numbers in given range#####

#for value in range(1, 21):
    #print(value)


#####will get min/max of LIST)
#numbers = list(range(1, 1000001))

#print(numbers)
#print(min(numbers))
#print(max(numbers))
#print(sum(numbers))

#####using a for loop to print numbers#####
##for value in range(1, 100000):
  ##  print(value)

#####prints odd numbers from 1-20#####

##odd_numbers = list(range(1, 20, 2))
##print(odd_numbers)

####list of multiples of 3 from 3 to 30#####
#multiples_three = list(range(3, 31, 3))
#print(multiples_three)

#####cubes power#####
cubes = [value**3 for value in range(1, 11)]
print(cubes)

#####prints first 3 items on a list#####
print("\nThe first three items in the list are:")
print(cubes[0:3])