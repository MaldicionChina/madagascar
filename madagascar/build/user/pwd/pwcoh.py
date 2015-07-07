sfpwcoh = rsf.doc.rsfprog('sfpwcoh','user/pwd/Mpwcoh.c','''Coherency by plane-wave construction. ''')
sfpwcoh.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwcoh.par('a2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpwcoh.par('b2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpwcoh.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfpwcoh.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfpwcoh.par('rect',rsf.doc.rsfpar('int','2','','''spread '''))
sfpwcoh.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfpwcoh.version('1.7 Mflat.c 1131 2005-04-20 18:19:10Z fomels')
sfpwcoh.synopsis('''sfpwcoh < in.rsf > out.rsf dip=dip.rsf a2=a2.rsf b2=b2.rsf verb=n eps=0.01 rect=2 order=1''','''''')
rsf.doc.progs['sfpwcoh']=sfpwcoh

