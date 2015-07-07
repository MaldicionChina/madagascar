sfmpigpufwi = rsf.doc.rsfprog('sfmpigpufwi','user/pyang/Mmpigpufwi.cu','''CUDA based FWI using Enquist absorbing boundary condition''')
sfmpigpufwi.par('shots',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmpigpufwi.par('grads',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmpigpufwi.par('objs',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmpigpufwi.par('illums',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmpigpufwi.par('verb',rsf.doc.rsfpar('bool','y','','''vebosity '''))
sfmpigpufwi.par('precon',rsf.doc.rsfpar('bool','n','','''precondition or not '''))
sfmpigpufwi.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfmpigpufwi.par('rbell',rsf.doc.rsfpar('int','2','','''radius of bell smooth '''))
sfmpigpufwi.version('1.7')
sfmpigpufwi.synopsis('''sfmpigpufwi < vinit.rsf shots=shots.rsf > vupdates.rsf grads=grads.rsf objs=objs.rsf illums=illums.rsf verb=y precon=n niter=100 rbell=2''','''
Note: 	You can try other complex boundary condition but we do not
	recommend to do so. The main reason is that FWI is to recover
	the low-frequency information of the earth model. Low-freq 
	means that exact absorbing is not necessarilly needed. The 
	result will be improved with the optimization precedure. 
	Furthermore, complex boundary condition (such as sponge ABC or
	PML) implies more computational cost, which will degrade the
	efficiency of FWI. 
''')
rsf.doc.progs['sfmpigpufwi']=sfmpigpufwi

