sfshift1 = rsf.doc.rsfprog('sfshift1','user/fomels/Mshift1.c','''Generate shifts for 1-D regularized autoregression. ''')
sfshift1.par('ns',rsf.doc.rsfpar('int','','','''number of shifts '''))
sfshift1.version('1.7')
sfshift1.synopsis('''sfshift1 < in.rsf > shift.rsf ns=''','''''')
rsf.doc.progs['sfshift1']=sfshift1

