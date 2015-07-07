sfsglfdcx2_7 = rsf.doc.rsfprog('sfsglfdcx2_7','user/fangg/Msglfdcx2_7.cc','''2D Lowrank FD coefficient of d/dx on staggered grid (optimized)''')
sfsglfdcx2_7.par('sx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsglfdcx2_7.par('sz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsglfdcx2_7.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfsglfdcx2_7.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sfsglfdcx2_7.par('npk',rsf.doc.rsfpar('','50','','''maximum rank'''))
sfsglfdcx2_7.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sfsglfdcx2_7.par('size',rsf.doc.rsfpar('','6','','''stencil length'''))
sfsglfdcx2_7.par('wavnumcut',rsf.doc.rsfpar('','1.0','','''wavenumber cut percentile'''))
sfsglfdcx2_7.version('1.7')
sfsglfdcx2_7.synopsis('''sfsglfdcx2_7 < velf.rsf > outm.rsf sx=fsx.rsf sz=fsz.rsf seed=time(NULL eps=1.e-6 npk=50 dt= size=6 wavnumcut=1.0''','''''')
rsf.doc.progs['sfsglfdcx2_7']=sfsglfdcx2_7

