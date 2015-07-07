sfenvelope = rsf.doc.rsfprog('sfenvelope','system/seismic/Menvelope.c','''Compute data envelope or phase rotation. ''')
sfenvelope.par('order',rsf.doc.rsfpar('int','100','','''Hilbert transformer order '''))
sfenvelope.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) '''))
sfenvelope.par('hilb',rsf.doc.rsfpar('bool','n','','''if y, compute Hilbert transform '''))
sfenvelope.par('phase',rsf.doc.rsfpar('float','90.','','''phase shift (in degrees) to use with hilb=y '''))
sfenvelope.version('1.7 Menvelope.c 12370 2014-05-04 11:49:34Z sfomel')
sfenvelope.synopsis('''sfenvelope < in.rsf > out.rsf order=100 ref=1. hilb=n phase=90.''','''
November 2011 program of the month:
http://ahay.org/rsflog/index.php?/archives/274-Program-of-the-month-sfenvelope.html
''')
rsf.doc.progs['sfenvelope']=sfenvelope

