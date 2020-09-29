fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
  #line=line.rstrip()
  words=line.split()
  for x in words:
    if x in lst:
      continue

    else:
       lst.append(x)
lst.sort()
print(line.rstrip())
