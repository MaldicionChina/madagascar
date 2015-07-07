sfpwpaint3 = rsf.doc.rsfprog('sfpwpaint3','user/pwd/Mpwpaint3.c','''3-D painting by plane-wave construction. ''')
sfpwpaint3.par('seed',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwpaint3.par('cost',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwpaint3.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfpwpaint3.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfpwpaint3.par('ref2',rsf.doc.rsfpar('int','0','',''''''))
sfpwpaint3.par('ref3',rsf.doc.rsfpar('int','0','','''reference trace '''))
sfpwpaint3.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfpwpaint3.version('1.7 Mflat.c 743 2004-08-16 20:41:00Z fomels')
sfpwpaint3.synopsis('''sfpwpaint3 < dip.rsf > out.rsf seed=seed.rsf cost=cost.rsf verb=n eps=0.01 ref2=0 ref3=0 order=1''','''''')
rsf.doc.progs['sfpwpaint3']=sfpwpaint3

