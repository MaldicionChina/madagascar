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

