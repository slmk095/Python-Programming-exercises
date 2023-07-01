file_name = "word.txt"
f = open(file_name, 'r')
f3 = f.read().splitlines()
print(f3)
f3.sort()
print(f3)