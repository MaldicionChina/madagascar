sfbspvel2 = rsf.doc.rsfprog('sfbspvel2','user/cram/Mbspvel2.c','''B-spline coefficients for a 2-D (an)isotropic velocity model. ''')
sfbspvel2.par('vx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfbspvel2.par('eta',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfbspvel2.par('theta',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfbspvel2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfbspvel2.par('vx',rsf.doc.rsfpar('string ',desc='''Horizontal velocity (auxiliary input file name)'''))
sfbspvel2.par('eta',rsf.doc.rsfpar('string ',desc='''Anellipticity (auxiliary input file name)'''))
sfbspvel2.par('theta',rsf.doc.rsfpar('string ',desc='''Tilt angle (auxiliary input file name)'''))
sfbspvel2.version('1.7')
sfbspvel2.synopsis('''sfbspvel2 < velz.rsf > out.rsf vx=velx.rsf eta=eta.rsf theta=theta.rsf verb=n''','''''')
rsf.doc.progs['sfbspvel2']=sfbspvel2

