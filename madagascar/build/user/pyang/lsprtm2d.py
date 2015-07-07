sflsprtm2d = rsf.doc.rsfprog('sflsprtm2d','user/pyang/Mlsprtm2d.c','''2-D prestack least-squares RTM using wavefield reconstruction''')
sflsprtm2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflsprtm2d.par('imgrtm',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sflsprtm2d.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sflsprtm2d.par('niter',rsf.doc.rsfpar('int','10','','''totol number of least-squares iteration'''))
sflsprtm2d.par('nb',rsf.doc.rsfpar('int','20','','''number (thickness) of ABC on each side '''))
sflsprtm2d.version('1.7')
sflsprtm2d.synopsis('''sflsprtm2d < shots.rsf vel=velo.rsf > imag.rsf imgrtm=imgrtm.rsf verb=y niter=10 nb=20''','''NB: Sponge ABC is applied!
''')
rsf.doc.progs['sflsprtm2d']=sflsprtm2d

