sfve2d = rsf.doc.rsfprog('sfve2d','user/kourkina/Mve2d.c','''Convert interval velocity to Dix velocity ''')
sfve2d.par('x',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfve2d.par('z',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfve2d.par('nt',rsf.doc.rsfpar('int','','',''''''))
sfve2d.par('dt',rsf.doc.rsfpar('float','','',''''''))
sfve2d.par('order',rsf.doc.rsfpar('int','4','','''interpolation order '''))
sfve2d.version('1.7')
sfve2d.synopsis('''sfve2d < fsc.rsf > fid.rsf x=fx.rsf z=fy.rsf nt= dt= order=4''','''''')
rsf.doc.progs['sfve2d']=sfve2d

