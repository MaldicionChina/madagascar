sfdwt = rsf.doc.rsfprog('sfdwt','system/generic/Mdwt.c','''1-D digital wavelet transform ''')
sfdwt.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfdwt.par('adj',rsf.doc.rsfpar('bool','n','','''if y, do adjoint transform '''))
sfdwt.par('unit',rsf.doc.rsfpar('bool','n','','''if y, use unitary scaling '''))
sfdwt.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sfdwt.version('1.7')
sfdwt.synopsis('''sfdwt < in.rsf > out.rsf inv=n adj=n unit=n type=''','''''')
rsf.doc.progs['sfdwt']=sfdwt

