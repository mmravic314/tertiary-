### The following edits to chain A of 3ux4.pdb for Crick-helical paramaterization 
## 8/4/15 Marco Mravic DeGrado Lab UCSF      using PYTHON 2.7 interpreter (and ProDy package)

#inF = open( './3ux4a.pdb', 'rU') 
#inF = inF.readlines()
loopyList = ['22', '23', '24', '25','26','27', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '74', '75', '76', '98', '99', '100','101', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '162', '163', '164', '165', '166', '167', '168', '190' ,'191', '192', '193', '194', '195']

from prody import *
import numpy as np
inPdb = parsePDB('./3ux4a.pdb')
chainDict = {}
helices = [  np.arange(1,22), np.arange(28,49),  np.arange(77,98), np.arange(102,123), np.arange(141,162), np.arange(169,190) ]
chains = ['A', 'B', 'C', 'D', 'E', 'F']
for c,h in zip( chains, helices):
    for res in h: 
    	chainDict[str(res)] = c

for i in inPdb.iterResidues():
	if str( i.getResnum() ) not in loopyList: 
		i.setChids( chainDict[ str( i.getResnum() ) ] )
		print chainDict[str( i.getResnum() ) ], i

writePDB( './strip3UX4a.pdb', inPdb)

inF = open( './strip3UX4a.pdb', 'rU') 
inF = inF.readlines()
outF = open( './3UX4a.pdb', 'w') 
for i in inF:
	if i[:4] != 'ATOM': 
		continue
	if  i[22:26].strip() in loopyList:
		continue
	else:
		outF.write(i)
            #print i
import os
os.remove('./strip3UX4a.pdb')
