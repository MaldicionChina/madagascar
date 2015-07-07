sfshiftd1 = rsf.doc.rsfprog('sfshiftd1','user/gchliu/Mshiftd1.c','''Generate shifts for 1-D regularized autoregression double sides (not include the trace self). ''')
sfshiftd1.par('ns',rsf.doc.rsfpar('int','','','''number of shifts '''))
sfshiftd1.version('1.7')
sfshiftd1.synopsis('''sfshiftd1 < in.rsf > shift.rsf ns=''','''''')
rsf.doc.progs['sfshiftd1']=sfshiftd1

