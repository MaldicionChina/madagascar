sftxrna3 = rsf.doc.rsfprog('sftxrna3','user/yliu/Mtxrna3.c','''3D space-noncausal t-x-y nonstationary regularized autoregression. ''')
sftxrna3.par('a',rsf.doc.rsfpar('ints','','',''' [mdim]'''))
sftxrna3.par('niter',rsf.doc.rsfpar('int','20','','''number of iterations '''))
sftxrna3.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sftxrna3.version('1.7 Mtxrna3.c 11561 2014-01-05 05:16:51Z yang_liu')
sftxrna3.synopsis('''sftxrna3 < mat.rsf > pre.rsf a= niter=20 verb=n''','''''')
rsf.doc.progs['sftxrna3']=sftxrna3

