sfocor3d = rsf.doc.rsfprog('sfocor3d','user/psava/Mocor3d.py','''''')
sfocor3d.par('opr',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfocor3d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag'''))
sfocor3d.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag'''))
sfocor3d.par('ocox',rsf.doc.rsfpar('float','0.0','',''''''))
sfocor3d.par('ocoy',rsf.doc.rsfpar('float','0.0','',''''''))
sfocor3d.par('ocoz',rsf.doc.rsfpar('float','0.0','',''''''))
sfocor3d.par('ntlag',rsf.doc.rsfpar('int','100','',''''''))
sfocor3d.par('nxlag',rsf.doc.rsfpar('int','0','',''''''))
sfocor3d.par('nylag',rsf.doc.rsfpar('int','0','',''''''))
sfocor3d.par('nzlag',rsf.doc.rsfpar('int','0','',''''''))
sfocor3d.version('1.7')
sfocor3d.synopsis('''sfocor3d < Fwfl.rsf opr=Fopr.rsf > Fcor.rsf verb=n adj=n ocox=0.0 ocoy=0.0 ocoz=0.0 ntlag=100 nxlag=0 nylag=0 nzlag=0''','''Oriented correlation
wfl [file] : is taken from stdin
opr [file] : is taken from  "opr"
requires both files to have the same dimensions
correlation is computed at coordinates (ocox,ocoy,ocoz)
the (half) lags are: ntlag, nxlag, nylag, nzlag
''')
rsf.doc.progs['sfocor3d']=sfocor3d

