sflapfill = rsf.doc.rsfprog('sflapfill','system/generic/Mlapfill.c','''Missing data interpolation in 2-D by Laplacian regularization. ''')
sflapfill.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflapfill.par('niter',rsf.doc.rsfpar('int','200','','''number of iterations '''))
sflapfill.par('grad',rsf.doc.rsfpar('bool','n','','''if y, use gradient instead of laplacian '''))
sflapfill.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sflapfill.par('mask',rsf.doc.rsfpar('string ',desc='''optional mask file with zeroes for missing data locations (auxiliary input file name)'''))
sflapfill.version('1.7')
sflapfill.synopsis('''sflapfill < in.rsf > out.rsf mask=mask.rsf niter=200 grad=n verb=n''','''''')
rsf.doc.progs['sflapfill']=sflapfill

