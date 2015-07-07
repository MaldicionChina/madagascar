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

