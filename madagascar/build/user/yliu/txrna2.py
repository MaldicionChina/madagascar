sftxrna2 = rsf.doc.rsfprog('sftxrna2','user/yliu/Mtxrna2.c','''2D space-noncausal t-x nonstationary regularized autoregression. ''')
sftxrna2.par('a',rsf.doc.rsfpar('ints','','',''' [mdim]'''))
sftxrna2.par('niter',rsf.doc.rsfpar('int','20','','''number of iterations '''))
sftxrna2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sftxrna2.version('1.7 Mtxrna2.c 11561 2014-01-05 05:16:51Z yang_liu')
sftxrna2.synopsis('''sftxrna2 < mat.rsf > pre.rsf a= niter=20 verb=n''','''''')
rsf.doc.progs['sftxrna2']=sftxrna2

