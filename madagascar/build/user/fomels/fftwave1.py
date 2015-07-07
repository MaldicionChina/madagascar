sffftwave1 = rsf.doc.rsfprog('sffftwave1','user/fomels/Mfftwave1.c','''1-D FFT wave extrapolation ''')
sffftwave1.par('prop',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave1.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave1.par('nt',rsf.doc.rsfpar('int','','',''''''))
sffftwave1.par('dt',rsf.doc.rsfpar('float','','',''''''))
sffftwave1.par('sub',rsf.doc.rsfpar('bool','y','','''if -1 is included in the matrix '''))
sffftwave1.par('step',rsf.doc.rsfpar('bool','y','','''if two-step propagation '''))
sffftwave1.par('nsps',rsf.doc.rsfpar('bool','n','','''if using NSPS '''))
sffftwave1.par('right',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sffftwave1.version('1.7')
sffftwave1.synopsis('''sffftwave1 < inp.rsf > out.rsf prop=prop.rsf right=right.rsf nt= dt= sub=y step=y nsps=n''','''''')
rsf.doc.progs['sffftwave1']=sffftwave1

