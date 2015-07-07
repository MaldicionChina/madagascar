sfpwspray = rsf.doc.rsfprog('sfpwspray','user/pwd/Mpwspray.c','''Plane-wave spray. ''')
sfpwspray.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwspray.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfpwspray.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfpwspray.par('ns',rsf.doc.rsfpar('int','','','''spray radius '''))
sfpwspray.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfpwspray.par('rect',rsf.doc.rsfpar('int','2','','''radius for predictive coherence (reduce=coherence) '''))
sfpwspray.par('reduce',rsf.doc.rsfpar('string ',desc='''reduction method (none,stack,median,triangle,gaussian,predict,coherence) '''))
sfpwspray.version('1.7')
sfpwspray.synopsis('''sfpwspray < inp.rsf dip=dip.rsf > out.rsf verb=n eps=0.01 ns= order=1 rect=2 reduce=''','''''')
rsf.doc.progs['sfpwspray']=sfpwspray

