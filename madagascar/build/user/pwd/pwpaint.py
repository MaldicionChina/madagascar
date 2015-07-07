sfpwpaint = rsf.doc.rsfprog('sfpwpaint','user/pwd/Mpwpaint.c','''Painting by plane-wave construction. ''')
sfpwpaint.par('seed',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwpaint.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfpwpaint.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfpwpaint.par('i0',rsf.doc.rsfpar('int','0','','''reference trace '''))
sfpwpaint.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfpwpaint.par('seed',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfpwpaint.version('1.7 Mflat.c 1131 2005-04-20 18:19:10Z fomels')
sfpwpaint.synopsis('''sfpwpaint < dip.rsf > out.rsf seed=seed.rsf verb=n eps=0.01 i0=0 order=1''','''''')
rsf.doc.progs['sfpwpaint']=sfpwpaint

