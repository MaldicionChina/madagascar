import rsf.doc

sflrmatrix = rsf.doc.rsfprog('sflrmatrix','user/lexing/Mlrmatrix.cc','''Lowrank matrix decomposition''')
sflrmatrix.par('name',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sflrmatrix.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sflrmatrix.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sflrmatrix.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sflrmatrix.par('outputs',rsf.doc.rsfpar('','2','','''number of outputs (2 or 3)'''))
sflrmatrix.version('1.7')
sflrmatrix.synopsis('''sflrmatrix name=mfile.rsf < in.rsf > out.rsf seed=time(NULL eps=1.e-4 npk=20 outputs=2''','''''')
rsf.doc.progs['sflrmatrix']=sflrmatrix

