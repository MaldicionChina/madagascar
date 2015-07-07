sfleftsize = rsf.doc.rsfprog('sfleftsize','user/ivlad/Mleftsize.c','''Computes Ni+1 x Ni+2 x ...''')
sfleftsize.par('i',rsf.doc.rsfpar('int','0','','''What size to start counting from. i=0 gets total number of elements '''))
sfleftsize.version('1.7')
sfleftsize.synopsis('''sfleftsize < in.rsf i=0''','''Wrapper for sf_leftsize''')
rsf.doc.progs['sfleftsize']=sfleftsize

