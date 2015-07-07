import rsf.doc

sfcshifts2 = rsf.doc.rsfprog('sfcshifts2','user/gchliu/Mcshifts2.c','''Generate shifts for 2-D regularized autoregression in complex domain. From (x,y,f) to (x,y,s,f) ''')
sfcshifts2.par('ns1',rsf.doc.rsfpar('int','','','''number of shifts in first dim '''))
sfcshifts2.par('ns2',rsf.doc.rsfpar('int','','','''number of shifts in second dim '''))
sfcshifts2.version('1.7')
sfcshifts2.synopsis('''sfcshifts2 < in.rsf > shifts.rsf ns1= ns2=''','''''')
rsf.doc.progs['sfcshifts2']=sfcshifts2

sfshiftd1 = rsf.doc.rsfprog('sfshiftd1','user/gchliu/Mshiftd1.c','''Generate shifts for 1-D regularized autoregression double sides (not include the trace self). ''')
sfshiftd1.par('ns',rsf.doc.rsfpar('int','','','''number of shifts '''))
sfshiftd1.version('1.7')
sfshiftd1.synopsis('''sfshiftd1 < in.rsf > shift.rsf ns=''','''''')
rsf.doc.progs['sfshiftd1']=sfshiftd1

sfshiftd2 = rsf.doc.rsfprog('sfshiftd2','user/gchliu/Mshiftd2.c','''Generate shifts for 1-D regularized autoregression double sides (include the trace self for 3D shifts). ''')
sfshiftd2.par('ns',rsf.doc.rsfpar('int','','','''number of shifts '''))
sfshiftd2.version('1.7')
sfshiftd2.synopsis('''sfshiftd2 < in.rsf > shift.rsf ns=''','''''')
rsf.doc.progs['sfshiftd2']=sfshiftd2

sfsmstack = rsf.doc.rsfprog('sfsmstack','user/gchliu/Msmstack.c','''Stack a dataset over the second dimensions by smart stacking. ''')
sfsmstack.par('s',rsf.doc.rsfpar('int','1','','''exponent'''))
sfsmstack.par('l',rsf.doc.rsfpar('int','0','','''parameter for alpha-trimmed mean '''))
sfsmstack.par('ifwt',rsf.doc.rsfpar('bool','y','',''''''))
sfsmstack.par('esp',rsf.doc.rsfpar('float','1e-10','',''''''))
sfsmstack.version('1.7')
sfsmstack.synopsis('''sfsmstack < in.rsf > out.rsf s=1 l=0 ifwt=y esp=1e-10''','''''')
rsf.doc.progs['sfsmstack']=sfsmstack

sfsnrstack = rsf.doc.rsfprog('sfsnrstack','user/gchliu/Msnrstack.c','''Stack a dataset over the second dimensions by SNR weighted method. ''')
sfsnrstack.par('w',rsf.doc.rsfpar('int','50','','''sliding window size'''))
sfsnrstack.par('sft',rsf.doc.rsfpar('float','1','','''weight shift'''))
sfsnrstack.par('ee',rsf.doc.rsfpar('float','1.0','',''''''))
sfsnrstack.par('esp',rsf.doc.rsfpar('float','1.0','',''''''))
sfsnrstack.version('1.7')
sfsnrstack.synopsis('''sfsnrstack < in.rsf > out.rsf w=50 sft=1 ee=1.0 esp=1.0''','''''')
rsf.doc.progs['sfsnrstack']=sfsnrstack

sfwcorr = rsf.doc.rsfprog('sfwcorr','user/gchliu/Mwcorr.c','''Stack a dataset over the second dimensions by SNR weighted method. ''')
sfwcorr.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwcorr.par('w',rsf.doc.rsfpar('int','50','','''size of window'''))
sfwcorr.par('eps',rsf.doc.rsfpar('float','0','','''stable parameter'''))
sfwcorr.version('1.7')
sfwcorr.synopsis('''sfwcorr < in.rsf other=other.rsf > out.rsf w=50 eps=0''','''''')
rsf.doc.progs['sfwcorr']=sfwcorr

