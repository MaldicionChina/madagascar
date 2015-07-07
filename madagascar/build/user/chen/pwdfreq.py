sfpwdfreq = rsf.doc.rsfprog('sfpwdfreq','user/chen/Mpwdfreq.c','''frequency response of PWD operator ''')
sfpwdfreq.par('n1',rsf.doc.rsfpar('int','50','','''samples in frequency domain between (0:f_c] '''))
sfpwdfreq.par('order',rsf.doc.rsfpar('int','1','','''order of PWD '''))
sfpwdfreq.par('o3',rsf.doc.rsfpar('float','20','','''first dip angle '''))
sfpwdfreq.par('d3',rsf.doc.rsfpar('float','30','','''dip angle increment '''))
sfpwdfreq.par('n3',rsf.doc.rsfpar('int','1','','''number dip angle '''))
sfpwdfreq.par('iir',rsf.doc.rsfpar('bool','n','','''y: iir; n: fir '''))
sfpwdfreq.par('opwd',rsf.doc.rsfpar('bool','y','','''y: circle interpolating pwd; n: line interpolating pwd '''))
sfpwdfreq.par('radius',rsf.doc.rsfpar('float','1.0','','''radius for circle interpolating pwd '''))
sfpwdfreq.par('interp',rsf.doc.rsfpar('string ',desc='''interpolation method: maxflat lagrange bspline '''))
sfpwdfreq.version('1.7')
sfpwdfreq.synopsis('''sfpwdfreq > out.rsf n1=50 order=1 o3=20 d3=30 n3=1 iir=n opwd=y radius=1.0 interp=''','''''')
rsf.doc.progs['sfpwdfreq']=sfpwdfreq

