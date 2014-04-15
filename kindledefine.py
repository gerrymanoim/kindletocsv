import sqlite3, csv, unicodedata, re
from subprocess import *

outputdata = []
conn = sqlite3.connect('vocab.db')

#get the data

for row in conn.execute('Select * From WORDS'):
	word = unicodedata.normalize('NFKD',row[1]).encode('ascii','ignore')
	definition = Popen(["automator","-D","Text="+word,"define.workflow"],stdout=PIPE).communicate()[0]
	#cleanup
	definition = re.sub('[()]', '', definition)
	outputdata.append([word, definition])

#write the data 

with open('output.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(outputdata)
