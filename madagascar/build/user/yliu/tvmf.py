sftvmf = rsf.doc.rsfprog('sftvmf','user/yliu/Mtvmf.c','''1D Time-varying median filtering. ''')
sftvmf.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sftvmf.par('nfw',rsf.doc.rsfpar('int','','','''reference filter-window length (>delta, positive and odd integer)'''))
sftvmf.par('alpha',rsf.doc.rsfpar('int','2','','''time-varying window parameter "alpha" (default=2)'''))
sftvmf.par('beta',rsf.doc.rsfpar('int','0','','''time-varying window parameter "beta" (default=0)'''))
sftvmf.par('gamma',rsf.doc.rsfpar('int','2','','''time-varying window parameter "gamma" (default=2)'''))
sftvmf.par('delta',rsf.doc.rsfpar('int','4','','''time-varying window parameter "delta" (default=4)'''))
sftvmf.version('1.7')
sftvmf.synopsis('''sftvmf < in.rsf > out.rsf boundary=n nfw= alpha=2 beta=0 gamma=2 delta=4''','''''')
rsf.doc.progs['sftvmf']=sftvmf

