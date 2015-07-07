sffileflush = rsf.doc.rsfprog('sffileflush','user/ivlad/Mfileflush.c','''Creates just the ascii header from parameters''')
sffileflush.version('1.7')
sffileflush.synopsis('''sffileflush < in.rsf > out.rsf''','''Wrapper for sf_fileflush (copy RSF header of a file to another) ''')
rsf.doc.progs['sffileflush']=sffileflush

