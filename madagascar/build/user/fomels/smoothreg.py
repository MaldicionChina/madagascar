sfsmoothreg = rsf.doc.rsfprog('sfsmoothreg','user/fomels/Msmoothreg.c','''Smoothing in 1-D by simple regularization.''')
sfsmoothreg.par('eps',rsf.doc.rsfpar('float','1.','','''smoothness parameter '''))
sfsmoothreg.par('repeat',rsf.doc.rsfpar('int','1','','''repeat smoothing '''))
sfsmoothreg.version('1.7 Msmoothreg.c 7107 2011-04-10 02:04:14Z ivlad')
sfsmoothreg.synopsis('''sfsmoothreg < in.rsf > smooth.rsf eps=1. repeat=1''','''''')
rsf.doc.progs['sfsmoothreg']=sfsmoothreg

