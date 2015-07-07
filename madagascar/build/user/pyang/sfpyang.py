import rsf.doc

sfdlct = rsf.doc.rsfprog('sfdlct','user/pyang/Mdlct.c','''discrete linear chirp transfrom (DLCT)''')
sfdlct.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform (Here adjoint is the same as inverse!) '''))
sfdlct.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfdlct.par('C',rsf.doc.rsfpar('float','0.005','','''C=2*Lambda/L, unit slice '''))
sfdlct.par('L',rsf.doc.rsfpar('int','','',''''''))
sfdlct.version('1.7')
sfdlct.synopsis('''sfdlct < in.rsf > out.rsf inv=n verb=n C=0.005 L=''',''' ''')
rsf.doc.progs['sfdlct']=sfdlct

sffpocs2d = rsf.doc.rsfprog('sffpocs2d','user/pyang/Mfpocs2d.c','''2-D Two-step POCS interpolation using a general Lp-norm optimization''')
sffpocs2d.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffpocs2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sffpocs2d.par('niter',rsf.doc.rsfpar('int','100','','''total number iterations '''))
sffpocs2d.par('tol',rsf.doc.rsfpar('float','1.0e-6','','''iteration tolerance '''))
sffpocs2d.par('pclip',rsf.doc.rsfpar('float','99.','','''starting data clip percentile (default is 99)'''))
sffpocs2d.par('p',rsf.doc.rsfpar('float','0.35','','''norm=p, where 0<p<=1 '''))
sffpocs2d.par('mode',rsf.doc.rsfpar('string ',desc='''thresholding mode: 'hard', 'soft','pthresh','exp';
	'hard', hard thresholding;	'soft', soft thresholding; 
	'pthresh', generalized quasi-p; 'exp', exponential shrinkage '''))
sffpocs2d.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sffpocs2d.version('1.7')
sffpocs2d.synopsis('''sffpocs2d < Fin.rsf mask=Fmask.rsf > Fout.rsf verb=n niter=100 tol=1.0e-6 pclip=99. p=0.35 mode=''','''''')
rsf.doc.progs['sffpocs2d']=sffpocs2d

sffpocs3d = rsf.doc.rsfprog('sffpocs3d','user/pyang/Mfpocs3d.c','''3-D Two-step POCS interpolation using a general Lp-norm optimization''')
sffpocs3d.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffpocs3d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sffpocs3d.par('niter',rsf.doc.rsfpar('int','100','','''total number iterations '''))
sffpocs3d.par('tol',rsf.doc.rsfpar('float','1.0e-6','','''iteration tolerance '''))
sffpocs3d.par('pclip',rsf.doc.rsfpar('float','99.','','''starting data clip percentile (default is 99)'''))
sffpocs3d.par('p',rsf.doc.rsfpar('float','0.35','','''norm=p, where 0<p<=1 '''))
sffpocs3d.par('mode',rsf.doc.rsfpar('string ',desc='''thresholding mode: 'hard', 'soft','pthresh','exp';
	'hard', hard thresholding;	'soft', soft thresholding; 
	'pthresh', generalized quasi-p; 'exp', exponential shrinkage '''))
sffpocs3d.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sffpocs3d.version('1.7')
sffpocs3d.synopsis('''sffpocs3d < Fin.rsf mask=Fmask.rsf > Fout.rsf verb=n niter=100 tol=1.0e-6 pclip=99. p=0.35 mode=''','''''')
rsf.doc.progs['sffpocs3d']=sffpocs3d

sfistseislet = rsf.doc.rsfprog('sfistseislet','user/pyang/Mistseislet.c','''Analysis-based IST interpolation using seislet (2d validation)''')
sfistseislet.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfistseislet.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfistseislet.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfistseislet.par('order',rsf.doc.rsfpar('int','1','','''accuracy order for seislet transform'''))
sfistseislet.par('pscale',rsf.doc.rsfpar('float','25','','''percentile of small scale to be preserved (default is 25)'''))
sfistseislet.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfistseislet.par('niter',rsf.doc.rsfpar('int','10','','''total number iterations '''))
sfistseislet.par('pclip',rsf.doc.rsfpar('float','99','','''starting data clip percentile (default is 99)'''))
sfistseislet.par('p',rsf.doc.rsfpar('float','0.35','','''norm=p, where 0<p<=1 '''))
sfistseislet.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sfistseislet.par('mode',rsf.doc.rsfpar('string ',desc='''thresholding mode: 'hard', 'soft','pthresh','exp';
	'hard', hard thresholding;	'soft', soft thresholding; 
	'pthresh', generalized quasi-p; 'exp', exponential shrinkage '''))
sfistseislet.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfistseislet.version('1.7')
sfistseislet.synopsis('''sfistseislet < Fin.rsf mask=Fmask.rsf > Fout.rsf dip=Fdip.rsf eps=0.01 order=1 pscale=25 verb=n niter=10 pclip=99 p=0.35 type= mode=''','''IST=iterative shrinkage-thresholding
''')
rsf.doc.progs['sfistseislet']=sfistseislet

sflsinterp2d = rsf.doc.rsfprog('sflsinterp2d','user/pyang/Mlsinterp2d.c','''Least-squares interpolation for 2D validition''')
sflsinterp2d.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflsinterp2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sflsinterp2d.par('niter',rsf.doc.rsfpar('int','100','','''inner iterations '''))
sflsinterp2d.par('nouter',rsf.doc.rsfpar('int','5','','''outer iterations '''))
sflsinterp2d.par('eps',rsf.doc.rsfpar('float','1.e-2','','''regularization parameter '''))
sflsinterp2d.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sflsinterp2d.version('1.7')
sflsinterp2d.synopsis('''sflsinterp2d < Fin.rsf mask=Fmask.rsf > Fout.rsf verb=n niter=100 nouter=5 eps=1.e-2''','''''')
rsf.doc.progs['sflsinterp2d']=sflsinterp2d

sflsprtm2d = rsf.doc.rsfprog('sflsprtm2d','user/pyang/Mlsprtm2d.c','''2-D prestack least-squares RTM using wavefield reconstruction''')
sflsprtm2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflsprtm2d.par('imgrtm',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sflsprtm2d.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sflsprtm2d.par('niter',rsf.doc.rsfpar('int','10','','''totol number of least-squares iteration'''))
sflsprtm2d.par('nb',rsf.doc.rsfpar('int','20','','''number (thickness) of ABC on each side '''))
sflsprtm2d.version('1.7')
sflsprtm2d.synopsis('''sflsprtm2d < shots.rsf vel=velo.rsf > imag.rsf imgrtm=imgrtm.rsf verb=y niter=10 nb=20''','''NB: Sponge ABC is applied!
''')
rsf.doc.progs['sflsprtm2d']=sflsprtm2d

sflsrtm2d = rsf.doc.rsfprog('sflsrtm2d','user/pyang/Mlsrtm2d.c','''2-D zero-offset least-squares reverse time migration (LSRTM)''')
sflsrtm2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflsrtm2d.par('n0',rsf.doc.rsfpar('int','0','','''shot depth in the grid '''))
sflsrtm2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sflsrtm2d.par('niter',rsf.doc.rsfpar('int','10','','''totol number of least-squares iteration'''))
sflsrtm2d.par('tol',rsf.doc.rsfpar('float','1.e-12','','''tolerance of inversion '''))
sflsrtm2d.version('1.7')
sflsrtm2d.synopsis('''sflsrtm2d < data.rsf > imag.rsf vel=modl.rsf n0=0 verb=n niter=10 tol=1.e-12''','''''')
rsf.doc.progs['sflsrtm2d']=sflsrtm2d

sfmcaseislet = rsf.doc.rsfprog('sfmcaseislet','user/pyang/Mmcaseislet.c','''Morphological component analysis using 2-D Seislet transform ''')
sfmcaseislet.par('dips',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmcaseislet.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmcaseislet.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfmcaseislet.par('order',rsf.doc.rsfpar('int','1','','''accuracy order for seislet transform'''))
sfmcaseislet.par('pscale',rsf.doc.rsfpar('float','25','','''percentile of small scale to be preserved (default is 100)'''))
sfmcaseislet.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity or not '''))
sfmcaseislet.par('decr',rsf.doc.rsfpar('bool','y','','''decrease threshold in iterations or not '''))
sfmcaseislet.par('niter',rsf.doc.rsfpar('int','10','','''total number iterations '''))
sfmcaseislet.par('pclip',rsf.doc.rsfpar('float','10','','''starting data clip percentile (default is 10)'''))
sfmcaseislet.par('p',rsf.doc.rsfpar('float','0.5','','''norm=p, where 0<p<=1 '''))
sfmcaseislet.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sfmcaseislet.par('mode',rsf.doc.rsfpar('string ',desc='''thresholding mode: 'hard', 'soft','pthresh','exp';
	'hard', hard thresholding;	'soft', soft thresholding; 
	'pthresh', generalized quasi-p; 'exp', exponential shrinkage '''))
sfmcaseislet.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfmcaseislet.version('1.7')
sfmcaseislet.synopsis('''sfmcaseislet < Fin.rsf > Fout.rsf dips=Fdips.rsf mask=Fmask.rsf eps=0.01 order=1 pscale=25 verb=n decr=y niter=10 pclip=10 p=0.5 type= mode=''','''Note:  Here, nc components with nc seislet transforms build a seislet 
 frame to do the simultineous multicomponent separation and interpolation.	
''')
rsf.doc.progs['sfmcaseislet']=sfmcaseislet

sfmodeling2d = rsf.doc.rsfprog('sfmodeling2d','user/pyang/Mmodeling2d.c','''2-D forward modeling to generate shot records ''')
sfmodeling2d.par('time',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmodeling2d.par('check',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmodeling2d.par('chk',rsf.doc.rsfpar('bool','','',''''''))
sfmodeling2d.par('kt',rsf.doc.rsfpar('int','100','','''check it at it=100 '''))
sfmodeling2d.par('amp',rsf.doc.rsfpar('float','1000','','''maximum amplitude of ricker '''))
sfmodeling2d.par('fm',rsf.doc.rsfpar('float','10','','''dominant freq of ricker '''))
sfmodeling2d.par('dt',rsf.doc.rsfpar('float','','','''time interval '''))
sfmodeling2d.par('nt',rsf.doc.rsfpar('int','','','''total modeling time steps '''))
sfmodeling2d.par('ns',rsf.doc.rsfpar('int','','','''total shots '''))
sfmodeling2d.par('ng',rsf.doc.rsfpar('int','','','''total receivers in each shot '''))
sfmodeling2d.par('jsx',rsf.doc.rsfpar('int','','','''source x-axis  jump interval  '''))
sfmodeling2d.par('jsz',rsf.doc.rsfpar('int','0','','''source z-axis jump interval  '''))
sfmodeling2d.par('jgx',rsf.doc.rsfpar('int','1','','''receiver x-axis jump interval '''))
sfmodeling2d.par('jgz',rsf.doc.rsfpar('int','0','','''receiver z-axis jump interval '''))
sfmodeling2d.par('sxbeg',rsf.doc.rsfpar('int','','','''x-begining index of sources, starting from 0 '''))
sfmodeling2d.par('szbeg',rsf.doc.rsfpar('int','','','''z-begining index of sources, starting from 0 '''))
sfmodeling2d.par('gxbeg',rsf.doc.rsfpar('int','','','''x-begining index of receivers, starting from 0 '''))
sfmodeling2d.par('gzbeg',rsf.doc.rsfpar('int','','','''z-begining index of receivers, starting from 0 '''))
sfmodeling2d.par('csdgather',rsf.doc.rsfpar('bool','n','','''default, common shot-gather; if n, record at every point'''))
sfmodeling2d.version('1.7')
sfmodeling2d.synopsis('''sfmodeling2d < vinit.rsf > shots.rsf time=time.rsf check=check.rsf chk= kt=100 amp=1000 fm=10 dt= nt= ns= ng= jsx= jsz=0 jgx=1 jgz=0 sxbeg= szbeg= gxbeg= gzbeg= csdgather=n''','''Note: Clayton-Enquist absorbing boundary condition (A2) is applied!
 ''')
rsf.doc.progs['sfmodeling2d']=sfmodeling2d

sfmshots = rsf.doc.rsfprog('sfmshots','user/pyang/Mmshots.c','''2-D prestack forward modeling using sponge ABC using 4-th order FD''')
sfmshots.par('amp',rsf.doc.rsfpar('float','1000','','''maximum amplitude of ricker '''))
sfmshots.par('fm',rsf.doc.rsfpar('float','10','','''dominant freq of ricker '''))
sfmshots.par('nb',rsf.doc.rsfpar('int','30','','''thickness of sponge ABC  '''))
sfmshots.par('dt',rsf.doc.rsfpar('float','','','''time interval '''))
sfmshots.par('nt',rsf.doc.rsfpar('int','','','''total modeling time steps '''))
sfmshots.par('ns',rsf.doc.rsfpar('int','','','''total shots '''))
sfmshots.par('ng',rsf.doc.rsfpar('int','','','''total receivers in each shot '''))
sfmshots.par('jsx',rsf.doc.rsfpar('int','','','''source x-axis  jump interval  '''))
sfmshots.par('jsz',rsf.doc.rsfpar('int','0','','''source z-axis jump interval  '''))
sfmshots.par('jgx',rsf.doc.rsfpar('int','1','','''receiver x-axis jump interval '''))
sfmshots.par('jgz',rsf.doc.rsfpar('int','0','','''receiver z-axis jump interval '''))
sfmshots.par('sxbeg',rsf.doc.rsfpar('int','','','''x-begining index of sources, starting from 0 '''))
sfmshots.par('szbeg',rsf.doc.rsfpar('int','','','''z-begining index of sources, starting from 0 '''))
sfmshots.par('gxbeg',rsf.doc.rsfpar('int','','','''x-begining index of receivers, starting from 0 '''))
sfmshots.par('gzbeg',rsf.doc.rsfpar('int','','','''z-begining index of receivers, starting from 0 '''))
sfmshots.par('csdgather',rsf.doc.rsfpar('bool','n','','''default, common shot-gather; if n, record at every point'''))
sfmshots.version('1.7')
sfmshots.synopsis('''sfmshots < vinit.rsf > shots.rsf amp=1000 fm=10 nb=30 dt= nt= ns= ng= jsx= jsz=0 jgx=1 jgz=0 sxbeg= szbeg= gxbeg= gzbeg= csdgather=n''','''NB: prepare high quality prestack seismic data for LSRTM and FWI
Top boundary is free surface (no ABC applied)!
 ''')
rsf.doc.progs['sfmshots']=sfmshots

sfmwni2d = rsf.doc.rsfprog('sfmwni2d','user/pyang/Mmwni2d.c','''2-D bandlimited minimum weighted-norm interpolation (MWNI) ''')
sfmwni2d.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmwni2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfmwni2d.par('niter',rsf.doc.rsfpar('int','100','','''total number iterations '''))
sfmwni2d.par('tol',rsf.doc.rsfpar('float','1.0e-6','','''iteration tolerance '''))
sfmwni2d.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfmwni2d.version('1.7')
sfmwni2d.synopsis('''sfmwni2d < Fin.rsf mask=Fmask.rsf > Fout.rsf verb=n niter=100 tol=1.0e-6''',''' implemented with conjugate gradient least squares (CGLS) method
''')
rsf.doc.progs['sfmwni2d']=sfmwni2d

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

sfmysnr = rsf.doc.rsfprog('sfmysnr','user/pyang/Mmysnr.c','''print out signal-to-noise ratio in decibel (dB)''')
sfmysnr.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmysnr.version('1.7')
sfmysnr.synopsis('''sfmysnr < in.rsf ref=ref.rsf > out.rsf''','''''')
rsf.doc.progs['sfmysnr']=sfmysnr

sfpocs = rsf.doc.rsfprog('sfpocs','user/pyang/Mpocs.c','''n-D POCS interpolation using a hard thresholding''')
sfpocs.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpocs.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfpocs.par('niter',rsf.doc.rsfpar('int','100','','''total number iterations '''))
sfpocs.par('pclip',rsf.doc.rsfpar('float','10.','','''starting data clip percentile (default is 99)'''))
sfpocs.par('n#',rsf.doc.rsfpar('int','','','''size of #-th axis '''))
sfpocs.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfpocs.version('1.7')
sfpocs.synopsis('''sfpocs < in.rsf > out.rsf mask=Fmask.rsf verb=n niter=100 pclip=10. n#=''','''Note: Acquistion geometry specified by mask operator.
''')
rsf.doc.progs['sfpocs']=sfpocs

sfrtm2d = rsf.doc.rsfprog('sfrtm2d','user/pyang/Mrtm2d.c','''2-D zero-offset reverse-time migration''')
sfrtm2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrtm2d.par('adj',rsf.doc.rsfpar('bool','n','','''if y, migration; else, modeling '''))
sfrtm2d.par('n0',rsf.doc.rsfpar('int','0','','''shot depth in the grid '''))
sfrtm2d.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfrtm2d.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval: dt '''))
sfrtm2d.version('1.7')
sfrtm2d.synopsis('''sfrtm2d vel=modl.rsf < data.rsf > imag.rsf adj=n n0=0 nt= dt=''',''' ''')
rsf.doc.progs['sfrtm2d']=sfrtm2d

sfrtmadcig = rsf.doc.rsfprog('sfrtmadcig','user/pyang/Mrtmadcig.c','''RTM and angle gather (ADCIG) extraction using poynting vector''')
sfrtmadcig.par('vecx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfrtmadcig.par('vecz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfrtmadcig.par('amp',rsf.doc.rsfpar('float','1.e3','','''maximum amplitude of ricker wavelet'''))
sfrtmadcig.par('fm',rsf.doc.rsfpar('float','','','''dominant freq of ricker '''))
sfrtmadcig.par('dt',rsf.doc.rsfpar('float','','','''time interval '''))
sfrtmadcig.par('nt',rsf.doc.rsfpar('int','','','''total modeling time steps '''))
sfrtmadcig.par('ns',rsf.doc.rsfpar('int','','','''total shots '''))
sfrtmadcig.par('ng',rsf.doc.rsfpar('int','','','''total receivers in each shot '''))
sfrtmadcig.par('nb',rsf.doc.rsfpar('int','20','','''thickness of split PML '''))
sfrtmadcig.par('na',rsf.doc.rsfpar('int','30','','''number of angles'''))
sfrtmadcig.par('kt',rsf.doc.rsfpar('int','200','','''record poynting vector at kt '''))
sfrtmadcig.par('jsx',rsf.doc.rsfpar('int','','','''source x-axis  jump interval  '''))
sfrtmadcig.par('jsz',rsf.doc.rsfpar('int','0','','''source z-axis jump interval  '''))
sfrtmadcig.par('jgx',rsf.doc.rsfpar('int','1','','''receiver x-axis jump interval '''))
sfrtmadcig.par('jgz',rsf.doc.rsfpar('int','0','','''receiver z-axis jump interval '''))
sfrtmadcig.par('sxbeg',rsf.doc.rsfpar('int','','','''x-begining index of sources, starting from 0 '''))
sfrtmadcig.par('szbeg',rsf.doc.rsfpar('int','','','''z-begining index of sources, starting from 0 '''))
sfrtmadcig.par('gxbeg',rsf.doc.rsfpar('int','','','''x-begining index of receivers, starting from 0 '''))
sfrtmadcig.par('gzbeg',rsf.doc.rsfpar('int','','','''z-begining index of receivers, starting from 0 '''))
sfrtmadcig.par('csdgather',rsf.doc.rsfpar('bool','y','','''default, common shot-gather; if n, record at every point'''))
sfrtmadcig.par('vmute',rsf.doc.rsfpar('float','1500','','''muting velocity to remove the low-freq noise, unit=m/s'''))
sfrtmadcig.par('tdmute',rsf.doc.rsfpar('int','2./(fm*dt)','','''number of deleyed time samples to mute '''))
sfrtmadcig.version('1.7')
sfrtmadcig.synopsis('''sfrtmadcig < vmodl.rsf > rtmadcig.rsf vecx=vecx.rsf vecz=vecz.rsf amp=1.e3 fm= dt= nt= ns= ng= nb=20 na=30 kt=200 jsx= jsz=0 jgx=1 jgz=0 sxbeg= szbeg= gxbeg= gzbeg= csdgather=y vmute=1500 tdmute=2./(fm*dt)''','''SPML boundary condition combined with 4-th order finite difference,
effective boundary saving strategy used!
''')
rsf.doc.progs['sfrtmadcig']=sfrtmadcig

sfTestaniso = rsf.doc.rsfprog('sfTestaniso','user/pyang/MTestaniso.c','''A 2D demo of elliptically-anisotropic wave propagation (4th order)''')
sfTestaniso.par('vx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfTestaniso.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfTestaniso.par('nb',rsf.doc.rsfpar('int','30','','''thickness of sponge ABC '''))
sfTestaniso.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfTestaniso.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfTestaniso.par('fm',rsf.doc.rsfpar('float','20.0','','''dominant freq of Ricker wavelet '''))
sfTestaniso.par('ft',rsf.doc.rsfpar('int','0','','''first recorded time '''))
sfTestaniso.par('jt',rsf.doc.rsfpar('int','1','','''time interval '''))
sfTestaniso.version('1.7')
sfTestaniso.synopsis('''sfTestaniso < Fvz.rsf vx=Fvx.rsf > Fw.rsf verb=n nb=30 nt= dt= fm=20.0 ft=0 jt=1''','''  Note: It is adapted according to Seregy Fomel's lecture on Seismic imaging.
''')
rsf.doc.progs['sfTestaniso']=sfTestaniso

sfTesteb = rsf.doc.rsfprog('sfTesteb','user/pyang/MTesteb.c','''Demo for effective boundary saving in regular grid''')
sfTesteb.par('back',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfTesteb.par('nb',rsf.doc.rsfpar('int','20','','''thickness of sponge ABC '''))
sfTesteb.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfTesteb.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfTesteb.par('fm',rsf.doc.rsfpar('float','20.0','','''dominant freq of Ricker wavelet '''))
sfTesteb.par('ft',rsf.doc.rsfpar('int','0','','''first recorded time '''))
sfTesteb.par('jt',rsf.doc.rsfpar('int','1','','''time interval '''))
sfTesteb.par('ns',rsf.doc.rsfpar('int','1','','''number of shots '''))
sfTesteb.par('ng',rsf.doc.rsfpar('int','nx','','''number of receivers '''))
sfTesteb.version('1.7')
sfTesteb.synopsis('''sfTesteb < Fv.rsf > Fw1.rsf back=Fw2.rsf nb=20 nt= dt= fm=20.0 ft=0 jt=1 ns=1 ng=nx''','''The sponge absorbing boundary condition is applied for simplicity!
2N-order FD: effective boundary needs N points on each side!
Note: In this demo, 2N=4 (N=2). 
 ''')
rsf.doc.progs['sfTesteb']=sfTesteb

sfTestelastic2d = rsf.doc.rsfprog('sfTestelastic2d','user/pyang/MTestelastic2d.c','''2D 8-th order elastic wave propagation using sponge ABC ''')
sfTestelastic2d.par('vs',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfTestelastic2d.par('rho',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfTestelastic2d.par('wavx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfTestelastic2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfTestelastic2d.par('nb',rsf.doc.rsfpar('int','30','','''thickness of PML boundary '''))
sfTestelastic2d.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfTestelastic2d.par('kt',rsf.doc.rsfpar('int','','','''record wavefield at time kt '''))
sfTestelastic2d.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfTestelastic2d.par('fm',rsf.doc.rsfpar('float','20.0','','''dominant freq of Ricker wavelet '''))
sfTestelastic2d.par('ft',rsf.doc.rsfpar('int','0','','''first recorded time '''))
sfTestelastic2d.par('jt',rsf.doc.rsfpar('int','1','','''time interval '''))
sfTestelastic2d.version('1.7')
sfTestelastic2d.synopsis('''sfTestelastic2d < Fvp.rsf vs=Fvs.rsf rho=Frho.rsf > Fwavz.rsf wavx=Fwavx.rsf verb=n nb=30 nt= kt= dt= fm=20.0 ft=0 jt=1''','''''')
rsf.doc.progs['sfTestelastic2d']=sfTestelastic2d

sfTestfd2d = rsf.doc.rsfprog('sfTestfd2d','user/pyang/MTestfd2d.c','''A demo of 2D FD test''')
sfTestfd2d.par('nb',rsf.doc.rsfpar('int','30','','''thickness of sponge ABC '''))
sfTestfd2d.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfTestfd2d.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfTestfd2d.par('fm',rsf.doc.rsfpar('float','20.0','','''dominant freq of Ricker wavelet '''))
sfTestfd2d.par('ft',rsf.doc.rsfpar('int','0','','''first recorded time '''))
sfTestfd2d.par('jt',rsf.doc.rsfpar('int','1','','''time interval '''))
sfTestfd2d.version('1.7')
sfTestfd2d.synopsis('''sfTestfd2d < Fv.rsf > Fw.rsf nb=30 nt= dt= fm=20.0 ft=0 jt=1''','''  Sponage absorbing boundary condition
''')
rsf.doc.progs['sfTestfd2d']=sfTestfd2d

sfTestfd3d = rsf.doc.rsfprog('sfTestfd3d','user/pyang/MTestfd3d.c','''3D acoustic time-domain FD modeling''')
sfTestfd3d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfTestfd3d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfTestfd3d.par('frsf',rsf.doc.rsfpar('bool','n','','''free surface or not '''))
sfTestfd3d.par('nt',rsf.doc.rsfpar('int','','',''''''))
sfTestfd3d.par('kt',rsf.doc.rsfpar('int','','','''record wavefield at time kt '''))
sfTestfd3d.par('ns',rsf.doc.rsfpar('int','1','',''''''))
sfTestfd3d.par('nb',rsf.doc.rsfpar('int','30','',''''''))
sfTestfd3d.par('dt',rsf.doc.rsfpar('float','','',''''''))
sfTestfd3d.par('fm',rsf.doc.rsfpar('float','20','',''''''))
sfTestfd3d.version('1.7')
sfTestfd3d.synopsis('''sfTestfd3d < Fv.rsf > Fw.rsf verb=n verb=n frsf=n nt= kt= ns=1 nb=30 dt= fm=20''','''4th order in space, 2nd order in time, sponge absorbing boundary condition.
''')
rsf.doc.progs['sfTestfd3d']=sfTestfd3d

sfTestspml = rsf.doc.rsfprog('sfTestspml','user/pyang/MTestspml.c','''2D acoustic FD using Split PML (SPML) absorbing boundary condition''')
sfTestspml.par('pz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfTestspml.par('px',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfTestspml.par('nb',rsf.doc.rsfpar('int','30','','''thickness of PML ABC '''))
sfTestspml.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfTestspml.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfTestspml.par('fm',rsf.doc.rsfpar('float','20.0','','''dominant freq of Ricker wavelet '''))
sfTestspml.par('ft',rsf.doc.rsfpar('int','0','','''first recorded time '''))
sfTestspml.par('jt',rsf.doc.rsfpar('int','1','','''time interval '''))
sfTestspml.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity, if y, output px and pz '''))
sfTestspml.par('kt',rsf.doc.rsfpar('int','','','''output px and pz component at kt '''))
sfTestspml.version('1.7')
sfTestspml.synopsis('''sfTestspml < Fv.rsf > Fw.rsf pz=Fpz.rsf px=Fpx.rsf nb=30 nt= dt= fm=20.0 ft=0 jt=1 verb=n kt=''','''NB: Staggered grid finite difference used!
''')
rsf.doc.progs['sfTestspml']=sfTestspml

sfviscoa2d = rsf.doc.rsfprog('sfviscoa2d','user/pyang/Mviscoa2d.c','''2D visco-acoustic modeling with 8th order staggered-grid FD''')
sfviscoa2d.par('rho',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfviscoa2d.par('tau',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfviscoa2d.par('tauo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfviscoa2d.par('pz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfviscoa2d.par('px',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfviscoa2d.par('nb',rsf.doc.rsfpar('int','30','','''thickness of PML ABC '''))
sfviscoa2d.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfviscoa2d.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfviscoa2d.par('fm',rsf.doc.rsfpar('float','20.0','','''dominant freq of Ricker wavelet '''))
sfviscoa2d.par('ft',rsf.doc.rsfpar('int','0','','''first recorded time '''))
sfviscoa2d.par('jt',rsf.doc.rsfpar('int','1','','''time interval '''))
sfviscoa2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity, if y, output px and pz '''))
sfviscoa2d.par('kt',rsf.doc.rsfpar('int','','','''output px and pz component at kt '''))
sfviscoa2d.version('1.7')
sfviscoa2d.synopsis('''sfviscoa2d < Fv.rsf rho=Frho.rsf tau=Ftau.rsf tauo=Ftauo.rsf > Fw.rsf pz=Fpz.rsf px=Fpx.rsf nb=30 nt= dt= fm=20.0 ft=0 jt=1 verb=n kt=''',''' ''')
rsf.doc.progs['sfviscoa2d']=sfviscoa2d

sfviscoe2d = rsf.doc.rsfprog('sfviscoe2d','user/pyang/Mviscoe2d.c','''2D 4-th order visco-elastic wave propagation using sponge ABC''')
sfviscoe2d.par('vs',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfviscoe2d.par('rho',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfviscoe2d.par('taup',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfviscoe2d.par('taus',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfviscoe2d.par('tauo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfviscoe2d.par('wavx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfviscoe2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfviscoe2d.par('nb',rsf.doc.rsfpar('int','30','','''thickness of sponge ABC '''))
sfviscoe2d.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfviscoe2d.par('kt',rsf.doc.rsfpar('int','','','''record wavefield at time kt '''))
sfviscoe2d.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfviscoe2d.par('fm',rsf.doc.rsfpar('float','20.0','','''dominant freq of Ricker wavelet '''))
sfviscoe2d.par('ft',rsf.doc.rsfpar('int','0','','''first recorded time '''))
sfviscoe2d.par('jt',rsf.doc.rsfpar('int','1','','''time interval '''))
sfviscoe2d.version('1.7')
sfviscoe2d.synopsis('''sfviscoe2d < Fvp.rsf vs=Fvs.rsf rho=Frho.rsf taup=Ftaup.rsf taus=Ftaus.rsf tauo=Ftauo.rsf > Fwavz.rsf wavx=Fwavx.rsf verb=n nb=30 nt= kt= dt= fm=20.0 ft=0 jt=1''','''''')
rsf.doc.progs['sfviscoe2d']=sfviscoe2d

sffbrec = rsf.doc.rsfprog('sffbrec','user/pyang/Mfbrec.cu','''Forward-backword exact reconstruction using boundary saving''')
sffbrec.par('back',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffbrec.par('amp',rsf.doc.rsfpar('float','1000','','''maximum amplitude of ricker '''))
sffbrec.par('fm',rsf.doc.rsfpar('float','10','','''dominant freq of ricker '''))
sffbrec.par('dt',rsf.doc.rsfpar('float','','','''time interval '''))
sffbrec.par('nt',rsf.doc.rsfpar('int','','','''total modeling time steps '''))
sffbrec.par('ns',rsf.doc.rsfpar('int','1','','''total shots '''))
sffbrec.par('ng',rsf.doc.rsfpar('int','','','''total receivers in each shot '''))
sffbrec.par('jsx',rsf.doc.rsfpar('int','','','''source x-axis  jump interval  '''))
sffbrec.par('jsz',rsf.doc.rsfpar('int','0','','''source z-axis jump interval  '''))
sffbrec.par('jgx',rsf.doc.rsfpar('int','1','','''receiver x-axis jump interval '''))
sffbrec.par('jgz',rsf.doc.rsfpar('int','0','','''receiver z-axis jump interval '''))
sffbrec.par('sxbeg',rsf.doc.rsfpar('int','','','''x-begining index of sources, starting from 0 '''))
sffbrec.par('szbeg',rsf.doc.rsfpar('int','','','''z-begining index of sources, starting from 0 '''))
sffbrec.par('gxbeg',rsf.doc.rsfpar('int','','','''x-begining index of receivers, starting from 0 '''))
sffbrec.par('gzbeg',rsf.doc.rsfpar('int','','','''z-begining index of receivers, starting from 0 '''))
sffbrec.par('csdgather',rsf.doc.rsfpar('bool','y','','''default, common shot-gather; if n, record at every point'''))
sffbrec.par('ft',rsf.doc.rsfpar('int','0','','''first recorded time '''))
sffbrec.par('jt',rsf.doc.rsfpar('int','1','','''time interval '''))
sffbrec.version('1.7')
sffbrec.synopsis('''sffbrec < vinit.rsf > Fw1.rsf back=Fw2.rsf amp=1000 fm=10 dt= nt= ns=1 ng= jsx= jsz=0 jgx=1 jgz=0 sxbeg= szbeg= gxbeg= gzbeg= csdgather=y ft=0 jt=1''','''Note: It is used as a demonstration that we can reconstruct the modeled
	wavefield exactly via boundary saving.
''')
rsf.doc.progs['sffbrec']=sffbrec

sfgpurtm = rsf.doc.rsfprog('sfgpurtm','user/pyang/Mgpurtm.cu','''2D prestack GPU-based RTM using effective boundary saving.''')
sfgpurtm.par('imag2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfgpurtm.par('fm',rsf.doc.rsfpar('float','','','''dominant freq of ricker '''))
sfgpurtm.par('dt',rsf.doc.rsfpar('float','','','''time interval '''))
sfgpurtm.par('nt',rsf.doc.rsfpar('int','','','''total modeling time steps '''))
sfgpurtm.par('ns',rsf.doc.rsfpar('int','','','''total shots '''))
sfgpurtm.par('ng',rsf.doc.rsfpar('int','','','''total receivers in each shot '''))
sfgpurtm.par('jsx',rsf.doc.rsfpar('int','','','''source x-axis  jump interval  '''))
sfgpurtm.par('jsz',rsf.doc.rsfpar('int','0','','''source z-axis jump interval  '''))
sfgpurtm.par('jgx',rsf.doc.rsfpar('int','1','','''receiver x-axis jump interval '''))
sfgpurtm.par('jgz',rsf.doc.rsfpar('int','0','','''receiver z-axis jump interval '''))
sfgpurtm.par('sxbeg',rsf.doc.rsfpar('int','','','''x-begining index of sources, starting from 0 '''))
sfgpurtm.par('szbeg',rsf.doc.rsfpar('int','','','''z-begining index of sources, starting from 0 '''))
sfgpurtm.par('gxbeg',rsf.doc.rsfpar('int','','','''x-begining index of receivers, starting from 0 '''))
sfgpurtm.par('gzbeg',rsf.doc.rsfpar('int','','','''z-begining index of receivers, starting from 0 '''))
sfgpurtm.par('order',rsf.doc.rsfpar('int','6','','''order of finite difference, order=2,4,6,8,10 '''))
sfgpurtm.par('phost',rsf.doc.rsfpar('float','0','','''phost% points on host with zero-copy pinned memory, the rest on device '''))
sfgpurtm.par('csdgather',rsf.doc.rsfpar('bool','y','','''default, common shot-gather; if n, record at every point'''))
sfgpurtm.par('vmute',rsf.doc.rsfpar('float','1500','','''muting velocity to remove the low-freq artifacts, unit=m/s'''))
sfgpurtm.par('tdmute',rsf.doc.rsfpar('int','2.0/(fm*dt)','','''number of deleyed time samples to mute '''))
sfgpurtm.version('1.7')
sfgpurtm.synopsis('''sfgpurtm < vmodl.rsf > imag1.rsf imag2=imag2.rsf fm= dt= nt= ns= ng= jsx= jsz=0 jgx=1 jgz=0 sxbeg= szbeg= gxbeg= gzbeg= order=6 phost=0 csdgather=y vmute=1500 tdmute=2.0/(fm*dt)''','''
Some basic descriptions of this code are in order.
1) Coordinate configuration of seismic data:

		o--------------> x (2nd dim: *.y)
		|
		|
		|
		|
		|
		z (1st dim: *.x)
	1st dim: i1=threadIdx.x+blockDim.x*blockIdx.x;
	2nd dim: i2=threadIdx.y+blockDim.y*blockIdx.y;
	(i1, i2)=i1+i2*nnz;

2) stability condition:	
	min(dx, dz)>sqrt(2)*dt*max(v) (NJ=2)
   numerical dispersion condition:	
	max(dx, dz)<min(v)/(10*fmax)  (NJ=2)
	max(dx, dz)<min(v)/(5*fmax)   (NJ=4)

3) This code doesn't save the history of forward time steps. We 
   just save the least boundaries (referred to as effective boundary 
   in our work) of every time step and the two final steps of the 
   wavefield. Using this information, we can easily reconstruct 
   the exact wavefield in the reverse time steps. It is noteworthy
   that to implement large scale seismic imaging, pinned memory is 
   employed to save the boundaries of each step so that all the saved
   data can be computed on the device directly.

4) In our implementation, we employ staggered grid based 
   convolutional PML (CPML) boundary condition. Using 20 points for 
   CPML is enough to obtain perfect absorbing effect (while commonly 
   used sponge ABC may need 30 or more). However, we use 32 points on
   each side due to the grid alignment reasons. (To make your code 
   fast, you should consider that the GPU codes implementation unit 
   is half-warp (16 threads). The thickness of the boundary should be 
   times of 16. 

5) The final images can be two kinds: result of correlation imaging 
   condition and the normalized one. The normalized correlation imaging
   result is preferred due to compensated illumination. Some filters 
   are popular and effective to remove the low frequency artifacts of 
   the imaging: the Laplacian filtering, derivative filtering and 
   the bandpass filtering. In this code, we use laplacian filtering.
''')
rsf.doc.progs['sfgpurtm']=sfgpurtm

sfgpufwi = rsf.doc.rsfprog('sfgpufwi','user/pyang/Mgpufwi.cu','''CUDA based FWI using Enquist absorbing boundary condition (A2)''')
sfgpufwi.par('shots',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgpufwi.par('grads',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfgpufwi.par('objs',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfgpufwi.par('illums',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfgpufwi.par('verb',rsf.doc.rsfpar('bool','y','','''vebosity '''))
sfgpufwi.par('precon',rsf.doc.rsfpar('bool','n','','''precondition or not '''))
sfgpufwi.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfgpufwi.par('rbell',rsf.doc.rsfpar('int','2','','''radius of bell smooth '''))
sfgpufwi.version('1.7')
sfgpufwi.synopsis('''sfgpufwi < vinit.rsf shots=shots.rsf > vupdates.rsf grads=grads.rsf objs=objs.rsf illums=illums.rsf verb=y precon=n niter=100 rbell=2''','''
Note: 	You can try other complex boundary condition but we do not
	recommend to do so. The main reason is that FWI is to recover
	the low-frequency information of the earth model. Low-freq 
	means that exact absorbing is not necessarilly needed. The 
	result will be improved with the optimization precedure. 
	Furthermore, complex boundary condition (such as sponge ABC or
	PML) implies more computational cost, which will degrade the
	efficiency of FWI. 
''')
rsf.doc.progs['sfgpufwi']=sfgpufwi

sfgenshots = rsf.doc.rsfprog('sfgenshots','user/pyang/Mgenshots.cu','''Generate shots for FWI using Enquist absorbing boundary condition''')
sfgenshots.par('time',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfgenshots.par('check',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfgenshots.par('chk',rsf.doc.rsfpar('bool','n','','''check whether GPU-CPU implementation coincide with each other or not '''))
sfgenshots.par('kt',rsf.doc.rsfpar('int','100','','''check it at it=100 '''))
sfgenshots.par('amp',rsf.doc.rsfpar('float','1000','','''maximum amplitude of ricker '''))
sfgenshots.par('fm',rsf.doc.rsfpar('float','10','','''dominant freq of ricker '''))
sfgenshots.par('dt',rsf.doc.rsfpar('float','','','''time interval '''))
sfgenshots.par('nt',rsf.doc.rsfpar('int','','','''total modeling time steps '''))
sfgenshots.par('ns',rsf.doc.rsfpar('int','','','''total shots '''))
sfgenshots.par('ng',rsf.doc.rsfpar('int','','','''total receivers in each shot '''))
sfgenshots.par('jsx',rsf.doc.rsfpar('int','','','''source x-axis  jump interval  '''))
sfgenshots.par('jsz',rsf.doc.rsfpar('int','0','','''source z-axis jump interval  '''))
sfgenshots.par('jgx',rsf.doc.rsfpar('int','1','','''receiver x-axis jump interval '''))
sfgenshots.par('jgz',rsf.doc.rsfpar('int','0','','''receiver z-axis jump interval '''))
sfgenshots.par('sxbeg',rsf.doc.rsfpar('int','','','''x-begining index of sources, starting from 0 '''))
sfgenshots.par('szbeg',rsf.doc.rsfpar('int','','','''z-begining index of sources, starting from 0 '''))
sfgenshots.par('gxbeg',rsf.doc.rsfpar('int','','','''x-begining index of receivers, starting from 0 '''))
sfgenshots.par('gzbeg',rsf.doc.rsfpar('int','','','''z-begining index of receivers, starting from 0 '''))
sfgenshots.par('csdgather',rsf.doc.rsfpar('bool','n','','''default, common shot-gather; if n, record at every point'''))
sfgenshots.version('1.7')
sfgenshots.synopsis('''sfgenshots < vinit.rsf > shots.rsf time=time.rsf check=check.rsf chk=n kt=100 amp=1000 fm=10 dt= nt= ns= ng= jsx= jsz=0 jgx=1 jgz=0 sxbeg= szbeg= gxbeg= gzbeg= csdgather=n''','''
Note: 	You can try other complex boundary condition but we do not
	recommend to do so. The main reason is that FWI is to recover
	the low-frequency information of the earth model. Low-freq 
	means that exact absorbing is not necessarilly needed. The 
	result will be improved with the optimization procedure. 
	Furthermore, complex boundary condition (such as sponge ABC or
	PML) implies more computational cost, which will degrade the
	efficiency of FWI. 
''')
rsf.doc.progs['sfgenshots']=sfgenshots

sfgpufd3d = rsf.doc.rsfprog('sfgpufd3d','user/pyang/Mgpufd3d.cu','''GPU-based finite difference on 3-D grid''')
sfgpufd3d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosit2 '''))
sfgpufd3d.par('nt',rsf.doc.rsfpar('int','','','''total number of time steps '''))
sfgpufd3d.par('kt',rsf.doc.rsfpar('int','','','''record wavefield at time kt '''))
sfgpufd3d.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfgpufd3d.par('fm',rsf.doc.rsfpar('float','20','','''dominant frequency of Ricker wavelet '''))
sfgpufd3d.par('ns',rsf.doc.rsfpar('int','1','','''number of sources '''))
sfgpufd3d.par('szbeg',rsf.doc.rsfpar('int','','','''source beginning of z-axis '''))
sfgpufd3d.par('sxbeg',rsf.doc.rsfpar('int','','','''source beginning of x-axis '''))
sfgpufd3d.par('sybeg',rsf.doc.rsfpar('int','','','''source beginning of y-axis '''))
sfgpufd3d.par('jsz',rsf.doc.rsfpar('int','','','''source jump interval in z-axis '''))
sfgpufd3d.par('jsx',rsf.doc.rsfpar('int','','','''source jump interval in x-axis '''))
sfgpufd3d.par('jsy',rsf.doc.rsfpar('int','','','''source jump interval in y-axis '''))
sfgpufd3d.version('1.7')
sfgpufd3d.synopsis('''sfgpufd3d < Fv.rsf > Fw.rsf verb=n nt= kt= dt= fm=20 ns=1 szbeg= sxbeg= sybeg= jsz= jsx= jsy=''','''''')
rsf.doc.progs['sfgpufd3d']=sfgpufd3d

sfgpufbrec3d = rsf.doc.rsfprog('sfgpufbrec3d','user/pyang/Mgpufbrec3d.cu','''Backward reconstruction of forward modeling with random boundary''')
sfgpufbrec3d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfgpufbrec3d.par('nb',rsf.doc.rsfpar('int','20','','''thickness of random boundary '''))
sfgpufbrec3d.par('nt',rsf.doc.rsfpar('int','','','''total number of time steps '''))
sfgpufbrec3d.par('kt',rsf.doc.rsfpar('int','','','''record wavefield at time kt '''))
sfgpufbrec3d.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfgpufbrec3d.par('fm',rsf.doc.rsfpar('float','20','','''dominant frequency of Ricker wavelet '''))
sfgpufbrec3d.par('ns',rsf.doc.rsfpar('int','1','','''number of sources '''))
sfgpufbrec3d.par('szbeg',rsf.doc.rsfpar('int','','','''source beginning of z-axis '''))
sfgpufbrec3d.par('sxbeg',rsf.doc.rsfpar('int','','','''source beginning of x-axis '''))
sfgpufbrec3d.par('sybeg',rsf.doc.rsfpar('int','','','''source beginning of y-axis '''))
sfgpufbrec3d.par('jsz',rsf.doc.rsfpar('int','','','''source jump interval in z-axis '''))
sfgpufbrec3d.par('jsx',rsf.doc.rsfpar('int','','','''source jump interval in x-axis '''))
sfgpufbrec3d.par('jsy',rsf.doc.rsfpar('int','','','''source jump interval in y-axis '''))
sfgpufbrec3d.version('1.7')
sfgpufbrec3d.synopsis('''sfgpufbrec3d < Fv.rsf > Fw.rsf verb=n nb=20 nt= kt= dt= fm=20 ns=1 szbeg= sxbeg= sybeg= jsz= jsx= jsy=''','''''')
rsf.doc.progs['sfgpufbrec3d']=sfgpufbrec3d

sfmpigpufwi = rsf.doc.rsfprog('sfmpigpufwi','user/pyang/Mmpigpufwi.cu','''CUDA based FWI using Enquist absorbing boundary condition''')
sfmpigpufwi.par('shots',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmpigpufwi.par('grads',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmpigpufwi.par('objs',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmpigpufwi.par('illums',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmpigpufwi.par('verb',rsf.doc.rsfpar('bool','y','','''vebosity '''))
sfmpigpufwi.par('precon',rsf.doc.rsfpar('bool','n','','''precondition or not '''))
sfmpigpufwi.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfmpigpufwi.par('rbell',rsf.doc.rsfpar('int','2','','''radius of bell smooth '''))
sfmpigpufwi.version('1.7')
sfmpigpufwi.synopsis('''sfmpigpufwi < vinit.rsf shots=shots.rsf > vupdates.rsf grads=grads.rsf objs=objs.rsf illums=illums.rsf verb=y precon=n niter=100 rbell=2''','''
Note: 	You can try other complex boundary condition but we do not
	recommend to do so. The main reason is that FWI is to recover
	the low-frequency information of the earth model. Low-freq 
	means that exact absorbing is not necessarilly needed. The 
	result will be improved with the optimization precedure. 
	Furthermore, complex boundary condition (such as sponge ABC or
	PML) implies more computational cost, which will degrade the
	efficiency of FWI. 
''')
rsf.doc.progs['sfmpigpufwi']=sfmpigpufwi

sfshuffle_test = rsf.doc.rsfprog('sfshuffle_test','user/pyang/Mshuffle_test.py','''shuffle the data''')
sfshuffle_test.par('axis',rsf.doc.rsfpar('int','2','',''''''))
sfshuffle_test.par('seed',rsf.doc.rsfpar('int','n2','',''''''))
sfshuffle_test.par('inv',rsf.doc.rsfpar('bool','n','',''''''))
sfshuffle_test.version('1.7')
sfshuffle_test.synopsis('''sfshuffle_test < pi.rsf > po.rsf axis=2 seed=n2 inv=n''','''''')
rsf.doc.progs['sfshuffle_test']=sfshuffle_test

