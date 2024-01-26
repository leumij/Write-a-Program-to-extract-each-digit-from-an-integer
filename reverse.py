# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

def reverse_num(intiger):
  new_string = ''
  new_num = str(intiger)
  for num in new_num:
    new_string += num+' '
  return new_string[::-1]

print(reverse_num(7536), end=" ")