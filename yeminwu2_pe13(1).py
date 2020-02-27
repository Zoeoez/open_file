# first I define a function which can return acronym of a phrase.

def acro(input_phrase):
    words =input_phrase.split()
    acronym = ""
    for one_word_str in words :
        first_letter = one_word_str[0]
        acronym = acronym + first_letter
        acronym=acronym.upper()
    return acronym



infile = open('phrases.txt', 'r')
lines = infile.read()
infile.close()
lines=lines.split('\n')
print(lines)

outfile=open('result.txt','w')
for phrase in lines:
    res = ""
    res = res + acro(phrase)
    print(res,file=outfile)

outfile.close()
