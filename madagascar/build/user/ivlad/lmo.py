sflmo = rsf.doc.rsfprog('sflmo','user/ivlad/Mlmo.c','''Linear move-out in the frequency domain''')
sflmo.par('p',rsf.doc.rsfpar('float','','','''Slope of LMO '''))
sflmo.version('1.7')
sflmo.synopsis('''sflmo < in.rsf > out.rsf p=''','''''')
rsf.doc.progs['sflmo']=sflmo

