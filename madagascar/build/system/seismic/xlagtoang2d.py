sfxlagtoang2d = rsf.doc.rsfprog('sfxlagtoang2d','system/seismic/Mxlagtoang2d.c','''SS(x-lag) to angle transformation (PP or PS waves) ''')
sfxlagtoang2d.par('vpvs',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfxlagtoang2d.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfxlagtoang2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfxlagtoang2d.par('inv',rsf.doc.rsfpar('bool','n','','''inverse transformation flag '''))
sfxlagtoang2d.par('na',rsf.doc.rsfpar('int','sf_n(axs)','',''''''))
sfxlagtoang2d.par('da',rsf.doc.rsfpar('float','1./(sf_n(axs)-1)','',''''''))
sfxlagtoang2d.par('oa',rsf.doc.rsfpar('float','0.','',''''''))
sfxlagtoang2d.par('extend',rsf.doc.rsfpar('int','4','','''tmp extension '''))
sfxlagtoang2d.version('1.7')
sfxlagtoang2d.synopsis('''sfxlagtoang2d < Fstk.rsf > Fang.rsf vpvs=Fgam.rsf dip=Fdip.rsf verb=n inv=n na=sf_n(axs) da=1./(sf_n(axs)-1) oa=0. extend=4''','''''')
rsf.doc.progs['sfxlagtoang2d']=sfxlagtoang2d

