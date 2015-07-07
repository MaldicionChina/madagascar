sfmodrefl = rsf.doc.rsfprog('sfmodrefl','system/seismic/Mmodrefl.c','''Normal reflectivity modeling. ''')
sfmodrefl.par('vp',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmodrefl.par('vs',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmodrefl.par('rho',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmodrefl.par('nt',rsf.doc.rsfpar('int','','','''time samples '''))
sfmodrefl.par('dt',rsf.doc.rsfpar('float','','','''time sampling '''))
sfmodrefl.par('nw',rsf.doc.rsfpar('int','4','','''interpolation length '''))
sfmodrefl.version('1.7')
sfmodrefl.synopsis('''sfmodrefl < depth.rsf vp=vp.rsf vs=vs.rsf rho=rho.rsf > dat.rsf nt= dt= nw=4''','''''')
rsf.doc.progs['sfmodrefl']=sfmodrefl

