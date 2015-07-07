sfthreshold2 = rsf.doc.rsfprog('sfthreshold2','user/yliu/Mthreshold2.c','''2-D Soft thresholding. ''')
sfthreshold2.par('thr',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfthreshold2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfthreshold2.par('pclip',rsf.doc.rsfpar('float','99.','',''''''))
sfthreshold2.par('thr',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfthreshold2.version('1.7 Mthreshold2.c 13869 2015-03-03 03:58:51Z zhiguang0810')
sfthreshold2.synopsis('''sfthreshold2 < in.rsf > out.rsf thr=thr.rsf verb=n pclip=99.''','''''')
rsf.doc.progs['sfthreshold2']=sfthreshold2

