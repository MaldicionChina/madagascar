sfinterleave = rsf.doc.rsfprog('sfinterleave','system/main/interleave.c','''Combine several datasets by interleaving.''')
sfinterleave.par('axis',rsf.doc.rsfpar('int','3','','''Axis for interleaving '''))
sfinterleave.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfinterleave')
sfinterleave.version('1.7')
sfinterleave.synopsis('''sfinterleave > out.rsf axis=3 [< file0.rsf] file1.rsf file2.rsf ...''','''''')
rsf.doc.progs['sfinterleave']=sfinterleave

