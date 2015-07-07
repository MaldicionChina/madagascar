sfcsqrtf = rsf.doc.rsfprog('sfcsqrtf','user/ivlad/Mcsqrtf.c','''Complex square root. Good example of I/O loop for applying a function.''')
sfcsqrtf.version('1.7')
sfcsqrtf.synopsis('''sfcsqrtf < in.rsf > out.rsf''','''Realized after I wrote this program that the sqrt function in sfmath does the
same job, but keeping it around as a simple example of buffer I/O. ''')
rsf.doc.progs['sfcsqrtf']=sfcsqrtf

