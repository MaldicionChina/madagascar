sfiwarp = rsf.doc.rsfprog('sfiwarp','system/seismic/Miwarp.c','''Inverse 1-D warping. ''')
sfiwarp.par('warp',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfiwarp.par('inv',rsf.doc.rsfpar('bool','y','','''inversion flag '''))
sfiwarp.par('n1',rsf.doc.rsfpar('int','nt','','''output samples - for inv=y '''))
sfiwarp.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfiwarp.par('d1',rsf.doc.rsfpar('float','1','','''output sampling - for inv=y '''))
sfiwarp.par('o1',rsf.doc.rsfpar('float','0','','''output origin - for inv=y '''))
sfiwarp.version('1.7')
sfiwarp.synopsis('''sfiwarp < in.rsf > out.rsf warp=warp.rsf inv=y n1=nt eps=0.01 d1=1 o1=0''','''
September 2012 program of the month:
http://ahay.org/rsflog/index.php?/archives/304-Program-of-the-month-sfiwarp.html
''')
rsf.doc.progs['sfiwarp']=sfiwarp

