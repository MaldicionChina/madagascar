sffactorm = rsf.doc.rsfprog('sffactorm','user/gee/Mfactorm.c','''Plane-wave destruction with 3-D plane-wave filter. ''')
sffactorm.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffactorm.par('eps',rsf.doc.rsfpar('float','0.001','',''''''))
sffactorm.par('nt',rsf.doc.rsfpar('int','','',''''''))
sffactorm.par('nx',rsf.doc.rsfpar('int','','',''''''))
sffactorm.par('npx',rsf.doc.rsfpar('int','100','',''''''))
sffactorm.par('npy',rsf.doc.rsfpar('int','100','','''np = npx *npy; '''))
sffactorm.par('niter',rsf.doc.rsfpar('int','10','','''number of iterations '''))
sffactorm.version('1.7')
sffactorm.synopsis('''sffactorm < in.rsf > out.rsf dip=dip.rsf eps=0.001 nt= nx= npx=100 npy=100 niter=10''','''''')
rsf.doc.progs['sffactorm']=sffactorm

