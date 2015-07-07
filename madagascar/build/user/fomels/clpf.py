sfclpf = rsf.doc.rsfprog('sfclpf','user/fomels/Mclpf.c','''Local prediction filter for complex numbers (n-dimensional). ''')
sfclpf.par('match',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfclpf.par('pred',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfclpf.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfclpf.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfclpf.par('pred',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfclpf.version('1.7')
sfclpf.synopsis('''sfclpf < dat.rsf match=mat.rsf > flt.rsf pred=pre.rsf niter=100 verb=y''','''''')
rsf.doc.progs['sfclpf']=sfclpf

