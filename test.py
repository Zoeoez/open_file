infile = open('phrases.txt', 'r')
lines = infile.read()
infile.close()
lines=lines.split('\n')
print(lines)

outfile=open('result2.txt','w')

for phrase in lines:
    res = 0
    res = res +len(phrase)
    print(res,file=outfile)

outfile.close()
