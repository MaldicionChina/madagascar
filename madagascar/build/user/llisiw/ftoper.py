sfftoper = rsf.doc.rsfprog('sfftoper','user/llisiw/Mftoper.c','''First-arrival Traveltime Tomography (linear operator) ''')
sfftoper.par('time',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfftoper.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfftoper.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfftoper.par('time',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfftoper.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfftoper.version('1.7')
sfftoper.synopsis('''sfftoper < in.rsf > out.rsf time=time.rsf mask=mask.rsf adj=n''','''''')
rsf.doc.progs['sfftoper']=sfftoper

