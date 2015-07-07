sfpscefd = rsf.doc.rsfprog('sfpscefd','user/chen/Mpscefd.c','''EFD phase shift wave extrapolation. ''')
sfpscefd.par('data',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpscefd.par('wave',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpscefd.par('jt',rsf.doc.rsfpar('int','40','','''time step for wave data '''))
sfpscefd.par('nz',rsf.doc.rsfpar('int','nz0','','''depth number '''))
sfpscefd.version('1.7')
sfpscefd.synopsis('''sfpscefd < modl.rsf > imag.rsf data=data.rsf wave=wave.rsf jt=40 nz=nz0''','''''')
rsf.doc.progs['sfpscefd']=sfpscefd

