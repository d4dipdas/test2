#Reading a text file
file = open("F:/Poem.txt","r")
for line in file:
  print(line, end="")
file.close()