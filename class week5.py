# there are roughly 3 tasks to take care of.

# 1) using the open() function, specifying the 'mode', creates the fileio object
# 2) you're going to act on that fileio object, using whichever read or write methods you want
# 3) you're going to close the file, by calling .close() on.
#           it will seem like this doesn't matter, but it really does.


# reading stuff first
# .read() reads the file as one large string

infile = open('small.txt', 'r')  # step 1 python know the file exists
text = infile.read()  # step 2
infile.close()  # step 3 close the file
print(text)

# .readlines()  reads the file as a list of lines which are strings store in a list
infile=open('small.txt','r') # step 1
lines=infile.readlines()
infile.close()
print(lines)

print(text.split('\n')) #
infile = open('small.txt','r')
for line in infile:
    print(line)
infile.close()

# not save the txt

#### writing outfiles


phrase="Hello humans,I would also like to be a human."


outfile=open('newfile.txt','w')
outfile.write(phrase)
outfile.close()


# 163 print pattern
outfile=open('newfilelines.txt','w')
print(phrase,file=outfile)
outfile.close()



lines=["hello human","I am certainly a human","want to play a game"]

outfile=open('newfilelines.txt','w')
for lines in lines:
    print(lines,file=outfile)
outfile.close()


## put all together


phrase='hello this text'
newphrase=""
for w in phrase.split():
    newphrase=newphrase+w.title()
#print(newphrase)



#
infile=open('small.txt','r')
lines=infile.readlines()
infile.close()
outfile=open('newphrases.txt','w')

for phrase in lines:
    newphrase = ""
    for w in phrase.split() :
        newphrase = newphrase + w.title()
    print(newphrase,file=outfile)

outfile.close()

infile=open('small.txt','r')
text=infile.read()
words=text.split()
infile.close
print(words)
