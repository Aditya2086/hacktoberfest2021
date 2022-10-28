#Count the occurance of character

def char_occur(word):
  f = {}
  for i in word:
    if i in f:
      f[i] += 1
    else:
      f[i] = 1 # creating a dictionary key- value pair
  return f

a = input('Enter the word:')
char_occur(a)
