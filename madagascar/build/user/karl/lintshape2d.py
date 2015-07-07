sflintshape2d = rsf.doc.rsfprog('sflintshape2d','user/karl/Mlintshape2d.c','''find grid that will Linearly INTerpolate the input.  Use SHAPEing in 2D.''')
sflintshape2d.par('verbose',rsf.doc.rsfpar('int','1','','''\n
     flag to control amount of print
     0 terse, 1 informative, 2 chatty, 3 debug
  '''))
sflintshape2d.par('xmin',rsf.doc.rsfpar('float','','',''''''))
sflintshape2d.par('xmax',rsf.doc.rsfpar('float','','',''''''))
sflintshape2d.par('ymin',rsf.doc.rsfpar('float','','',''''''))
sflintshape2d.par('ymax',rsf.doc.rsfpar('float','','',''''''))
sflintshape2d.par('dx',rsf.doc.rsfpar('float','','',''''''))
sflintshape2d.par('dy',rsf.doc.rsfpar('float','','',''''''))
sflintshape2d.par('nx',rsf.doc.rsfpar('int','','',''''''))
sflintshape2d.par('ny',rsf.doc.rsfpar('int','','',''''''))
sflintshape2d.version('1.7')
sflintshape2d.synopsis('''sflintshape2d < in.rsf > out.rsf verbose=1 xmin= xmax= ymin= ymax= dx= dy= nx= ny=''','''
Input data is Z, elevation, or amplitude at irregular (x,y) locations.  These 
are just (x,y,z) triplets.  The input file is RSF.  Input file n1 is 3, for 
the (x,y,z) values.  Input file n2 is the number of (x,y,z) points.

The output data is a regularly sampled 2D grid (ie 2D rsf).  

sflintshape2d computes a 2D grid that can be bilinearly interpolated to
fit the input data points.  A conjugate gradient algorithm is used.  The 
equation solved is:
    bilinear_interpolate * 2d_grid ~ irregular_input

Where ~ means "approximately equals".

There may be more than one 2d_grid that will fit the data, so I use 
preconditioning (aka shaping regularization).  Change variables using;

   2d_grid = Smooth * 2d_grid'   

and you obtain:

   bilinear_interpolate * Smooth * 2d_grid' ~ irregular_input

After solving this equation the desired answer is 2d_grid = Smooth * 2d_grid'.

For a smoothing filter I use a 2D box car filter convolved with a 2D boxcar 
filter that is 1/1.5 times smaller.  The smaller filter is intended to reduce
the first sidelobe of the larger filter.

I solve the problem with a very long filter, then repeat with a filter 
1/1.5 times smaller.  I repeat with smaller and smaller filters until the
filter is only a single point (ie no filtering at all.)

This algorithm is a direct implementation of the ideas in Geophysical Image 
Estimation by Example" by Jon Claerbout.  I adopted the left and right 
preconditioning for congugate gradient psuedo code described in "Merits 
and challenges for accurate velocity model building by 3D gridded tomography"
by Guo et al. 

EXAMPLE:

< sxyamp.rsf \\
   sflintshape2d  \\
        verbose=1 \\
        xmin=788150000 xmax=809380000 nx=194 dx=110000 \\
        ymin=939180000 ymax=977020000 ny=345 dy=110000 \\
> s_lintshape.rsf

< s_lintshape.rsf sfclip2 lower=0.34461 upper=2.46485 \\
| sfmath output="input-1.4" \\
| sfgrey title="s_lintshape2d shot scalar" color=j \\
| sfpen

This example grids the shot consistant amplitude (sxyamp.rsf) estimated on the 
teapot dome 3D land survey.  The 2d grid s_lintshape.rsf is clipped, biased, 
and plotted (sfgrey | sfpen)

''')
rsf.doc.progs['sflintshape2d']=sflintshape2d

