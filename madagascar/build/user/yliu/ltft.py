sfltft = rsf.doc.rsfprog('sfltft','user/yliu/Mltft.c','''Local time-frequency transform (LTFT). ''')
sfltft.par('basis',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfltft.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfltft.par('weight',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfltft.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfltft.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfltft.par('nw',rsf.doc.rsfpar('int','','','''number of frequencies '''))
sfltft.par('dw',rsf.doc.rsfpar('float','','','''frequency step '''))
sfltft.par('w0',rsf.doc.rsfpar('float','0.','','''first frequency '''))
sfltft.par('rect',rsf.doc.rsfpar('int','10','','''smoothing radius (in time, samples) '''))
sfltft.par('niter',rsf.doc.rsfpar('int','100','','''number of inversion iterations '''))
sfltft.par('alpha',rsf.doc.rsfpar('float','0.','','''frequency adaptivity '''))
sfltft.par('basis',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfltft.par('mask',rsf.doc.rsfpar('string ',desc='''data weight (auxiliary input file name)'''))
sfltft.par('weight',rsf.doc.rsfpar('string ',desc='''model weight (auxiliary input file name)'''))
sfltft.version('1.7 Mltft.c 12981 2014-07-14 14:28:02Z sfomel')
sfltft.synopsis('''sfltft < in.rsf > out.rsf basis=basis.rsf mask=mask.rsf weight=weight.rsf inv=n verb=n nw= dw= w0=0. rect=10 niter=100 alpha=0.''','''
July 2014 program of the month:
ahay.org/rsflog/index.php?/archives/396-Program-of-the-month-sfltft.html
''')
rsf.doc.progs['sfltft']=sfltft

