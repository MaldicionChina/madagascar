sflistminmax = rsf.doc.rsfprog('sflistminmax','user/jennings/Mlistminmax.c','''Construct incremental minimum or maximum lists from an RSF file.''')
sflistminmax.par('mode',rsf.doc.rsfpar('string ',desc=''''min' (default) or 'max' '''))
sflistminmax.version('1.7 Mlistminmax.c 4796 2009-09-29 19:39:07Z ivlad')
sflistminmax.synopsis('''sflistminmax < in.rsf > out.rsf mode=''','''
Constructs the following set of minimum or maximum lists for each
x2, x3, ... xn in the input RSF file:

out[0] = in[0]
out[i] = min or max of (in[i], out[i-1]) for i = 1, 2, 3, ... n1

The input file data type must be float.
The output file data type will be float.

sflistminmax mode=min, can be used to simulate "erosion" for a set of 
geological surfaces, producing a new set of surfaces that do not cross.

See also: sfminmax, sfstack.
''')
rsf.doc.progs['sflistminmax']=sflistminmax

