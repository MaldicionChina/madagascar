sfTestspml = rsf.doc.rsfprog('sfTestspml','user/pyang/MTestspml.c','''2D acoustic FD using Split PML (SPML) absorbing boundary condition''')
sfTestspml.par('pz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfTestspml.par('px',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfTestspml.par('nb',rsf.doc.rsfpar('int','30','','''thickness of PML ABC '''))
sfTestspml.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfTestspml.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfTestspml.par('fm',rsf.doc.rsfpar('float','20.0','','''dominant freq of Ricker wavelet '''))
sfTestspml.par('ft',rsf.doc.rsfpar('int','0','','''first recorded time '''))
sfTestspml.par('jt',rsf.doc.rsfpar('int','1','','''time interval '''))
sfTestspml.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity, if y, output px and pz '''))
sfTestspml.par('kt',rsf.doc.rsfpar('int','','','''output px and pz component at kt '''))
sfTestspml.version('1.7')
sfTestspml.synopsis('''sfTestspml < Fv.rsf > Fw.rsf pz=Fpz.rsf px=Fpx.rsf nb=30 nt= dt= fm=20.0 ft=0 jt=1 verb=n kt=''','''NB: Staggered grid finite difference used!
''')
rsf.doc.progs['sfTestspml']=sfTestspml

