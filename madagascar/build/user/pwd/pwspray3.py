sfpwspray3 = rsf.doc.rsfprog('sfpwspray3','user/pwd/Mpwspray3.c','''Plane-wave spray in 3-D. ''')
sfpwspray3.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwspray3.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfpwspray3.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfpwspray3.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfpwspray3.par('ns2',rsf.doc.rsfpar('int','','',''''''))
sfpwspray3.par('ns3',rsf.doc.rsfpar('int','','','''spray radius '''))
sfpwspray3.version('1.7')
sfpwspray3.synopsis('''sfpwspray3 < inp.rsf dip=dip.rsf > out.rsf verb=n eps=0.01 order=1 ns2= ns3=''','''''')
rsf.doc.progs['sfpwspray3']=sfpwspray3

