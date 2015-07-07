sfcshifts2 = rsf.doc.rsfprog('sfcshifts2','user/gchliu/Mcshifts2.c','''Generate shifts for 2-D regularized autoregression in complex domain. From (x,y,f) to (x,y,s,f) ''')
sfcshifts2.par('ns1',rsf.doc.rsfpar('int','','','''number of shifts in first dim '''))
sfcshifts2.par('ns2',rsf.doc.rsfpar('int','','','''number of shifts in second dim '''))
sfcshifts2.version('1.7')
sfcshifts2.synopsis('''sfcshifts2 < in.rsf > shifts.rsf ns1= ns2=''','''''')
rsf.doc.progs['sfcshifts2']=sfcshifts2

