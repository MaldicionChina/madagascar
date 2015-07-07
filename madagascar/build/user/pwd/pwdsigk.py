sfpwdsigk = rsf.doc.rsfprog('sfpwdsigk','user/pwd/Mpwdsigk.c','''Signal component separation using plane-wave destruction. ''')
sfpwdsigk.par('dips',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwdsigk.par('weight',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpwdsigk.par('niter',rsf.doc.rsfpar('int','50','','''maximum number of iterations '''))
sfpwdsigk.par('nliter',rsf.doc.rsfpar('int','1','','''number of reweighting iterations '''))
sfpwdsigk.par('eps',rsf.doc.rsfpar('float','0.','','''regularization parameter '''))
sfpwdsigk.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfpwdsigk.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfpwdsigk.par('weight',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfpwdsigk.version('1.7')
sfpwdsigk.synopsis('''sfpwdsigk < in.rsf dips=dips.rsf > out.rsf weight=weight.rsf niter=50 nliter=1 eps=0. verb=n order=1''','''
The program works with 2-D data.
''')
rsf.doc.progs['sfpwdsigk']=sfpwdsigk

