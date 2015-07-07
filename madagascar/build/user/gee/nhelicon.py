sfnhelicon = rsf.doc.rsfprog('sfnhelicon','user/gee/Mnhelicon.c','''Non-stationary helix convolution and deconvolution. ''')
sfnhelicon.par('filt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnhelicon.par('nh',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnhelicon.par('pch',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnhelicon.par('adj',rsf.doc.rsfpar('bool','n','','''if y, do adjoint operation '''))
sfnhelicon.par('div',rsf.doc.rsfpar('bool','n','','''if y, do inverse operation (deconvolution) '''))
sfnhelicon.par('nh',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfnhelicon.par('pch',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfnhelicon.par('lag',rsf.doc.rsfpar('string ',desc=''''''))
sfnhelicon.version('1.7 Mnhelicon.c 4796 2009-09-29 19:39:07Z ivlad')
sfnhelicon.synopsis('''sfnhelicon < in.rsf > out.rsf filt=filt.rsf nh=fnh.rsf pch=fpch.rsf adj=n div=n lag=''','''''')
rsf.doc.progs['sfnhelicon']=sfnhelicon

