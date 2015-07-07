sfcanny = rsf.doc.rsfprog('sfcanny','system/generic/Mcanny.c','''Canny-like edge detector. ''')
sfcanny.par('min',rsf.doc.rsfpar('float','5.0','','''minimum threshold '''))
sfcanny.par('max',rsf.doc.rsfpar('float','95.0','','''maximum threshold '''))
sfcanny.version('1.7')
sfcanny.synopsis('''sfcanny < in.rsf > out.rsf min=5.0 max=95.0''','''''')
rsf.doc.progs['sfcanny']=sfcanny

