sftrismooth2 = rsf.doc.rsfprog('sftrismooth2','user/pwd/Mtrismooth2.c','''2-D smoothing by triangle directional shaping. ''')
sftrismooth2.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftrismooth2.par('rect1',rsf.doc.rsfpar('int','3','',''''''))
sftrismooth2.par('rect2',rsf.doc.rsfpar('int','3','','''smoothing radius '''))
sftrismooth2.par('adj',rsf.doc.rsfpar('bool','n','',''''''))
sftrismooth2.version('1.7 Mtrismooth2.c 10160 2013-04-10 20:11:15Z sfomel')
sftrismooth2.synopsis('''sftrismooth2 < in.rsf dip=dip.rsf > out.rsf rect1=3 rect2=3 adj=n''','''''')
rsf.doc.progs['sftrismooth2']=sftrismooth2

