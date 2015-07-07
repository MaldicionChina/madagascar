sfdeburst = rsf.doc.rsfprog('sfdeburst','user/gee/Mdeburst.c','''Remove bursty noise by IRLS. ''')
sfdeburst.par('niter',rsf.doc.rsfpar('int','10','','''number of iterations '''))
sfdeburst.par('eps',rsf.doc.rsfpar('float','1.','','''regularization parameter '''))
sfdeburst.par('norm',rsf.doc.rsfpar('string ',desc='''norm to use in IRLS (cauchy,l1) '''))
sfdeburst.version('1.7 Mdeburst.c 7267 2011-06-13 18:38:18Z saragiotis')
sfdeburst.synopsis('''sfdeburst < in.rsf > out.rsf niter=10 eps=1. norm=''','''''')
rsf.doc.progs['sfdeburst']=sfdeburst

