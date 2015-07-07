sfgettype = rsf.doc.rsfprog('sfgettype','user/ivlad/Mgettype.c','''Displays numerical type of a dataset''')
sfgettype.version('1.7')
sfgettype.synopsis('''sfgettype < in.rsf''','''Output can be be: SF_CHAR, SF_COMPLEX, SF_FLOAT, SF_INT, SF_SHORT, SF_UCHAR
Shell/tester for sf_gettype''')
rsf.doc.progs['sfgettype']=sfgettype

