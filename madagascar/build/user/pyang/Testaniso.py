sfTestaniso = rsf.doc.rsfprog('sfTestaniso','user/pyang/MTestaniso.c','''A 2D demo of elliptically-anisotropic wave propagation (4th order)''')
sfTestaniso.par('vx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfTestaniso.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfTestaniso.par('nb',rsf.doc.rsfpar('int','30','','''thickness of sponge ABC '''))
sfTestaniso.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfTestaniso.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfTestaniso.par('fm',rsf.doc.rsfpar('float','20.0','','''dominant freq of Ricker wavelet '''))
sfTestaniso.par('ft',rsf.doc.rsfpar('int','0','','''first recorded time '''))
sfTestaniso.par('jt',rsf.doc.rsfpar('int','1','','''time interval '''))
sfTestaniso.version('1.7')
sfTestaniso.synopsis('''sfTestaniso < Fvz.rsf vx=Fvx.rsf > Fw.rsf verb=n nb=30 nt= dt= fm=20.0 ft=0 jt=1''','''  Note: It is adapted according to Seregy Fomel's lecture on Seismic imaging.
''')
rsf.doc.progs['sfTestaniso']=sfTestaniso

