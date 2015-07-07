sfigrad = rsf.doc.rsfprog('sfigrad','system/generic/Migrad.c','''Gradient on the first axis. ''')
sfigrad.par('square',rsf.doc.rsfpar('bool','n','','''if y, use gradient squared '''))
sfigrad.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfigrad.version('1.7')
sfigrad.synopsis('''sfigrad < in.rsf > out.rsf square=n adj=n''','''''')
rsf.doc.progs['sfigrad']=sfigrad

