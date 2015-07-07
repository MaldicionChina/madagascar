sfiwarp2 = rsf.doc.rsfprog('sfiwarp2','system/seismic/Miwarp2.c','''Inverse 2-D warping ''')
sfiwarp2.par('warp',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfiwarp2.par('inv',rsf.doc.rsfpar('bool','y','','''inversion flag '''))
sfiwarp2.par('n1',rsf.doc.rsfpar('int','nt','',''''''))
sfiwarp2.par('n2',rsf.doc.rsfpar('int','nx','','''output samples - for inv=y '''))
sfiwarp2.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfiwarp2.par('d1',rsf.doc.rsfpar('int','1','','''output sampling - for inv=y '''))
sfiwarp2.par('o1',rsf.doc.rsfpar('float','0','','''output origin - for inv=y '''))
sfiwarp2.par('d2',rsf.doc.rsfpar('float','1','','''output sampling - for inv=y '''))
sfiwarp2.par('o2',rsf.doc.rsfpar('float','0','','''output origin - for inv=y '''))
sfiwarp2.version('1.7')
sfiwarp2.synopsis('''sfiwarp2 < in.rsf > out.rsf warp=warp.rsf inv=y n1=nt n2=nx eps=0.01 d1=1 o1=0 d2=1 o2=0''','''''')
rsf.doc.progs['sfiwarp2']=sfiwarp2

