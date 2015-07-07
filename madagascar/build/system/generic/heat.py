sfheat = rsf.doc.rsfprog('sfheat','system/generic/Mheat.c','''Finite-difference solution of 2-D heat-flow equation ''')
sfheat.par('impl',rsf.doc.rsfpar('bool','n','','''if y, use implicit scheme '''))
sfheat.par('alpha',rsf.doc.rsfpar('float','1.','',''''''))
sfheat.version('1.7')
sfheat.synopsis('''sfheat > out.rsf impl=n alpha=1.''','''''')
rsf.doc.progs['sfheat']=sfheat

