sfsglfdcz2_7 = rsf.doc.rsfprog('sfsglfdcz2_7','user/fangg/Msglfdcz2_7.cc','''2D Lowrank FD coefficient of d/dx on staggered grid''')
sfsglfdcz2_7.par('sx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsglfdcz2_7.par('sz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsglfdcz2_7.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfsglfdcz2_7.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sfsglfdcz2_7.par('npk',rsf.doc.rsfpar('','50','','''maximum rank'''))
sfsglfdcz2_7.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sfsglfdcz2_7.par('size',rsf.doc.rsfpar('','6','','''stencil length'''))
sfsglfdcz2_7.par('wavnumcut',rsf.doc.rsfpar('','1.0','','''wavenumber cut percentile'''))
sfsglfdcz2_7.version('1.7')
sfsglfdcz2_7.synopsis('''sfsglfdcz2_7 < velf.rsf > outm.rsf sx=fsx.rsf sz=fsz.rsf seed=time(NULL eps=1.e-6 npk=50 dt= size=6 wavnumcut=1.0''','''''')
rsf.doc.progs['sfsglfdcz2_7']=sfsglfdcz2_7

