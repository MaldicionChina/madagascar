sfmyradon2 = rsf.doc.rsfprog('sfmyradon2','user/pyang/Mmyradon2.c','''Linear/parabolic radon transform frequency domain implementation ''')
sfmyradon2.par('adj',rsf.doc.rsfpar('bool','y','','''if y, perform adjoint operation '''))
sfmyradon2.par('inv',rsf.doc.rsfpar('bool','n','','''if y, perform inverse operation '''))
sfmyradon2.par('np',rsf.doc.rsfpar('int','','','''number of p values (if adj=y) '''))
sfmyradon2.par('dp',rsf.doc.rsfpar('float','','','''p sampling (if adj=y) '''))
sfmyradon2.par('p0',rsf.doc.rsfpar('float','','','''p origin (if adj=y) '''))
sfmyradon2.par('niter',rsf.doc.rsfpar('int','100','','''number of CGLS iterations '''))
sfmyradon2.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization parameter '''))
sfmyradon2.par('nx',rsf.doc.rsfpar('int','','','''number of offsets (if adj=n) '''))
sfmyradon2.par('ox',rsf.doc.rsfpar('float','','','''x origin '''))
sfmyradon2.par('dx',rsf.doc.rsfpar('float','','','''sampling interval in x '''))
sfmyradon2.par('parab',rsf.doc.rsfpar('bool','n','','''if y, parabolic Radon transform '''))
sfmyradon2.par('x0',rsf.doc.rsfpar('float','1.','','''reference offset '''))
sfmyradon2.par('invmode',rsf.doc.rsfpar('string ',desc='''inverse method: 'ls' if least-squares; 'toeplitz' if use FFT '''))
sfmyradon2.version('1.7')
sfmyradon2.synopsis('''sfmyradon2 < in.rsf > out.rsf adj=y inv=n np= dp= p0= niter=100 eps=0.01 nx= ox= dx= parab=n x0=1. invmode=''','''Also referred to as high-resolution radon transform
Note: I borrowed a lot from /system/seismic/radon+Mradon.c. The distinction:
	I am using FFTW because I am inexperienced in invoking kiss_fft. 
''')
rsf.doc.progs['sfmyradon2']=sfmyradon2

