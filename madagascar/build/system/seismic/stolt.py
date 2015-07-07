sfstolt = rsf.doc.rsfprog('sfstolt','system/seismic/Mstolt.c','''Post-stack Stolt modeling/migration. ''')
sfstolt.par('vel',rsf.doc.rsfpar('float','','','''Constant velocity (use negative velocity for modeling) '''))
sfstolt.par('pad',rsf.doc.rsfpar('int','nt','','''padding on the time axis '''))
sfstolt.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sfstolt.par('mute',rsf.doc.rsfpar('int','12','','''mute zone '''))
sfstolt.par('minstr',rsf.doc.rsfpar('float','0.0','','''minimum stretch allowed '''))
sfstolt.par('stretch',rsf.doc.rsfpar('float','1','','''Stolt stretch parameter '''))
sfstolt.version('1.7')
sfstolt.synopsis('''sfstolt < in.rsf > out.rsf vel= pad=nt extend=4 mute=12 minstr=0.0 stretch=1''','''
Requires the input to be cosine-transformed over the lateral axes.

August 2014 program of the month:
http://ahay.org/rsflog/index.php?/archives/399-Program-of-the-month-sfstolt.html
''')
rsf.doc.progs['sfstolt']=sfstolt

