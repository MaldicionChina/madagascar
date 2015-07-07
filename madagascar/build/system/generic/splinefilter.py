sfsplinefilter = rsf.doc.rsfprog('sfsplinefilter','system/generic/Msplinefilter.c','''Convert data to B-spline coefficients. ''')
sfsplinefilter.par('nw',rsf.doc.rsfpar('int','','','''filter size '''))
sfsplinefilter.version('1.7')
sfsplinefilter.synopsis('''sfsplinefilter < in.rsf > out.rsf nw=''','''''')
rsf.doc.progs['sfsplinefilter']=sfsplinefilter

