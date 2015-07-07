sfsparsify = rsf.doc.rsfprog('sfsparsify','user/ivlad/Msparsify.c','''Transforms regular 2-D array to sparse array''')
sfsparsify.par('nonzero',rsf.doc.rsfpar('int','n1*n2','','''Number of nonzero elements in input '''))
sfsparsify.version('1.7')
sfsparsify.synopsis('''sfsparsify < in.rsf > out.rsf nonzero=n1*n2''','''Input is int or float array
Output is a float nonzero-by-3 array, where 
nonzero=`<input.rsf sfattr want=nonzero | awk -F '= ' '{ print $2 }';`
column 0 holds the data values (converted from int to float, if necessary),
column 1 holds coordinate values (i.e. o+i*d, not indices i) for dimension
1 of input, and column 2 the coordinate values for dimension 2 of input ''')
rsf.doc.progs['sfsparsify']=sfsparsify

