sfpredict = rsf.doc.rsfprog('sfpredict','user/pwd/Mpredict.c','''2-D plane-wave prediction. ''')
sfpredict.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpredict.par('adj',rsf.doc.rsfpar('bool','n','',''''''))
sfpredict.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfpredict.version('1.7 Mtrismooth2.c 752 2004-08-22 21:57:40Z fomels')
sfpredict.synopsis('''sfpredict < in.rsf dip=dip.rsf > out.rsf adj=n order=1''','''''')
rsf.doc.progs['sfpredict']=sfpredict

