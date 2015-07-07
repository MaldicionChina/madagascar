sfstackn = rsf.doc.rsfprog('sfstackn','user/saragiotis/Mstackn.c','''Stack prespecified values. ''')
sfstackn.par('min',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfstackn.par('max',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfstackn.par('mean',rsf.doc.rsfpar('bool','y','','''if n, sum; if y, average '''))
sfstackn.par('thres',rsf.doc.rsfpar('float','0.','','''threshold (percentage of maxabs) '''))
sfstackn.par('min',rsf.doc.rsfpar('string ',desc='''file determining from which value to stack (auxiliary input file name)'''))
sfstackn.par('max',rsf.doc.rsfpar('string ',desc='''file determining up to which value to stack (auxiliary input file name)'''))
sfstackn.version('1.7')
sfstackn.synopsis('''sfstackn < in.rsf > out.rsf min=minin.rsf max=maxin.rsf mean=y thres=0.''','''''')
rsf.doc.progs['sfstackn']=sfstackn

