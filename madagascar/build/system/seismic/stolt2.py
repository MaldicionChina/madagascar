sfstolt2 = rsf.doc.rsfprog('sfstolt2','system/seismic/Mstolt2.c','''Post-stack Stolt modeling/migration. ''')
sfstolt2.par('vel',rsf.doc.rsfpar('float','','','''Constant velocity (use negative velocity for modeling) '''))
sfstolt2.par('pad',rsf.doc.rsfpar('int','nt','','''padding on the time axis '''))
sfstolt2.par('nf',rsf.doc.rsfpar('int','2','','''Interpolation accuracy '''))
sfstolt2.version('1.7')
sfstolt2.synopsis('''sfstolt2 < in.rsf > out.rsf vel= pad=nt nf=2''','''
Requires the input to be cosine-transformed over the lateral axes.
''')
rsf.doc.progs['sfstolt2']=sfstolt2

