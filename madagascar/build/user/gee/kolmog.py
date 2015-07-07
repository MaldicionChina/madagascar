sfkolmog = rsf.doc.rsfprog('sfkolmog','user/gee/Mkolmog.c','''Kolmogoroff spectral factorization. ''')
sfkolmog.par('spec',rsf.doc.rsfpar('bool','n','','''if y, the input is spectrum squared; n, time-domain signal '''))
sfkolmog.par('lag',rsf.doc.rsfpar('int','0','','''lag for asymmetric part '''))
sfkolmog.par('shift',rsf.doc.rsfpar('int','0','','''time shift '''))
sfkolmog.version('1.7 Mkolmog.c 10702 2013-07-25 21:37:48Z sfomel')
sfkolmog.synopsis('''sfkolmog < in.rsf > out.rsf spec=n lag=0 shift=0''','''''')
rsf.doc.progs['sfkolmog']=sfkolmog

