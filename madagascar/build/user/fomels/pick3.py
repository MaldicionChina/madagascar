sfpick3 = rsf.doc.rsfprog('sfpick3','user/fomels/Mpick3.c','''Automatic picking  from 3-D semblance-like panels. ''')
sfpick3.par('vel1',rsf.doc.rsfpar('float','o2','',''''''))
sfpick3.par('vel2',rsf.doc.rsfpar('float','o3','','''surface velocity '''))
sfpick3.par('rect1',rsf.doc.rsfpar('int','1','','''smoothing radius '''))
sfpick3.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfpick3.par('an1',rsf.doc.rsfpar('float','1.','',''''''))
sfpick3.par('an2',rsf.doc.rsfpar('float','1.','','''axes anisotropy '''))
sfpick3.par('gate1',rsf.doc.rsfpar('int','3','',''''''))
sfpick3.par('gate2',rsf.doc.rsfpar('int','3','','''picking gate '''))
sfpick3.par('smooth',rsf.doc.rsfpar('bool','y','','''if apply smoothing '''))
sfpick3.version('1.7')
sfpick3.synopsis('''sfpick3 < scn.rsf > pik.rsf vel1=o2 vel2=o3 rect1=1 niter=100 an1=1. an2=1. gate1=3 gate2=3 smooth=y''','''''')
rsf.doc.progs['sfpick3']=sfpick3

