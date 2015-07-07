sfmaskinv = rsf.doc.rsfprog('sfmaskinv','user/gee/Mmaskinv.c','''Missing data interpolation using one or two prediction-error filters. ''')
sfmaskinv.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmaskinv.par('center',rsf.doc.rsfpar('ints','','','''filter center  [dim]'''))
sfmaskinv.par('a',rsf.doc.rsfpar('ints','','','''first filter dimensions  [dim]'''))
sfmaskinv.par('b',rsf.doc.rsfpar('ints','','','''second filter dimensions  [dim]'''))
sfmaskinv.par('niter',rsf.doc.rsfpar('int','80','','''number of iterations '''))
sfmaskinv.version('1.7')
sfmaskinv.synopsis('''sfmaskinv < in.rsf > out.rsf mask=mask.rsf center= a= b= niter=80''','''''')
rsf.doc.progs['sfmaskinv']=sfmaskinv

