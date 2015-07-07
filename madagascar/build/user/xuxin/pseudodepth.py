sfpseudodepth = rsf.doc.rsfprog('sfpseudodepth','user/xuxin/Mpseudodepth.c','''depth to vertical-time interpolation''')
sfpseudodepth.par('tau',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpseudodepth.par('inv',rsf.doc.rsfpar('bool','n','','''if y, tau to z; if n, tau to z '''))
sfpseudodepth.par('linear',rsf.doc.rsfpar('bool','y','','''if y, linear spline; if n, cubic spline (buggy) '''))
sfpseudodepth.par('n',rsf.doc.rsfpar('int','','','''tau n '''))
sfpseudodepth.par('o',rsf.doc.rsfpar('float','0.','','''tau o '''))
sfpseudodepth.par('d',rsf.doc.rsfpar('float','','','''tau d (>0) '''))
sfpseudodepth.version('1.7')
sfpseudodepth.synopsis('''sfpseudodepth < Fin.rsf tau=Ftau.rsf > Fout.rsf inv=n linear=y n= o=0. d=''','''   z to tau : pseudodepth < FZ.rsf inv=n tau=tau.rsf n=ntau o=otau d=dtau > FT.rsf
   tau to z : pseudodepth < FT.rsf inv=y tau=tau.rsf > FZ.rsf ''')
rsf.doc.progs['sfpseudodepth']=sfpseudodepth

