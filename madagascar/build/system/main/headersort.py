sfheadersort = rsf.doc.rsfprog('sfheadersort','system/main/headersort.c','''Sort a dataset according to a header key. ''')
sfheadersort.par('head',rsf.doc.rsfpar('string ',desc='''header file '''))
sfheadersort.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfheadersort')
sfheadersort.version('1.7 headersort.c 13857 2015-02-22 19:18:06Z sfomel')
sfheadersort.synopsis('''sfheadersort < in.rsf > out.rsf head=''','''''')
rsf.doc.progs['sfheadersort']=sfheadersort

