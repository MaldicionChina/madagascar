sfshuffle = rsf.doc.rsfprog('sfshuffle','user/chen/Mshuffle.py','''shuffle the data''')
sfshuffle.par('axis',rsf.doc.rsfpar('int','2','',''''''))
sfshuffle.par('seed',rsf.doc.rsfpar('int','n2','',''''''))
sfshuffle.par('inv',rsf.doc.rsfpar('bool','n','',''''''))
sfshuffle.version('1.7')
sfshuffle.synopsis('''sfshuffle < pi.rsf > po.rsf axis=2 seed=n2 inv=n''','''''')
rsf.doc.progs['sfshuffle']=sfshuffle

