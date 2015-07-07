sffactorn = rsf.doc.rsfprog('sffactorn','user/gee/Mfactorn.c','''Missing data interpolation with 3-D plane-wave filter. ''')
sffactorn.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffactorn.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffactorn.par('eps',rsf.doc.rsfpar('float','0.001','',''''''))
sffactorn.par('nt',rsf.doc.rsfpar('int','','',''''''))
sffactorn.par('nx',rsf.doc.rsfpar('int','','',''''''))
sffactorn.par('npx',rsf.doc.rsfpar('int','100','',''''''))
sffactorn.par('npy',rsf.doc.rsfpar('int','100','',''''''))
sffactorn.par('niter',rsf.doc.rsfpar('int','10','','''number of factorization iterations '''))
sffactorn.par('miter',rsf.doc.rsfpar('int','10','','''number of interpolation iterations '''))
sffactorn.version('1.7')
sffactorn.synopsis('''sffactorn < in.rsf > out.rsf dip=dip.rsf mask=mask.rsf eps=0.001 nt= nx= npx=100 npy=100 niter=10 miter=10''','''''')
rsf.doc.progs['sffactorn']=sffactorn

