sfshiftd2 = rsf.doc.rsfprog('sfshiftd2','user/gchliu/Mshiftd2.c','''Generate shifts for 1-D regularized autoregression double sides (include the trace self for 3D shifts). ''')
sfshiftd2.par('ns',rsf.doc.rsfpar('int','','','''number of shifts '''))
sfshiftd2.version('1.7')
sfshiftd2.synopsis('''sfshiftd2 < in.rsf > shift.rsf ns=''','''''')
rsf.doc.progs['sfshiftd2']=sfshiftd2

