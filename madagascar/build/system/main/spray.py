sfspray = rsf.doc.rsfprog('sfspray','system/main/spray.c','''Extend a dataset by duplicating in the specified axis dimension.''')
sfspray.par('axis',rsf.doc.rsfpar('int','2','','''which axis to spray '''))
sfspray.par('n',rsf.doc.rsfpar('int','','','''Size of the newly created dimension '''))
sfspray.par('d',rsf.doc.rsfpar('float','','','''Sampling of the newly created dimension '''))
sfspray.par('o',rsf.doc.rsfpar('float','','','''Origin of the newly created dimension '''))
sfspray.par('label',rsf.doc.rsfpar('string ',desc='''Label of the newly created dimension '''))
sfspray.par('unit',rsf.doc.rsfpar('string ',desc='''Units of the newly created dimension '''))
sfspray.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfspray')
sfspray.version('1.7 spray.c 7107 2011-04-10 02:04:14Z ivlad')
sfspray.synopsis('''sfspray < in.rsf > out.rsf axis=2 n= d= o= label= unit=''','''   This operation is adjoint to sfstack.
''')
rsf.doc.progs['sfspray']=sfspray

