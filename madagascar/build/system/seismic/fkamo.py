sffkamo = rsf.doc.rsfprog('sffkamo','system/seismic/Mfkamo.c','''Computes Azimuth Move-Out (AMO) operator in the f-k log-stretch domain ''')
sffkamo.par('h1',rsf.doc.rsfpar('float','','','''input offset '''))
sffkamo.par('h2',rsf.doc.rsfpar('float','','','''output offset '''))
sffkamo.par('f1',rsf.doc.rsfpar('float','','','''input azimuth in degrees '''))
sffkamo.par('f2',rsf.doc.rsfpar('float','','','''output azimuth in degrees '''))
sffkamo.par('maxe',rsf.doc.rsfpar('float','10.','','''stability constraint '''))
sffkamo.version('1.7')
sffkamo.synopsis('''sffkamo < in.rsf > out.rsf h1= h2= f1= f2= maxe=10.''','''''')
rsf.doc.progs['sffkamo']=sffkamo

