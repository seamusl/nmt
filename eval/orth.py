
#same as orth.py but altered by ailbhe gill and is used for post editing on a corpus to replace 
#a string in list1 with a correspongding string in list2 when appropriate
#eg. if a sentence contains 'tríd an geata' it is changed to 'tríd an gheata'
#****I haven't tested the program yet so I don't know if it works at all
#****This version of the program was intended to run faster than the previous version


# -*-coding: utf-8 -*-  

import fileinput
import re
import sys

filename = sys.argv[1]
infile = open(filename)

data=infile.read()
infile.seek(0)

outfile = open(filename+".orth", "w")

counter = 0

#PREP + PRONOUN
list1 = ['ag','ar','as','chuig','de','do','faoi','i','le','ó','roimh','thar','tríd','um','idir']
list2 = ['muid', 'sinn', 'sibh', 'iad', 'mé', 'tú', 'é', 'í']
matrix = [['againn','againn','agaibh','acu','agam', 'agat','aige','aici'],['orainn','orainn','oraibh','orthu','orm', 'ort','ar','uirthi'],['asainn','asainn','asaibh','astu','asam', 'asat','as','aisti'],['chugainn','chugainn','chugaibh','chucu','chugam', 'chugat','chuige','chuici'],['dínn','dínn','díbh','díobh','díom','díot','de','di'],['dúinn','dúinn','daoibh','dóibh','dom','duit','dó','di'],['fúinn','fúinn','fúibh','fúthu','fúm','fút','faoi','fúithi'],['ionainn','ionainn','ionaibh','iontu','ionam','ionat','ann','inti'],['linn','linn','libh','leo','liom','leat','leis','leí'],['uainn','uainn','uaibh','uathu','uaim','uait','uaidh','uathi'],['romhainn','romhainn','romhaibh','rompu','romham','romhat','roimhe','roimpi'],['tharainn','tharainn','tharaibh','tharstu','tharam','tharat','thairis','thairsti'],['trínn','trínn','tríibh','tríothu','tríom','tríot','tríd','tríthi'],['uamainn', 'uamainn','uamaibh','umpu','umam','umat','uime','uimpi'],['eadrainn','eadrainn','eadraibh','eatarthu']]

#ag/ar/as/chuig/de/do/faoi/i/le/Ó/roimh/thar/TRÍD/um/idir 
regex = re.compile(' ((ag|ar|as|chuig|de|do|faoi|i|le|ó|roimh|thar|tríd|um) (mé|tú|é|í|muid|sinn|sibh|iad)) | idir (muid|sinn|sibh|iad) ')

findAllList = re.findall(regex,data)
findAllList = list(set(findAllList))

newList = list(map((lambda x:(' '+ matrix[list1.index(x.split()[0])][list2.index(x.split()[1])] +' '),findAllList))

#check each line in the file for angle brackets
for match in findAllList:
	newData = data.replace(match,newList[counter])
	data = newData
	counter += 1

#PREP + DEF ARTICLE
regex1 = re.compile(' ((de|do|faoi|ó) (a|A)n) | (i t-)')
findAllList1 = re.findall(regex1,data)
findAllList1 = list(set(findAllList1))

newList1 = list(map((lambda x:(' ' +x.split()[0]+'n '),findAllList1))

counter = 0
for match in findAllList1:
	newData = data.replace(match,newList1[counter])
	data = newData
	counter += 1

regex2 = re.compile(' ((sa|i) (a|e|i|o|u|á|é|í|ó|ú|A|E|I|O|U|Á|É|Í|Ó|Ú))')
findAllList2 = re.findall(regex2,data)
findAllList2 = list(set(findAllList2))

newList2 = list(map((lambda x:(' '+ x.split()[0]+'n '+ x.split()[-1]),findAllList2))

counter = 0
for match in findAllList2:
	newData = data.replace(match,newList2[counter])
	data = newData
	counter += 1

    
#PREP + Possesive Pronoun

regex3 = re.compile(' (le|na) (a|e|i|o|u|á|é|í|ó|ú|A|E|I|O|U|Á|É|Í|Ó|Ú)')
findAllList3 = re.findall(regex3,data)
findAllList3 = list(set(findAllList3))

newList3 = list(map((lambda x:(' '+x.split()[0]+ ' h' + x.split()[-1]),findAllList3))

counter = 0
for match in findAllList3:
	newData = data.replace(match,newList3[counter])
	data = newData
	counter += 1


regex4 = re.compile(' (le|faoi|i|ó|trí) (a|ár) ')
findAllList4 = re.findall(regex4,data)
findAllList4 = list(set(findAllList4))

newList4 = list(map((lambda x:(' '+ x[1:-1].replace(' ','n')+' '),findAllList4))

counter = 0
for match in findAllList4:
	newData = data.replace(match,newList4[counter])
	data = newData
	counter += 1


#DE/DO
    data = re.sub(' d(e|o) a ', ' dá ', data.rstrip())
    data = re.sub(' d(e|o) ár ', ' dár ', data.rstrip())

#exception
    data = re.sub(' trí an ', ' tríd an ', data.rstrip())
    data = re.sub(' trí An ', ' tríd An ', data.rstrip())
    data = re.sub(' le an ',' leis an ', data.rstrip())
    data = re.sub(' le An ',' leis An ', data.rstrip())
    data = re.sub(' i (a|A)n ',' sa ', data.rstrip())
    data = re.sub(' i (n|N)a ',' sna ', data.rstrip())
    data = re.sub(' sa f(hh)?',' san fh', data.rstrip())

    #exceptions
    data = re.sub(' leis An Post ',' le An Post ', data.rstrip())
    data = re.sub(' ón Post ', ' ó An Post ', data.rstrip())
    data = re.sub(' le hos ', ' le os ', data.rstrip())
    data = re.sub(' le hi ', ' le i ', data.rstrip())
    data = re.sub(' le há ', ' le á ', data.rstrip())
    data = re.sub(' le hag ', ' le ag ', data.rstrip())
    data = re.sub(' le hAn Post ', ' le An Post ', data.rstrip())
    
    outfile.write(data)

