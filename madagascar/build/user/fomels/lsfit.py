sflsfit = rsf.doc.rsfprog('sflsfit','user/fomels/Mlsfit.c','''Simple least-squares regression. ''')
sflsfit.par('fit',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflsfit.par('coef',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sflsfit.par('weight',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflsfit.par('linear',rsf.doc.rsfpar('bool','y','','''if linear LS '''))
sflsfit.par('dim',rsf.doc.rsfpar('int','dim','','''number of dimensions '''))
sflsfit.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization parameter '''))
sflsfit.par('coef',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sflsfit.par('weight',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sflsfit.version('1.7')
sflsfit.synopsis('''sflsfit < inp.rsf fit=fit.rsf > out.rsf coef=coef.rsf weight=wht.rsf linear=y dim=dim eps=0.0f''','''''')
rsf.doc.progs['sflsfit']=sflsfit

