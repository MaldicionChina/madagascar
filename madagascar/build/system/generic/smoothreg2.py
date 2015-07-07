sfsmoothreg2 = rsf.doc.rsfprog('sfsmoothreg2','system/generic/Msmoothreg2.c','''Smoothing in 2-D by simple regularization.''')
sfsmoothreg2.par('eps',rsf.doc.rsfpar('float','1.','','''smoothness parameter '''))
sfsmoothreg2.par('repeat',rsf.doc.rsfpar('int','1','','''repeat smoothing '''))
sfsmoothreg2.version('1.7')
sfsmoothreg2.synopsis('''sfsmoothreg2 < in.rsf > smooth.rsf eps=1. repeat=1''','''''')
rsf.doc.progs['sfsmoothreg2']=sfsmoothreg2

