sfhist2 = rsf.doc.rsfprog('sfhist2','user/ivlad/Mhist2.c','''Compute a 2-D histogram of integer- or float-valued input data''')
sfhist2.par('inp2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfhist2.par('n1',rsf.doc.rsfpar('int','','','''number of histogram samples in dimension 1 '''))
sfhist2.par('o1',rsf.doc.rsfpar('float','','','''histogram origin for dimension 1 '''))
sfhist2.par('d1',rsf.doc.rsfpar('float','','','''histogram sampling for dimension 1 '''))
sfhist2.par('n2',rsf.doc.rsfpar('int','','','''number of histogram samples in dimension 2 '''))
sfhist2.par('o2',rsf.doc.rsfpar('float','','','''histogram origin for dimension 2 '''))
sfhist2.par('d2',rsf.doc.rsfpar('float','','','''histogram sampling for dimension 2 '''))
sfhist2.version('1.7')
sfhist2.synopsis('''sfhist2 < in.rsf inp2=inp2.rsf > out.rsf n1= o1= d1= n2= o2= d2=''','''The output grid is not centered on the bins; it marks their "left edge".
I.e., the first sample holds the number of values between o1 and o1+d1''')
rsf.doc.progs['sfhist2']=sfhist2

