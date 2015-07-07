sflpf = rsf.doc.rsfprog('sflpf','user/fomels/Mlpf.c','''Local prediction filter (n-dimensional). ''')
sflpf.par('match',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflpf.par('pred',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sflpf.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sflpf.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sflpf.par('pred',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sflpf.par('pef',rsf.doc.rsfpar('string ',desc='''signal PEF file (optional) '''))
sflpf.par('lag',rsf.doc.rsfpar('string ',desc='''file with PEF lags (optional) '''))
sflpf.version('1.7')
sflpf.synopsis('''sflpf < dat.rsf match=mat.rsf > flt.rsf pred=pre.rsf niter=100 verb=y pef= lag=''','''''')
rsf.doc.progs['sflpf']=sflpf

