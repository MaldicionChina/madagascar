sfmffit = rsf.doc.rsfprog('sfmffit','user/fomels/Mmffit.c','''Fitting multi-focusing approximations ''')
sfmffit.par('coef',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmffit.par('fit',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmffit.par('x0',rsf.doc.rsfpar('float','m0','','''central midpoint '''))
sfmffit.par('type',rsf.doc.rsfpar('string ',desc='''Type of approximation (crs,mf,nonhyperbolic) '''))
sfmffit.version('1.7')
sfmffit.synopsis('''sfmffit < in.rsf coef=coef.rsf > out.rsf fit=fit.rsf x0=m0 type=''','''''')
rsf.doc.progs['sfmffit']=sfmffit

