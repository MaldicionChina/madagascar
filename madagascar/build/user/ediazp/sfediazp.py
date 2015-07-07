import rsf.doc

sfnderiv = rsf.doc.rsfprog('sfnderiv','user/ediazp/Mnderiv.py','''''')
sfnderiv.par('order',rsf.doc.rsfpar('int','1','','''order of the derivative, default first derivative'''))
sfnderiv.par('length',rsf.doc.rsfpar('int','5','','''filter length, the lengthier the accurate, but also gets costlier'''))
sfnderiv.par('scale',rsf.doc.rsfpar('bool','y','','''scales by 1/d^order'''))
sfnderiv.par('axis',rsf.doc.rsfpar('int','1','','''apply differentiator along axis, default is fast axis'''))
sfnderiv.version('1.7')
sfnderiv.synopsis('''sfnderiv < Fin.rsf > Fout.rsf order=1 length=5 scale=y axis=1''','''This program implements Fornberg, 1988
paper for digital differentiators
of arbitrary order.

So, it computes first, second, n derivative along axis 1,2 or 3.
''')
rsf.doc.progs['sfnderiv']=sfnderiv

