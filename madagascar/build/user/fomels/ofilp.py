sfofilp = rsf.doc.rsfprog('sfofilp','user/fomels/Mofilp.c','''2-D missing data interpolation by differential offset continuation. ''')
sfofilp.par('known',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfofilp.par('niter',rsf.doc.rsfpar('int','10','','''number of iterations '''))
sfofilp.par('simple',rsf.doc.rsfpar('bool','n','','''if y, use simple h derivative for regularization '''))
sfofilp.version('1.7 Mofilp.c 7107 2011-04-10 02:04:14Z ivlad')
sfofilp.synopsis('''sfofilp < in.rsf > out.rsf known=known.rsf niter=10 simple=n''','''''')
rsf.doc.progs['sfofilp']=sfofilp

