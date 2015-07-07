sfnoise = rsf.doc.rsfprog('sfnoise','system/generic/Mnoise.c','''Add random noise to the data.''')
sfnoise.par('seed',rsf.doc.rsfpar('int','time(NULL)','','''random seed '''))
sfnoise.par('type',rsf.doc.rsfpar('bool','y','','''noise distribution, y: normal, n: uniform '''))
sfnoise.par('var',rsf.doc.rsfpar('float','','','''noise variance '''))
sfnoise.par('range',rsf.doc.rsfpar('float','','','''noise range (default=1) '''))
sfnoise.par('mean',rsf.doc.rsfpar('float','0','','''noise mean '''))
sfnoise.par('rep',rsf.doc.rsfpar('bool','n','','''if y, replace data with noise '''))
sfnoise.version('1.7 Mnoise.c 13817 2015-02-03 00:18:33Z wangh0a')
sfnoise.synopsis('''sfnoise < in.rsf > out.rsf seed=time(NULL) type=y var= range= mean=0 rep=n''','''
July 2011 program of the month:
http://ahay.org/rsflog/index.php?/archives/262-Program-of-the-month-sfnoise.html
''')
rsf.doc.progs['sfnoise']=sfnoise

