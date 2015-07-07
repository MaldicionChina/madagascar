import rsf.doc

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

sfcisolr2 = rsf.doc.rsfprog('sfcisolr2','user/jsun/Mcisolr2.cc','''Complex lowrank decomposition for 2-D isotropic wave propagation. ''')
sfcisolr2.par('fft',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcisolr2.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfcisolr2.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfcisolr2.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sfcisolr2.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfcisolr2.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sfcisolr2.par('os',rsf.doc.rsfpar('','true','',''''''))
sfcisolr2.par('sub',rsf.doc.rsfpar('','false','','''for onestep, default false'''))
sfcisolr2.par('sub',rsf.doc.rsfpar('','true','','''for twostep, default true'''))
sfcisolr2.par('lap',rsf.doc.rsfpar('','false','',''''''))
sfcisolr2.version('1.7')
sfcisolr2.synopsis('''sfcisolr2 < vel.rsf fft=fft.rsf left=left.rsf > right.rsf seed=time(NULL eps=1.e-4 npk=20 dt= os=true sub=false sub=true lap=false''','''''')
rsf.doc.progs['sfcisolr2']=sfcisolr2

