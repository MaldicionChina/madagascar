sfmpipsp = rsf.doc.rsfprog('sfmpipsp','user/poulsonj/Mmpipsp.cc','''Parallel Sweeping Preconditioner (PSP) for solving 3D Helmholtz equations.''')
sfmpipsp.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmpipsp.par('source',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmpipsp.par('solution',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmpipsp.par('n1',rsf.doc.rsfpar('','origNx','',''''''))
sfmpipsp.par('n2',rsf.doc.rsfpar('','origNy','',''''''))
sfmpipsp.par('n3',rsf.doc.rsfpar('','origNz','',''''''))
sfmpipsp.par('freq',rsf.doc.rsfpar('','','','''frequency in HZ'''))
sfmpipsp.par('sigma',rsf.doc.rsfpar('','1.5 ','','''magnitude of PML stretching'''))
sfmpipsp.par('pmlSize',rsf.doc.rsfpar('','5 ','','''number of grid points of PML'''))
sfmpipsp.version('1.7')
sfmpipsp.synopsis('''sfmpipsp velocity=in.rsf source=src.rsf solution=out.rsf n1=origNx n2=origNy n3=origNz freq= sigma=1.5  pmlSize=5 ''','''''')
rsf.doc.progs['sfmpipsp']=sfmpipsp

