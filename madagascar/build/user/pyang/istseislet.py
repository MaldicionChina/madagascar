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

