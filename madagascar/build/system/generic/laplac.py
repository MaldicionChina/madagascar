sflaplac = rsf.doc.rsfprog('sflaplac','system/generic/Mlaplac.c','''2-D finite-difference Laplacian operation. ''')
sflaplac.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sflaplac.version('1.7')
sflaplac.synopsis('''sflaplac < in.rsf > out.rsf adj=n''','''''')
rsf.doc.progs['sflaplac']=sflaplac

