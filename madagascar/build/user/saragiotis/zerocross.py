sfzerocross = rsf.doc.rsfprog('sfzerocross','user/saragiotis/Mzerocross.c','''Zero crossings. ''')
sfzerocross.par('levels',rsf.doc.rsfpar('int','3','','''levels of quantization [2,3,5].
      levels=2	1: zero crossing or zero; 0: otherwise
      levels=3	1: positive to negative zc; -1 negative to positive zc; 0: otherwise
      levels=5	+/-2: positive/negative values; +/-1: as in levels=3; 0: zero. 
    '''))
sfzerocross.version('1.7')
sfzerocross.synopsis('''sfzerocross < in.rsf > out.rsf levels=3''','''''')
rsf.doc.progs['sfzerocross']=sfzerocross

