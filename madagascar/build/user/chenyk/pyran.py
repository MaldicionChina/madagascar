sfpyran = rsf.doc.rsfprog('sfpyran','user/chenyk/Mpyran.py','''Add random noise using python.''')
sfpyran.par('axis',rsf.doc.rsfpar('int','2','',''''''))
sfpyran.par('range',rsf.doc.rsfpar('float','1','','''noise range (default=1)'''))
sfpyran.par('seed',rsf.doc.rsfpar('int','n2','','''random seed (default=n2)'''))
sfpyran.par('type',rsf.doc.rsfpar('string','y','','''noise type, y: normal, n: uniform'''))
sfpyran.par('mean',rsf.doc.rsfpar('float','0','','''noise mean (default=0)'''))
sfpyran.par('var',rsf.doc.rsfpar('float','1','','''noise variance (default=1)'''))
sfpyran.par('rep',rsf.doc.rsfpar('bool','n','','''if y, replace data with noise'''))
sfpyran.version('1.7')
sfpyran.synopsis('''sfpyran < pi.rsf > po.rsf axis=2 range=1 seed=n2 type=y mean=0 var=1 rep=n''','''''')
rsf.doc.progs['sfpyran']=sfpyran

