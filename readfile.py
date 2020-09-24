fname = input("Enter file name: ")
try :
    fhand = open(fname)
except:
    print('Cannot open the file ',fname ,'please try again')
    quit()

for a in fhand :
    a = a.upper()
    a = a.rstrip()
    print(a)
