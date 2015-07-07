sffiledims = rsf.doc.rsfprog('sffiledims','user/ivlad/Mfiledims.c','''Computes number of dimensions and their values''')
sffiledims.par('large',rsf.doc.rsfpar('bool','n','','''if y, file with large dimensions. '''))
sffiledims.par('parform',rsf.doc.rsfpar('bool','y','','''If y, print out parameter=value. If n, print out value. '''))
sffiledims.version('1.7')
sffiledims.synopsis('''sffiledims < in.rsf large=n parform=y''','''Wrapper for sf_filedims. ''')
rsf.doc.progs['sffiledims']=sffiledims

