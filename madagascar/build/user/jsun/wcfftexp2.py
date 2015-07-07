sfwcfftexp2 = rsf.doc.rsfprog('sfwcfftexp2','user/jsun/Mwcfftexp2.c','''2-D FFT-based zero-offset exploding reflector modeling/migration  ''')
sfwcfftexp2.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwcfftexp2.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwcfftexp2.par('mig',rsf.doc.rsfpar('bool','n','','''if n, modeling; if y, migration '''))
sfwcfftexp2.par('timer',rsf.doc.rsfpar('bool','n','',''''''))
sfwcfftexp2.par('pad1',rsf.doc.rsfpar('int','1','','''padding factor on the first axis '''))
sfwcfftexp2.par('nz',rsf.doc.rsfpar('int','','','''depth samples (if migration) '''))
sfwcfftexp2.par('dz',rsf.doc.rsfpar('float','','','''depth sampling (if migration) '''))
sfwcfftexp2.par('nt',rsf.doc.rsfpar('int','','','''time samples (if modeling) '''))
sfwcfftexp2.par('dt',rsf.doc.rsfpar('float','','','''time sampling (if modeling) '''))
sfwcfftexp2.version('1.7')
sfwcfftexp2.synopsis('''sfwcfftexp2 < data.rsf > image.rsf left=left.rsf right=right.rsf mig=n timer=n pad1=1 nz= dz= nt= dt=''','''''')
rsf.doc.progs['sfwcfftexp2']=sfwcfftexp2

