sfbin = rsf.doc.rsfprog('sfbin','system/generic/Mbin.c','''Data binning in 2-D slices. ''')
sfbin.par('fold',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfbin.par('xkey',rsf.doc.rsfpar('int','0','','''x key number '''))
sfbin.par('ykey',rsf.doc.rsfpar('int','1','','''y key number '''))
sfbin.par('xmax',rsf.doc.rsfpar('float','','','''x maximum '''))
sfbin.par('xmin',rsf.doc.rsfpar('float','','','''x minimum '''))
sfbin.par('ymax',rsf.doc.rsfpar('float','','','''y maximum '''))
sfbin.par('ymin',rsf.doc.rsfpar('float','','','''y minimum '''))
sfbin.par('x0',rsf.doc.rsfpar('float','xmin','','''x origin '''))
sfbin.par('y0',rsf.doc.rsfpar('float','ymin','','''y origin '''))
sfbin.par('nx',rsf.doc.rsfpar('int','(int) (xmax - xmin + 1.)','','''Number of bins in x '''))
sfbin.par('ny',rsf.doc.rsfpar('int','(int) (ymax - ymin + 1.)','','''Number of bins in y '''))
sfbin.par('dx',rsf.doc.rsfpar('float','','','''bin size in x '''))
sfbin.par('dy',rsf.doc.rsfpar('float','','','''bin size in y '''))
sfbin.par('interp',rsf.doc.rsfpar('int','1','[0,1,2]','''interpolation method;
       0: median, 1: nearest neighbor, 2: bi-linear,  '''))
sfbin.par('norm',rsf.doc.rsfpar('bool','y','','''if normalize '''))
sfbin.par('clip',rsf.doc.rsfpar('float','FLT_EPSILON','','''clip for fold normalization '''))
sfbin.par('head',rsf.doc.rsfpar('string ',desc='''header file '''))
sfbin.par('fold',rsf.doc.rsfpar('string ',desc='''output file for fold (optional) (auxiliary output file name)'''))
sfbin.version('1.7 Mbin.c 13815 2015-02-01 23:48:56Z sfomel')
sfbin.synopsis('''sfbin < in.rsf > out.rsf fold=fold.rsf xkey=0 ykey=1 xmax= xmin= ymax= ymin= x0=xmin y0=ymin nx=(int) (xmax - xmin + 1.) ny=(int) (ymax - ymin + 1.) dx= dy= interp=1 norm=y clip=FLT_EPSILON head=''','''
December 2014 program of the month:
http://ahay.org/rsflog/index.php?/archives/419-Program-of-the-month-sfbin.html
''')
rsf.doc.progs['sfbin']=sfbin

