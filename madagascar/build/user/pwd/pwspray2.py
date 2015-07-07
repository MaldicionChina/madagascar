sfpwspray2 = rsf.doc.rsfprog('sfpwspray2','user/pwd/Mpwspray2.c','''Plane-wave spray in 3-D. ''')
sfpwspray2.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwspray2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfpwspray2.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfpwspray2.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfpwspray2.par('ns2',rsf.doc.rsfpar('int','','',''''''))
sfpwspray2.par('ns3',rsf.doc.rsfpar('int','','','''spray radius '''))
sfpwspray2.version('1.7')
sfpwspray2.synopsis('''sfpwspray2 < inp.rsf dip=dip.rsf > out.rsf verb=n eps=0.01 order=1 ns2= ns3=''','''''')
rsf.doc.progs['sfpwspray2']=sfpwspray2

