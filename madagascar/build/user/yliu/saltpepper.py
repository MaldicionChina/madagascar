sfsaltpepper = rsf.doc.rsfprog('sfsaltpepper','user/yliu/Msaltpepper.c','''Add salt and pepper noise to the data.''')
sfsaltpepper.par('den',rsf.doc.rsfpar('float','10.','','''noise density (percent, default=10, Min=0, Max=100) '''))
sfsaltpepper.par('inten',rsf.doc.rsfpar('float','0.1','','''noise intensity (multiple peak value of data, default=0.1) '''))
sfsaltpepper.par('rep',rsf.doc.rsfpar('bool','n','','''if y, replace data with noise '''))
sfsaltpepper.par('allpos',rsf.doc.rsfpar('bool','n','','''if y, assume positive noise '''))
sfsaltpepper.par('noise',rsf.doc.rsfpar('bool','n','','''if y, output noise only '''))
sfsaltpepper.par('seed',rsf.doc.rsfpar('int','time(NULL)','','''random seed '''))
sfsaltpepper.version('1.7 Msaltpepper.c 7107 2011-04-10 02:04:14Z ivlad')
sfsaltpepper.synopsis('''sfsaltpepper < in.rsf > out.rsf den=10. inten=0.1 rep=n allpos=n noise=n seed=time(NULL)''','''''')
rsf.doc.progs['sfsaltpepper']=sfsaltpepper

