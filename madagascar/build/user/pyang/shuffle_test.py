sfshuffle_test = rsf.doc.rsfprog('sfshuffle_test','user/pyang/Mshuffle_test.py','''shuffle the data''')
sfshuffle_test.par('axis',rsf.doc.rsfpar('int','2','',''''''))
sfshuffle_test.par('seed',rsf.doc.rsfpar('int','n2','',''''''))
sfshuffle_test.par('inv',rsf.doc.rsfpar('bool','n','',''''''))
sfshuffle_test.version('1.7')
sfshuffle_test.synopsis('''sfshuffle_test < pi.rsf > po.rsf axis=2 seed=n2 inv=n''','''''')
rsf.doc.progs['sfshuffle_test']=sfshuffle_test

