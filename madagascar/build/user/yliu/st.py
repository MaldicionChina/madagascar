sfst = rsf.doc.rsfprog('sfst','user/yliu/Mst.c','''S transform ''')
sfst.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfst.par('flo',rsf.doc.rsfpar('float','','','''Low frequency in band, default is 0 '''))
sfst.par('fhi',rsf.doc.rsfpar('float','','','''High frequency in band, default is Nyquist '''))
sfst.version('1.7 Mst.c 8858 2012-07-23 16:33:06Z saragiotis')
sfst.synopsis('''sfst < in.rsf > out.rsf inv=n flo= fhi=''','''''')
rsf.doc.progs['sfst']=sfst

