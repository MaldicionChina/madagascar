sfnmow_adj = rsf.doc.rsfprog('sfnmow_adj','system/seismic/Mnmow_adj.c','''None''')
sfnmow_adj.par('gather',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmow_adj.par('adj',rsf.doc.rsfpar('bool','n','',''''''))
sfnmow_adj.par('nw',rsf.doc.rsfpar('int','3','',''''''))
sfnmow_adj.version('1.7')
sfnmow_adj.synopsis('''sfnmow_adj < inp.rsf > out.rsf gather=gather.rsf adj=n nw=3''','''''')
rsf.doc.progs['sfnmow_adj']=sfnmow_adj

