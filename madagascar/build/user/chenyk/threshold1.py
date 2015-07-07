sfthreshold1 = rsf.doc.rsfprog('sfthreshold1','user/chenyk/Mthreshold1.c','''Soft or hard thresholding using exact-value or percentile thresholding.''')
sfthreshold1.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfthreshold1.par('ifperc',rsf.doc.rsfpar('int','1','','''0, exact-value thresholding; 1, percentile thresholding. '''))
sfthreshold1.par('ifverb',rsf.doc.rsfpar('int','0','','''0, not print threshold value; 1, print threshold value. '''))
sfthreshold1.par('thr',rsf.doc.rsfpar('float','','','''thresholding level '''))
sfthreshold1.par('type',rsf.doc.rsfpar('string ',desc='''[soft,hard] thresholding type, the default is soft  '''))
sfthreshold1.par('other',rsf.doc.rsfpar('string ',desc='''If output the difference between the thresholded part and the original one (auxiliary output file name)'''))
sfthreshold1.version('1.7')
sfthreshold1.synopsis('''sfthreshold1 < in.rsf > out.rsf other=other.rsf ifperc=1 ifverb=0 thr= type=''','''   When type=soft and ifperc=1, sfthreshold1 is equal to sfthreshold.
''')
rsf.doc.progs['sfthreshold1']=sfthreshold1

