sfederiv3d = rsf.doc.rsfprog('sfederiv3d','user/jyan/Mederiv3d.c','''''')
sfederiv3d.par('ccc',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfederiv3d.par('zdel',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfederiv3d.par('xdel',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfederiv3d.par('ydel',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfederiv3d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfederiv3d.par('stat',rsf.doc.rsfpar('bool','y','','''stationary operator '''))
sfederiv3d.par('domain',rsf.doc.rsfpar('string ',desc=''''''))
sfederiv3d.version('1.7')
sfederiv3d.synopsis('''sfederiv3d ccc=Fccc.rsf < Fspk.rsf zdel=Fzdel.rsf xdel=Fxdel.rsf ydel=Fydel.rsf verb=n stat=y domain=''','''''')
rsf.doc.progs['sfederiv3d']=sfederiv3d

