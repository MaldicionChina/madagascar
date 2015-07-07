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

