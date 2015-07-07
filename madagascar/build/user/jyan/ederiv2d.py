sfederiv2d = rsf.doc.rsfprog('sfederiv2d','user/jyan/Mederiv2d.c','''''')
sfederiv2d.par('ccc',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfederiv2d.par('zdel',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfederiv2d.par('xdel',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfederiv2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfederiv2d.par('stat',rsf.doc.rsfpar('bool','y','','''stationary operator '''))
sfederiv2d.par('sig',rsf.doc.rsfpar('float','1.5','','''sigma '''))
sfederiv2d.par('order',rsf.doc.rsfpar('int','8','','''order '''))
sfederiv2d.par('domain',rsf.doc.rsfpar('string ',desc=''''''))
sfederiv2d.par('tapertype',rsf.doc.rsfpar('string ',desc=''''''))
sfederiv2d.version('1.7')
sfederiv2d.synopsis('''sfederiv2d ccc=Fccc.rsf < Fspk.rsf zdel=Fzdel.rsf xdel=Fxdel.rsf verb=n stat=y sig=1.5 order=8 domain= tapertype=''','''''')
rsf.doc.progs['sfederiv2d']=sfederiv2d

