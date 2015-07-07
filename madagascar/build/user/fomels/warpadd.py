sfwarpadd = rsf.doc.rsfprog('sfwarpadd','user/fomels/Mwarpadd.c','''Add a perturbation to the warping function.''')
sfwarpadd.par('add',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwarpadd.par('accuracy',rsf.doc.rsfpar('int','','','''Interpolation accuracy order '''))
sfwarpadd.par('m1',rsf.doc.rsfpar('int','n1*2','','''Trace pading '''))
sfwarpadd.version('1.7 Mwarpadd.c 7107 2011-04-10 02:04:14Z ivlad')
sfwarpadd.synopsis('''sfwarpadd < in.rsf add=add.rsf > sum.rsf accuracy= m1=n1*2''','''''')
rsf.doc.progs['sfwarpadd']=sfwarpadd

