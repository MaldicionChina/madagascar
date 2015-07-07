sfcorop = rsf.doc.rsfprog('sfcorop','user/psava/Mcorop.py','''''')
sfcorop.par('opr',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcorop.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag'''))
sfcorop.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag'''))
sfcorop.par('ncor',rsf.doc.rsfpar('int','100','',''''''))
sfcorop.version('1.7')
sfcorop.synopsis('''sfcorop opr=Fopr.rsf < Fcor.rsf > Fwfl.rsf verb=n adj=n ncor=100''','''Correlation operator w/ adjoint
wfl [file] : is taken from stdin
opr [file] : is taken from  "opr"
Requires both files to have the same dimensions
''')
rsf.doc.progs['sfcorop']=sfcorop

