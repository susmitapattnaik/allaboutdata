#Write a function that takes a number and returns cumulative sum of its digits
def calculate_sum_digit(input):
  newNumber = str(input)
  i = 0
  for j in newNumber:
    i = i+int(j)
   print(i)
  
  
