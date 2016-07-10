# This piece of code is going to clean up ugly displays and display comments you put up during debugging
import re
from sys import argv
filename = argv[1]
str= raw_input('Output keywords : ');
keyword_list = str.split()

#print keyword_list

file = open(filename,'r')

fileTxt =file.read()
code = re.split('(;|\n)',fileTxt)


for line_num,line in enumerate(code):

    delete= False       
    if (('cout' in line) or( 'print' in line )):
        delete = True
        for str in keyword_list:
            if str in line:
                delete = False
                break
            
    if(delete):
        code[line_num]=''
        code[line_num+1]='' #this wipes out the semi colon as well


fluffed_codeTxt = ''.join(code) # this is one huge string obtained after joining all the code lines

#________________ the following part removes the blank left out lines as well

file =open(filename,'w')
fluffed_code = re.split('\n',fluffed_codeTxt)
for line in fluffed_code:
    if(line.strip()) :
        file.write(line)
        file.write('\n')

file.close()
