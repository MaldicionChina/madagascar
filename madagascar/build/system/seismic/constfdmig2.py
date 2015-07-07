sfconstfdmig2 = rsf.doc.rsfprog('sfconstfdmig2','system/seismic/Mconstfdmig2.c','''2-D implicit finite-difference migration in constant velocity. ''')
sfconstfdmig2.par('movie',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfconstfdmig2.par('nz',rsf.doc.rsfpar('int','2*(nw-1)','','''vertical time samples '''))
sfconstfdmig2.par('dz',rsf.doc.rsfpar('float','1./(nz*dw)','','''vertical time sampling '''))
sfconstfdmig2.par('vel',rsf.doc.rsfpar('float','','','''constant velocity '''))
sfconstfdmig2.par('hi',rsf.doc.rsfpar('bool','y','','''if y, use 45-degree; n, 15-degree '''))
sfconstfdmig2.par('sixth',rsf.doc.rsfpar('float','1./12','','''one-sixth trick '''))
sfconstfdmig2.par('movie',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfconstfdmig2.version('1.7')
sfconstfdmig2.synopsis('''sfconstfdmig2 < data.rsf > imag.rsf movie=movie.rsf nz=2*(nw-1) dz=1./(nz*dw) vel= hi=y sixth=1./12''','''''')
rsf.doc.progs['sfconstfdmig2']=sfconstfdmig2

