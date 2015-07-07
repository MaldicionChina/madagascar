sfiwarp3 = rsf.doc.rsfprog('sfiwarp3','system/seismic/Miwarp3.c','''Inverse 3-D warping ''')
sfiwarp3.par('warp',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfiwarp3.par('inv',rsf.doc.rsfpar('bool','y','','''inversion flag '''))
sfiwarp3.par('n1',rsf.doc.rsfpar('int','nt','',''''''))
sfiwarp3.par('n2',rsf.doc.rsfpar('int','ny','',''''''))
sfiwarp3.par('n3',rsf.doc.rsfpar('int','nx','','''output samples - for inv=y '''))
sfiwarp3.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfiwarp3.par('d1',rsf.doc.rsfpar('float','1','','''output sampling - for inv=y '''))
sfiwarp3.par('o1',rsf.doc.rsfpar('float','0','','''output origin - for inv=y '''))
sfiwarp3.version('1.7')
sfiwarp3.synopsis('''sfiwarp3 < in.rsf > out.rsf warp=warp.rsf inv=y n1=nt n2=ny n3=nx eps=0.01 d1=1 o1=0''','''''')
rsf.doc.progs['sfiwarp3']=sfiwarp3

