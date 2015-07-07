sfsnrstack = rsf.doc.rsfprog('sfsnrstack','user/gchliu/Msnrstack.c','''Stack a dataset over the second dimensions by SNR weighted method. ''')
sfsnrstack.par('w',rsf.doc.rsfpar('int','50','','''sliding window size'''))
sfsnrstack.par('sft',rsf.doc.rsfpar('float','1','','''weight shift'''))
sfsnrstack.par('ee',rsf.doc.rsfpar('float','1.0','',''''''))
sfsnrstack.par('esp',rsf.doc.rsfpar('float','1.0','',''''''))
sfsnrstack.version('1.7')
sfsnrstack.synopsis('''sfsnrstack < in.rsf > out.rsf w=50 sft=1 ee=1.0 esp=1.0''','''''')
rsf.doc.progs['sfsnrstack']=sfsnrstack

