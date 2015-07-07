sfpwpaint2 = rsf.doc.rsfprog('sfpwpaint2','user/pwd/Mpwpaint2.c','''3-D painting by plane-wave construction. ''')
sfpwpaint2.par('cost',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwpaint2.par('seed',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwpaint2.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfpwpaint2.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfpwpaint2.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfpwpaint2.par('seed',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfpwpaint2.version('1.7')
sfpwpaint2.synopsis('''sfpwpaint2 < dip.rsf > out.rsf cost=cost.rsf seed=seed.rsf verb=n eps=0.01 order=1''','''''')
rsf.doc.progs['sfpwpaint2']=sfpwpaint2

