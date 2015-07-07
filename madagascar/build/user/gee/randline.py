sfrandline = rsf.doc.rsfprog('sfrandline','user/gee/Mrandline.c','''Construct data from random lines ''')
sfrandline.par('n1',rsf.doc.rsfpar('int','10','',''''''))
sfrandline.par('n2',rsf.doc.rsfpar('int','10','','''dimensions '''))
sfrandline.par('lines',rsf.doc.rsfpar('int','3','','''number of lines '''))
sfrandline.par('seed',rsf.doc.rsfpar('int','2000','','''random number seed '''))
sfrandline.version('1.7')
sfrandline.synopsis('''sfrandline > out.rsf n1=10 n2=10 lines=3 seed=2000''','''''')
rsf.doc.progs['sfrandline']=sfrandline

