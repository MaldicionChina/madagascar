sfsglfdcp1 = rsf.doc.rsfprog('sfsglfdcp1','user/fangg/Msglfdcp1.cc','''Relative error of phase velocity of 16-th order 1D SG Lowrank FD and 1D FD coefficient ''')
sfsglfdcp1.par('Mfd',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsglfdcp1.par('Mlr',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsglfdcp1.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfsglfdcp1.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sfsglfdcp1.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfsglfdcp1.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sfsglfdcp1.par('size',rsf.doc.rsfpar('','16','','''stencil length'''))
sfsglfdcp1.version('1.7')
sfsglfdcp1.synopsis('''sfsglfdcp1 < velf.rsf > outm.rsf Mfd=Mfdfile.rsf Mlr=Mlrfile.rsf seed=time(NULL eps=1.e-4 npk=20 dt= size=16''','''''')
rsf.doc.progs['sfsglfdcp1']=sfsglfdcp1

