sfseisigk = rsf.doc.rsfprog('sfseisigk','user/pwd/Mseisigk.c','''Signal component separation using seislet transforms. ''')
sfseisigk.par('dips',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfseisigk.par('weight',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfseisigk.par('niter',rsf.doc.rsfpar('int','50','','''maximum number of iterations '''))
sfseisigk.par('nliter',rsf.doc.rsfpar('int','1','','''number of reweighting iterations '''))
sfseisigk.par('eps',rsf.doc.rsfpar('float','0.','','''regularization parameter '''))
sfseisigk.par('eps0',rsf.doc.rsfpar('float','0.01','','''regularization for seislet '''))
sfseisigk.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfseisigk.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfseisigk.par('weight',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfseisigk.par('type',rsf.doc.rsfpar('string ',desc='''wavelet type (haar,linear) '''))
sfseisigk.version('1.7')
sfseisigk.synopsis('''sfseisigk < in.rsf dips=dips.rsf > out.rsf weight=weight.rsf niter=50 nliter=1 eps=0. eps0=0.01 verb=n order=1 type=''','''
The program works with 2-D data. The second dimension should be a power of 2.
''')
rsf.doc.progs['sfseisigk']=sfseisigk

