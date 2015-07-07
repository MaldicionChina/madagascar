sflineiko = rsf.doc.rsfprog('sflineiko','user/llisiw/Mlineiko.c','''Iterative solution of the linearized eikonal equation. ''')
sflineiko.par('time',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflineiko.par('slow',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflineiko.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflineiko.par('squared',rsf.doc.rsfpar('bool','y','','''if slowness is squared '''))
sflineiko.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag (for what=linear) '''))
sflineiko.par('inv',rsf.doc.rsfpar('bool','n','','''inverse flag (for what=linear) '''))
sflineiko.par('niter',rsf.doc.rsfpar('int','1','','''maximum number of iterations '''))
sflineiko.par('tol',rsf.doc.rsfpar('float','0.001','','''tolerance for convergence '''))
sflineiko.par('what',rsf.doc.rsfpar('string ',desc='''what to compute '''))
sflineiko.par('time',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sflineiko.par('time',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sflineiko.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sflineiko.version('1.7')
sflineiko.synopsis('''sflineiko < time.rsf > dtime.rsf time=time0.rsf slow=slow.rsf mask=mask.rsf squared=y adj=n inv=n niter=1 tol=0.001 what=''','''''')
rsf.doc.progs['sflineiko']=sflineiko

