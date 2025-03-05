letters = ['a', 'b', 'c']
nums = [1, 2, 3]

new_letters = [i for i in letters]
dict = {i:j for (i, j) in zip(letters, nums)}

print(new_letters)
print(dict)