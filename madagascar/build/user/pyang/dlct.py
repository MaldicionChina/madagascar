sfdlct = rsf.doc.rsfprog('sfdlct','user/pyang/Mdlct.c','''discrete linear chirp transfrom (DLCT)''')
sfdlct.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform (Here adjoint is the same as inverse!) '''))
sfdlct.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfdlct.par('C',rsf.doc.rsfpar('float','0.005','','''C=2*Lambda/L, unit slice '''))
sfdlct.par('L',rsf.doc.rsfpar('int','','',''''''))
sfdlct.version('1.7')
sfdlct.synopsis('''sfdlct < in.rsf > out.rsf inv=n verb=n C=0.005 L=''',''' ''')
rsf.doc.progs['sfdlct']=sfdlct

