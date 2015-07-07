sflphfreq = rsf.doc.rsfprog('sflphfreq','user/chen/Mlphfreq.c','''frequency response of linear phase approximators ''')
sflphfreq.par('m',rsf.doc.rsfpar('int','1','','''b[-m, ... ,n] '''))
sflphfreq.par('n',rsf.doc.rsfpar('int','1','','''b[-m, ... ,n] '''))
sflphfreq.par('iir',rsf.doc.rsfpar('bool','y','','''y:iir,  n:fir '''))
sflphfreq.par('n1',rsf.doc.rsfpar('int','50','','''samples in frequency domain between (0:f_c] '''))
sflphfreq.par('o2',rsf.doc.rsfpar('float','0.1','','''first phase shift '''))
sflphfreq.par('d2',rsf.doc.rsfpar('float','0.3','','''phase shift increment '''))
sflphfreq.par('n2',rsf.doc.rsfpar('int','1','','''number of phase shift '''))
sflphfreq.par('interp',rsf.doc.rsfpar('string ',desc='''interpolation method: maxflat lagrange bspline '''))
sflphfreq.version('1.7')
sflphfreq.synopsis('''sflphfreq > out.rsf m=1 n=1 iir=y n1=50 o2=0.1 d2=0.3 n2=1 interp=''','''''')
rsf.doc.progs['sflphfreq']=sflphfreq

