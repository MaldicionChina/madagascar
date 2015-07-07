sfirays = rsf.doc.rsfprog('sfirays','user/llisiw/Mirays.c','''Fast marching for image rays ''')
sfirays.par('t0',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfirays.par('x0',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfirays.par('f0',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfirays.par('velocity',rsf.doc.rsfpar('bool','y','','''y, inputs are velocity / n, slowness-squared '''))
sfirays.par('order',rsf.doc.rsfpar('int','1','','''fastmarching accuracy order '''))
sfirays.par('thres',rsf.doc.rsfpar('float','10.','','''thresholding for caustics '''))
sfirays.par('t0',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfirays.par('x0',rsf.doc.rsfpar('string ',desc='''output upwind neighbor (auxiliary output file name)'''))
sfirays.par('f0',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfirays.version('1.7')
sfirays.synopsis('''sfirays < in.rsf > out.rsf t0=ot0.rsf x0=ox0.rsf f0=of0.rsf velocity=y order=1 thres=10.''','''''')
rsf.doc.progs['sfirays']=sfirays

