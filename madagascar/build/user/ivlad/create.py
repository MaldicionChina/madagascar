sfcreate = rsf.doc.rsfprog('sfcreate','user/ivlad/Mcreate.c','''Creates just the ascii header from parameters''')
sfcreate.par('n#',rsf.doc.rsfpar('int','','','''size of #-th axis '''))
sfcreate.version('1.7')
sfcreate.synopsis('''sfcreate > out.rsf n#=''','''Wrapper for sf_fileflush (creating RSF header from params) ''')
rsf.doc.progs['sfcreate']=sfcreate

