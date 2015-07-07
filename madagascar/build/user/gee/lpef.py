sflpef = rsf.doc.rsfprog('sflpef','user/gee/Mlpef.c','''Find PEF on aliased traces. ''')
sflpef.par('a',rsf.doc.rsfpar('ints','','',''' [dim]'''))
sflpef.par('center',rsf.doc.rsfpar('ints','','',''' [dim]'''))
sflpef.par('gap',rsf.doc.rsfpar('ints','','',''' [dim]'''))
sflpef.par('jump',rsf.doc.rsfpar('int','2','',''''''))
sflpef.par('lag',rsf.doc.rsfpar('string ',desc='''output file for filter lags '''))
sflpef.version('1.7 Mlpef.c 4796 2009-09-29 19:39:07Z ivlad')
sflpef.synopsis('''sflpef < dat.rsf > pef.rsf a= center= gap= jump=2 lag=''','''''')
rsf.doc.progs['sflpef']=sflpef

