import rsf.doc

sfkarlpocs = rsf.doc.rsfprog('sfkarlpocs','user/karl/Mkarlpocs.c','''n-D POCS interpolation using a general Lp-norm optimization''')
sfkarlpocs.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkarlpocs.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfkarlpocs.par('niter',rsf.doc.rsfpar('int','100','','''total number iterations '''))
sfkarlpocs.par('pclip',rsf.doc.rsfpar('float','10.','','''starting data clip percentile (default is 99)'''))
sfkarlpocs.par('n#',rsf.doc.rsfpar('int','','','''size of #-th axis '''))
sfkarlpocs.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfkarlpocs.version('1.7')
sfkarlpocs.synopsis('''sfkarlpocs < in.rsf > out.rsf mask=Fmask.rsf verb=n niter=100 pclip=10. n#=''','''   Note: Acquistion geometry represented by mask operator.
''')
rsf.doc.progs['sfkarlpocs']=sfkarlpocs

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

sfmake_ix_indx = rsf.doc.rsfprog('sfmake_ix_indx','user/karl/Mmake_ix_indx.c','''MAKE Iline Xline INDX files for quick 3D data subsets (superbins)''')
sfmake_ix_indx.par('verbose',rsf.doc.rsfpar('int','1','','''\n
     flag to control amount of print
     0 terse, 1 informative, 2 chatty, 3 debug
  '''))
sfmake_ix_indx.par('ilinemin',rsf.doc.rsfpar('float','-1e31','','''\n
     minimum "iline" header key to include in the index.  Use this parameter
     to remove null trace headers or traces outside project area.
  '''))
sfmake_ix_indx.par('ilinemax',rsf.doc.rsfpar('float','-1e31','','''\n
     maximum "iline" header key to include in the index.  Use this parameter
     to remove null trace headers or traces outside project area.
  '''))
sfmake_ix_indx.par('xlinemin',rsf.doc.rsfpar('float','-1e31','','''\n
     minimum "xline" header key to include in the index.  Use this parameter
     to remove null trace headers or traces outside project area.
  '''))
sfmake_ix_indx.par('xlinemax',rsf.doc.rsfpar('float','-1e31','','''\n
     maximum "xline" header key to include in the index.  Use this parameter
     to remove null trace headers or traces outside project area.
  '''))
sfmake_ix_indx.par('ilineinc',rsf.doc.rsfpar('int','10','','''\n
     incrment in iline for the index
  '''))
sfmake_ix_indx.par('input',rsf.doc.rsfpar('string ',desc='''\n
     Input file for traces amplitudes
  '''))
sfmake_ix_indx.par('headers',rsf.doc.rsfpar('string ',desc='''\n
     Trace header file name.  Default is the input data file
     name, with the final .rsf changed to _hdr.rsf 
  '''))
sfmake_ix_indx.par('iline',rsf.doc.rsfpar('string ',desc='''\n
     header key for the main index key.  This should be iline, but you 
     may have non-standard trace headers or a wierd use of this program 
  '''))
sfmake_ix_indx.par('xline',rsf.doc.rsfpar('string ',desc=''''''))
sfmake_ix_indx.par('indxdir',rsf.doc.rsfpar('string ',desc='''\n
     The name of the directory containing the iline,xline index.  This 
     directory will be in DATAPATH (probably the environment variable). The 
     directory also continues a file "filenames", a list of the trace and 
     header files that contributes to this index. The directory contains files 
     with names "indx#" here # is an integer multiple of ilineinc. These files 
     contains a record for each contributing trace with filenumber, 
     tracenumber, and the trace header. The file containing the trace is 
     determined using the  can be read by using the filenumber and the 
     "filenames" file.  The tracenumber defines the location of the trace 
     in the file.
  '''))
sfmake_ix_indx.version('1.7')
sfmake_ix_indx.synopsis('''sfmake_ix_indx < infile.rsf > out.rsf verbose=1 ilinemin=-1e31 ilinemax=-1e31 xlinemin=-1e31 xlinemax=-1e31 ilineinc=10 input= headers= iline= xline= indxdir=''','''
These indexes are intended to be used by future sftahsort and sftah5dinterp.

EXAMPLE:
Runnning the programs:

sfmake_ix_indx           \\
   verbose=1             \\
   input=npr3_fielda.rsf \\
   indxdir=npr3_field    \\
   ilineinc=10           \\
   iline=iline           \\
   xline=xline           \\
   append=no             \\
>/dev/null 
sfmake_ix_indx           \\
   verbose=1             \\
   input=npr3_fieldb.rsf \\
   indxdir=npr3_field    \\
   ilineinc=10           \\
   iline=iline           \\
   xline=xline           \\
   append=yes            \\
>/dev/null 

Will create a set of files:
npr3_field/il0
npr3_field/il5
...
npr3_field/il350
and
npr3_field/filename_indx

The file npr3_field/il15 will contain the trace headers of the traces with 
trace header "iline" nearest to 15.  The file also has the file number and
the trace number, so you can locate the trace in the input files (either 
npr3_fielda.rsf or npr3_fieldb.rsf.  The trace headers in the file are all 
sorted by xline.  With this information you can quickly find all the traces
that are in a range of ilines and xlines.  This supports sftah5dinterp which
processes all the traces in a midpoint superbin that might be 800 meters by 800
meters (about 16 ilines and 32 xlines).  This is not a simple sort problem 
because sftah5dinterp processes data in overlapping bin (i.e. the 800 meter 
superbin centers moveup by 400 meters).  Overlapping superbins are supported by
allowing traces to be reread.

The program also allows sftahsort to read from multiple files. This is useful
on larger 3D projects where the input data is on multiple segy files.  
Previously I merged the files into one big file after running sfsegyread.  This
required an additional copy of all the data to be saved on disk.    
''')
rsf.doc.progs['sfmake_ix_indx']=sfmake_ix_indx

sftahgethw = rsf.doc.rsfprog('sftahgethw','user/karl/Mtahgethw.c','''Trace And Header GET Header Word prints trace headers.''')
sftahgethw.par('key',rsf.doc.rsfpar('strings','','',''' [numkeys]'''))
sftahgethw.par('verbose',rsf.doc.rsfpar('int','1','','''\n
     flag to control amount of print
     0 terse, 1 informative, 2 chatty, 3 debug
  '''))
sftahgethw.version('1.7')
sftahgethw.synopsis('''sftahgethw < in.rsf > out.rsf key= verbose=1''','''
tah is the abbreviation of Trace And Header.  Madagascar programs 
that begin with sftah are a designed to:
1- read trace and headers from separate rsf files and write them to 
   standard output (ie sftahread)
2- filter programs that read and write standard input/output and 
   process the tah data (eg sftahnmo, sftahstack)
3- read tah data from standard input and write separate rsf files for 
   the trace and headers data (ie sftahwrite)

These programs allow Seismic Unix (su) like processing in Madagascar.  
Some programs have su like names.

Some programs in this suite are sftahread, sftahgethw, ftahhdrmath, 
and sftahwrite.

The sftahgethw program prints headers.  List the headers you want to
print in the key parameter.
EXAMPLE:

sftahread \\
   verbose=1 \\
   input=npr3_gathers.rsf \\
| sftahgethw \\
   verbose=0  \\
   key=sx,sy,gx,gy,offset  \\
>/dev/null

The headers are in the file npr3_gathers_hdr.rsf, 
the headers parameter default.  The headers are merged with the trace 
amplitudes and the tah data sent down the pipe for sftahgethw.  The 
source and group coordinates and offset (sx,sy,gx,gy,offset) are 
printed to STDERR.  Traces are sent to STDOUT, which is directed to
/dev/null (the bit bucket).

PARAMETERS
   string key= no default

        list of header keys print.  Look at the sfsegyread for a list
	of header names.

''')
rsf.doc.progs['sftahgethw']=sftahgethw

sftahread = rsf.doc.rsfprog('sftahread','user/karl/Mtahread.c','''Read Trace And Header from separate files, combine, write to pipe''')
sftahread.par('verbose',rsf.doc.rsfpar('int','1','','''\n
     flag to control amount of print
     0 terse, 1 informative, 2 chatty, 3 debug
  '''))
sftahread.par('input',rsf.doc.rsfpar('string ',desc='''\n
     Input file for traces amplitudes
  '''))
sftahread.par('headers',rsf.doc.rsfpar('string ',desc='''\n
     Trace header file name.  Default is the input data file
     name, with the final .rsf changed to _hdr.rsf 
  '''))
sftahread.version('1.7')
sftahread.synopsis('''sftahread < infile.rsf > out.rsf verbose=1 input= headers=''','''
tah is the abbreviation of Trace And Header.  Madagascar programs 
that begin with sftah are designed to:
1- read trace and headers from separate rsf files and write them to 
   standard output (ie sftahread)
2- filter programs that read and write standard input/output and 
   process the tah data (eg sftahnmo, sftahstack)
3- read tah data from standard input and write separate rsf files for 
   the trace and headers data (ie sftahwrite)

These programs allow Seismic Unix (su) like processing in Madagascar.  
Some programs have su like names.

Some programs in this suite are sftahread, sftahgethw, ftahhdrmath, 
and sftahwrite.

EXAMPLE:

sftahread \\
   verbose=1 \\
   input=npr3_gathers.rsf \\
| sftahnmo \\
   verbose=1  \\
   tnmo=0,.373,.619,.826,.909,1.017,1.132,1.222,1.716,3.010 \\
   vnmo=9086,10244,11085,10803,10969,11578,12252,12669,14590,17116 \\
| sftahstack key=iline,xline verbose=1 \\
| sftahwrite \\
   verbose=1                           \\
   label2="xline" o2=1 n2=188 d2=1   \\
   label3="iline" o3=1 n3=345 d3=1   \\
   output=mappedstack.rsf \\
>/dev/null

sfgrey <mappedstack.rsf | sfpen

In this example the cmp sorted prestack data, npr3_gathers.rsf,  are 
read by sftahread.  The headers are in the file npr3_gathers_hdr.rsf, 
the headers parameter default.  The headers are merged with the trace 
amplitudes and the tah data sent down the pipe for nmo and stack.  The 
sftahwrite writes the trace data to mappedstack.rsf and the headers 
are written to the file mappedstack_hdr.rsf.  The order of the data in
the output file is defined by the iline and xline trace headers, so the 
data order is (time,xline,iline).  Finally, the output volume is
displayed using sfgrey.
''')
rsf.doc.progs['sftahread']=sftahread

sftahwrite = rsf.doc.rsfprog('sftahwrite','user/karl/Mtahwrite.c','''Read Trace And Header (tah) from standard input, write to separate files''')
sftahwrite.par('verbose',rsf.doc.rsfpar('int','1','','''\n
     flag to control amount of print
     0 terse, 1 informative, 2 chatty, 3 debug
  '''))
sftahwrite.par('label#',rsf.doc.rsfpar('string','(2,...)','','''name of each of the axes. 
	   label1 is not changed from input. Each label must be a 
	   header key like cdp, cdpt, or ep.  The trace header 
	   values are used to define the output trace location in
	   the output file. '''))
sftahwrite.par('n#',rsf.doc.rsfpar('largeint','(2,...)','','''number of locations in the #-th dimension '''))
sftahwrite.par('o#',rsf.doc.rsfpar('float','(2,...)','','''origin of the #-th dimension '''))
sftahwrite.par('d#',rsf.doc.rsfpar('float','(2,...)','','''delta in the #-th dimension '''))
sftahwrite.par('output',rsf.doc.rsfpar('string ',desc='''\n
     output trace filename. Required parameter with no default.
  '''))
sftahwrite.par('outheaders',rsf.doc.rsfpar('string ',desc='''\n
     Output trace header file name.  Default is the input data
     file name, with the final .rsf changed to _hdr.rsf. 
  '''))
sftahwrite.version('1.7')
sftahwrite.synopsis('''sftahwrite < in.rsf > out.rsf verbose=1 label#=(2,...) n#=(2,...) o#=(2,...) d#=(2,...) output= outheaders=''','''
tah is the abbreviation of Trace And Header.  Madagascar programs 
that begin with sftah are a designed to:
1- read trace and headers from separate rsf files and write them to 
   standard output (ie sftahread)
2- filter programs that read and write standard input/output and 
   process the tah data (eg sftahnmo, sftahstack)
3- read tah data from standard input and write separate rsf files for 
   the trace and headers data (ie sftahwrite)

These programs allow Seismic Unix (su) like processing in Madagascar.  
Some programs have su like names.

Some programs in this suite are sftahread, sftahgethw, ftahhdrmath, 
and sftahwrite.

The sftahwrite program reads the trace and header data (tah) from 
standard input (usually a pipe), separates the trace data from the
header data.  The trace data is written to output and the header is
written to outheaders.  The trace headers are used to select the 
location in the file to write the data.  The iline and xline headers 
are used in the following example to put stacked data in 
(time, xline, iline) order so it can be viewed using sfgrey.

EXAMPLE:

sftahread \\
   verbose=1 \\
   input=npr3_gathers.rsf \\
| sftahnmo \\
   verbose=1  \\
   tnmo=0,.373,.619,.826,.909,1.017,1.132,1.222,1.716,3.010 \\
   vnmo=9086,10244,11085,10803,10969,11578,12252,12669,14590,17116 \\
| sftahstack key=iline,xline verbose=1 \\
| sftahwrite \\
   verbose=1                           \\
   label2="xline" o2=1 n2=188 d2=1   \\
   label3="iline" o3=1 n3=345 d3=1   \\
   output=mappedstack.rsf \\
>/dev/null

sfgrey <mappedstack.rsf | sfpen

In this example the cmp sorted prestack data, npr3_gathers.rsf,  are 
read by sftahread.  The headers are in the file npr3_gathers_hdr.rsf, 
the headers parameter default.  The headers are merged with the trace 
amplitudes and the tah data sent down the pipe for nmo and stack.  The 
sftahwrite writes the trace data to mappedstack.rsf and the headers 
are written to the file mappedstack_hdr.rsf.  The order of the data in
the output file is defined by the iline and xline trace headers, so the 
data order is (time,xline,iline).  Finally, the output volume is
displayed using sfgrey.
''')
rsf.doc.progs['sftahwrite']=sftahwrite

sftahnmo = rsf.doc.rsfprog('sftahnmo','user/karl/Mtahnmo.c','''Trace And Header Normal MoveOut''')
sftahnmo.par('vnmo',rsf.doc.rsfpar('floats','','','''list of NMO velocities for the tnmo times.  [numvnmo]'''))
sftahnmo.par('tnmo',rsf.doc.rsfpar('floats','','','''list of NMO times for the vnmo velocities.  [numtnmo]'''))
sftahnmo.par('verbose',rsf.doc.rsfpar('int','1','','''\n
     flag to control amount of print
     0 terse, 1 informative, 2 chatty, 3 debug
  '''))
sftahnmo.par('str',rsf.doc.rsfpar('float','0.5','','''maximum stretch allowed '''))
sftahnmo.par('lmute',rsf.doc.rsfpar('float','12.*d1','','''length of the mute zone in seconds '''))
sftahnmo.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse nmo.  Otherwise forward nmo '''))
sftahnmo.version('1.7')
sftahnmo.synopsis('''sftahnmo < in.rsf > out.rsf vnmo= tnmo= verbose=1 str=0.5 lmute=12.*d1 inv=n''','''
tah is the abbreviation of Trace And Header.  Madagascar programs 
that begin with sftah are a designed to:
1- read trace and headers from separate rsf files and write them to 
   standard output (ie sftahread)
2- filter programs that read and write standard input/output and 
   process the tah data (eg sftahnmo, sftahstack)
3- read tah data from standard input and write separate rsf files for 
   the trace and headers data (ie sftahwrite)

These programs allow Seismic Unix (su) like processing in Madagascar.  
Some programs have su like names.

Some programs in this suite are sftahread, sftahgethw, ftahhdrmath, 
and sftahwrite.

The sftahnmo uses offset in the trace headers to apply moveout using 
the velocity function defined in the tnmo= vnmo= parameters. Largely
based on the seismic unix program sunmo.

NMO interpolation error is less than 1% for frequencies less than 60% of
the Nyquist frequency. 
                                                                             
Exact inverse NMO is impossible, particularly for early times at large
offsets and for frequencies near Nyquist with large interpolation 
errors.  
 

EXAMPLE:

sftahread \\
   verbose=1 \\
   input=npr3_gathers.rsf \\
| sftahnmo \\
   verbose=1  \\
   tnmo=0,.373,.619,.826,.909,1.017,1.132,1.222,1.716,3.010 \\
   vnmo=9086,10244,11085,10803,10969,11578,12252,12669,14590,17116 \\
| sftahstack key=iline,xline verbose=1 \\
| sftahwrite \\
   verbose=1                           \\
   label2="xline" o2=1 n2=188 d2=1   \\
   label3="iline" o3=1 n3=345 d3=1   \\
   output=mappedstack.rsf \\
>/dev/null

sfgrey <mappedstack.rsf | sfpen

In this example the cmp sorted prestack data, npr3_gathers.rsf,  are 
read by sftahread.  The headers are in the file npr3_gathers_hdr.rsf, 
the headers parameter default.  The headers are merged with the trace 
amplitudes and the tah data sent down the pipe for nmo and stack.  The
sftahstack program uses both the iline and xline keys to determine
which traces blong to a gather.  Using both keys avoids a problem on 
edges of a survey when uising xline along may merge gathers across 
ilines (a special case that does sometimes happen). sftahwrite writes
the trace data to mappedstack.rsf and the headers are written to the
file mappedstack_hdr.rsf.  The order of the data in the output file
is defined by the iline and xline trace headers, so the  data order
is (time,xline,iline).  Finally, the output volume is displayed using
sfgrey.
''')
rsf.doc.progs['sftahnmo']=sftahnmo

sftahmakeskey = rsf.doc.rsfprog('sftahmakeskey','user/karl/Mtahmakeskey.c','''Trace And Header MAKE Secondary KEY.''')
sftahmakeskey.par('key',rsf.doc.rsfpar('strings','','',''' [numkeys]'''))
sftahmakeskey.par('verbose',rsf.doc.rsfpar('int','1','','''\n
     flag to control amount of print
     0 terse, 1 informative, 2 chatty, 3 debug
  '''))
sftahmakeskey.par('skey',rsf.doc.rsfpar('string ',desc='''The name of the secondary key created by the program. '''))
sftahmakeskey.version('1.7')
sftahmakeskey.synopsis('''sftahmakeskey < in.rsf > out.rsf key= verbose=1 skey=''','''
tah is the abbreviation of Trace And Header.  Madagascar programs 
that begin with sftah are a designed to:
1- read trace and headers from separate rsf files and write them to 
   standard output (ie sftahread)
2- filter programs that read and write standard input/output and 
   process the tah data (eg sftahnmo, sftahstack)
3- read tah data from standard input and write separate rsf files for 
   the trace and headers data (ie sftahwrite)

These programs allow Seismic Unix (su) like processing in Madagascar.  
Some programs have su like names.

Some programs in this suite are sftahread, sftahgethw, ftahhdrmath, 
and sftahwrite.

The sftahmakeskey program will make a secondary key.  You sometimes
need a secondary key to number the traces in a gather.  For example 
after sorting the data in iline,xline,offset you usually cannot
store the data using the offset key because the offset sampling is 
irregular.  sftahmakeskey can be used to build the cdpt header from 
the iline and xline keys.  The secondary key, skey, will start with 
1 when a new iline,xline is encounterred.  As long as iline,xline
does not change, he skey will increase by 1 on each successive trace
until the iline,xline changes.  The output data can be stored in a 
file indexed by cdpt,xline,iline.

EXAMPLE:

sftahread \\
   verbose=1 \\
   input=npr3_gathers.rsf \\
| sftahmakeskey key=iline,xline skey=cdpt verbose=1 \\
| sftahwrite \\
   verbose=1                         \\
   label2="cdpt"  o2=1 n2=24  n2=1   \\
   label3="xline" o3=1 n3=188 d3=1   \\
   label4="iline" o4=1 n4=10 d4=1   \\
   output=mappedgather.rsf \\
>/dev/null

sfgrey <mappedgather.rsf | sfpen

In this example the cmp sorted prestack data, npr3_gathers.rsf,  are 
read by sftahread.  The headers are in the file npr3_gathers_hdr.rsf, 
the headers parameter default.  The headers are merged with the trace 
amplitudes and the tah data sent down the pipe for sftahmakeskey.
sftahmakeskey creates the cdpt header and sftahwrite creates a 4 
dimensional file.

PARAMETERS
   strings key= no default

        list of header keys to monitor to determine when to break 
	between gathers.  A gather is a sequence of traces with the 
	same value for all the header keys.  Stack summs traces in 
	the gather, divides by the fold, and outputs the stack trace.c
''')
rsf.doc.progs['sftahmakeskey']=sftahmakeskey

sftahstack = rsf.doc.rsfprog('sftahstack','user/karl/Mtahstack.c','''Read Trace And Header (tah) from STDIN, stack matching header keys''')
sftahstack.par('key',rsf.doc.rsfpar('strings','','',''' [numkeys]'''))
sftahstack.par('xmute',rsf.doc.rsfpar('floats','','',''' [numxmute]'''))
sftahstack.par('tmute',rsf.doc.rsfpar('floats','','',''' [numtmute]'''))
sftahstack.par('verbose',rsf.doc.rsfpar('int','1','','''\n
     flag to control amount of print
     0 terse, 1 informative, 2 chatty, 3 debug
  '''))
sftahstack.par('ntaper',rsf.doc.rsfpar('int','12','','''\n
       length of the taper on the stack mute
    '''))
sftahstack.version('1.7')
sftahstack.synopsis('''sftahstack < in.rsf > out.rsf key= xmute= tmute= verbose=1 ntaper=12''','''
tah is the abbreviation of Trace And Header.  Madagascar programs 
that begin with sftah are a designed to:
1- read trace and headers from separate rsf files and write them to 
   standard output (ie sftahread)
2- filter programs that read and write standard input/output and 
   process the tah data (eg sftahnmo, sftahstack)
3- read tah data from standard input and write separate rsf files for 
   the trace and headers data (ie sftahwrite)

These programs allow Seismic Unix (su) like processing in Madagascar.  
Some programs have su like names.

Some programs in this suite are sftahread, sftahgethw, ftahhdrmath, 
and sftahwrite.

The sftahstack program is designed to stack sorted data. Trace and 
header data (tah) are read from from standard input (usually a pipe).
Gathers to be stacked are defined by the input parameter \'key\'.
The key parameter is a list of header keys to watch.  A new gather 
starts when one of the header keys change.  On each gather the stack
trace is initialized to zero, traces in the gather are summed, and
the stack trace is divided by the time variant fold, and the stacked
trace written to output.  The output trace header is taken from the
first trace in the input gather.    

EXAMPLE:

sftahread \\
   verbose=1 \\
   input=npr3_gathers.rsf \\
| sftahnmo \\
   verbose=1  \\
    tnmo=0,2,6,10.5,16 vnmo=1500,1500,2250,3250,3700  \\
| sftahstack key=iline,xline \
    xmute=0,20000 tmute=0,20 ntaper=25 \\
| sftahwrite \\
   verbose=1                           \\
   label2="xline" o2=1 n2=188 d2=1   \\
   label3="iline" o3=1 n3=345 d3=1   \\
   output=mappedstack.rsf \\
>/dev/null

sfgrey <mappedstack.rsf | sfpen

In this example the cmp sorted prestack data, npr3_gathers.rsf,  are 
read by sftahread.  The headers are in the file npr3_gathers_hdr.rsf, 
the headers parameter default.  The headers are merged with the trace 
amplitudes and the tah data sent down the pipe for nmo and stack.  The
sftahstack program uses both the iline and xline keys to determine
which traces blong to a gather.  Using both keys avoids a problem on 
edges of a survey when uising xline along may merge gathers across 
ilines (a special case that does sometimes happen). sftahwrite writes
the trace data to mappedstack.rsf and the headers are written to the
file mappedstack_hdr.rsf.  The order of the data in the output file
is defined by the iline and xline trace headers, so the  data order
is (time,xline,iline).  Finally, the output volume is displayed using
sfgrey.

PARAMETERS
   strings key= no default

        list of header keys to monitor to determine when to break 
	between gathers.  A gather is a sequence of traces with the 
	same value for all the header keys.  Stack summs traces in 
	the gather, divides by the fold, and outputs the stack trace.

   floats xmute= NULL

        List of floats the same length as list of floats in the tmute
	parameter.  The (xmute,tmute) pairs are interpolated using the
	trace headers offset to determine trace start time.  The mute is
	always increased to the first non-zero sample.  The default mutes 
	at the first non-zero sample.

   floats tmute= NULL

        List of floats the same length as list of floats in the xmute
	parameter.  The (xmute,tmute) pairs are interpolated using the
	trace headers offset to determine trace start time. The mute is
	always increased to the first non-zero sample.  The default mutes 
	at the first non-zero sample.

   float ntaper=12
        the length of the taper to use at the start of the trace.
	
''')
rsf.doc.progs['sftahstack']=sftahstack

sftahsort = rsf.doc.rsfprog('sftahsort','user/karl/Mtahsort.c','''Read Trace And Header from separate files in sorted order, write to pipe''')
sftahsort.par('verbose',rsf.doc.rsfpar('int','1','','''\n
     flag to control amount of print
     0 terse, 1 informative, 2 chatty, 3 debug
  '''))
sftahsort.par('input',rsf.doc.rsfpar('string ',desc='''\n
     Input file for traces amplitudes
  '''))
sftahsort.par('headers',rsf.doc.rsfpar('string ',desc='''\n
     Trace header file name.  Default is the input data file
     name, with the final .rsf changed to _hdr.rsf 
  '''))
sftahsort.par('sort',rsf.doc.rsfpar('string ',desc='''\n
     list of the sort keys.  Each key must be a trace header key name.
     It may be preceeded with + (the default) for ascending or - for 
     descending sort direction.  The key may be followed with :min,max 
     or :min,max,inc.  These parameters allow you to select a subset of 
     of the traces based on the header key.  The sort keys are blank
     seperated you should enclose the sort string in \"\'s.  Examples are
     sort=\"iline xline offset\" and sort=\"cdp:100,500,25 offset\"
  '''))
sftahsort.version('1.7')
sftahsort.synopsis('''sftahsort < infile.rsf > out.rsf verbose=1 input= headers= sort=''','''
tah is the abbreviation of Trace And Header.  Madagascar programs 
that begin with sftah are designed to:
1- read trace and headers from separate rsf files and write them to 
   standard output (ie sftahread)
2- filter programs that read and write standard input/output and 
   process the tah data (eg sftahnmo, sftahstack)
3- read tah data from standard input and write separate rsf files for 
   the trace and headers data (ie sftahwrite)

These programs allow Seismic Unix (su) like processing in Madagascar.  
Some programs have su like names.

Some programs in this suite are sftahread, sftahgethw, ftahhdrmath, 
and sftahwrite.

EXAMPLE:

sftahsort               \\
   verbose=1            \\
   input=npr3_field.rsf \\
   sort="iline:100,200,50  +xline:100,140,10 offset" \\
| sftahmakeskey pkey=iline,xline skey=cdpt verbose=1 \\
| sftahwrite \\
   verbose=1 \\                          
   label2="cdpt"  o2=1 n2=50  d2=1    \\
   label3="xline" o3=100 n3=5 d3=10   \\
   label4="iline" o4=100 n4=3  d4=50  \\
   output=mappedfieldsort.rsf         \\
>/dev/null

sfgrey <mappedstack.rsf | sfpen

In this example the cmp sorted prestack data, npr3_gathers.rsf,  are 
read by sftahread.  The headers are in the file npr3_gathers_hdr.rsf, 
the headers parameter default.  The headers are merged with the trace 
amplitudes and the tah data sent down the pipe for nmo and stack.  The 
sftahwrite writes the trace data to mappedstack.rsf and the headers 
are written to the file mappedstack_hdr.rsf.  The order of the data in
the output file is defined by the iline and xline trace headers, so the 
data order is (time,xline,iline).  Finally, the output volume is
displayed using sfgrey.
''')
rsf.doc.progs['sftahsort']=sftahsort

sftahscscale = rsf.doc.rsfprog('sftahscscale','user/karl/Mtahscscale.c','''Surface Consistant SCALE - Compute & apply surface consistant scale''')
sftahscscale.par('verbose',rsf.doc.rsfpar('int','1','','''\n
     flag to control amount of print
     0 terse, 1 informative, 2 chatty, 3 debug
  '''))
sftahscscale.par('starttime',rsf.doc.rsfpar('float','o1','','''start time to compute average trace ampltide '''))
sftahscscale.par('endtime',rsf.doc.rsfpar('float','(n1_traces-1)*d1+o1','',''''''))
sftahscscale.par('input',rsf.doc.rsfpar('string ',desc='''\n
     Input file for traces amplitudes
  '''))
sftahscscale.par('headers',rsf.doc.rsfpar('string ',desc='''\n
     Trace header file name.  Default is the input data file
     name, with the final .rsf changed to _hdr.rsf 
  '''))
sftahscscale.par('sxy',rsf.doc.rsfpar('string ',desc=''''''))
sftahscscale.par('gxy',rsf.doc.rsfpar('string ',desc=''''''))
sftahscscale.par('sxyamp',rsf.doc.rsfpar('string ',desc=''''''))
sftahscscale.par('gxyamp',rsf.doc.rsfpar('string ',desc=''''''))
sftahscscale.version('1.7')
sftahscscale.synopsis('''sftahscscale < infile.rsf > out.rsf verbose=1 starttime=o1 endtime=(n1_traces-1)*d1+o1 input= headers= sxy= gxy= sxyamp= gxyamp=''','''
tah is the abbreviation of Trace And Header.  Madagascar programs 
that begin with sftah are designed to:
1- read trace and headers from separate rsf files and write them to 
   standard output (ie sftahread)
2- filter programs that read and write standard input/output and 
   process the tah data (eg sftahnmo, sftahstack)
3- read tah data from standard input and write separate rsf files for 
   the trace and headers data (ie sftahwrite)

These programs allow Seismic Unix (su) like processing in Madagascar.  
Some programs have su like names.

Some programs in this suite are sftahread, sftahgethw, ftahhdrmath, 
and sftahwrite.

EXAMPLE:

  sftahscscale \\
    input=../fetch/npr3_field.rsf \\
    sxy=sxy.rsf       gxy=gxy.rsf \\
    sxyamp=sxyamp.rsf gxyamp=gxyamp.rsf \\
  | sftahwrite \\
    verbose=1                           \\
    label2="ep"  o2=14 n2=850  d2=1   \\
    label3="tracf" o3=1 n3=1063 d3=1    \\
    output=scscale.rsf \\
  >/dev/null

sfgrey <scscale.rsf | sfpen

In this example the input data ../fetch/npr_field.rsf is read.  Trace
order does not matter.  Seems like shot oriented data is likely, but
the program will process cdp of receiver gathers. the source x,y 
coorfinates are written to sxy.rsaf and the group x,y coordinates are 
written to gxy.rsf. The shot consistant amplitude and the shot x,y is 
written to sxyamp.rsf.  The group consistant amplitude and the group 
x,y is written to gxyamp.rsf.  Surface consistant scaling is applied 
to the data and the resulting trace and header is written to the pipe.
The sftahwrite writes the trace data to scscale.rsf and the headers 
are written to the file scscale_hdr.rsf.  Finally, the output volume 
is displayed using sfgrey.
''')
rsf.doc.progs['sftahscscale']=sftahscscale

sftahmakeevent = rsf.doc.rsfprog('sftahmakeevent','user/karl/Mtahmakeevent.c','''Trace And Header MAKEEVENT makes constant velocity dipping event synthetic.''')
sftahmakeevent.par('verbose',rsf.doc.rsfpar('int','1','','''\n
     flag to control amount of print
     0 terse, 1 informative, 2 chatty, 3 debug
  '''))
sftahmakeevent.par('v',rsf.doc.rsfpar('float','','',''''''))
sftahmakeevent.par('dx',rsf.doc.rsfpar('float','','',''''''))
sftahmakeevent.par('dy',rsf.doc.rsfpar('float','','',''''''))
sftahmakeevent.par('x0',rsf.doc.rsfpar('float','','',''''''))
sftahmakeevent.par('y0',rsf.doc.rsfpar('float','','',''''''))
sftahmakeevent.par('t0',rsf.doc.rsfpar('float','','','''****************************************'''))
sftahmakeevent.version('1.7')
sftahmakeevent.synopsis('''sftahmakeevent < in.rsf > out.rsf verbose=1 v= dx= dy= x0= y0= t0=''','''
tah is the abbreviation of Trace And Header.  Madagascar programs 
that begin with sftah are a designed to:
1- read trace and headers from separate rsf files and write them to 
   standard output (ie sftahread)
2- filter programs that read and write standard input/output and 
   process the tah data (eg sftahnmo, sftahstack)
3- read tah data from standard input and write separate rsf files for 
   the trace and headers data (ie sftahwrite)

These programs allow Seismic Unix (su) like processing in Madagascar.  
Some programs have su like names.

Some programs in this suite are sftahread, sftahgethw, ftahhdrmath, 
and sftahwrite.

The sftahmakeevent program makes simple synthetic on input data source
and group xy coordinates (i.e. sx, sy, gx, gy).  The event has constant
velocity and dip.  The nmo velocity will depend on source/receiver azimuth.
EXAMPLE:

sftahsort          \\
   input=npr3_gathers \\
   sort="iline:169,181  xline:104,116 offset:0,11000"  \\ 
   verbose=1       \\
| sftahmakeevent   \\
| sftahmakeskey pkey=iline,xline skey=cdpt verbose=1  \\      
| sftahnmo         \\
  verbose=1        \\
  tnmo=0.000,4.000 \\
  vnmo=11000,11000 \\
| sftahwrite       \\
  verbose=1        \\      
  label2="cdpt"  o2=1 n2=34  d2=1     \\
  label3="xline" o3=104 n3=13 d3=1    \\
  label4="iline" o4=169 n4=13  d4=1   \\
  output=gather_subset.rsf            \\
>/dev/null

The headers are in the file npr3_gathers_hdr.rsf, 
the headers parameter default.  The headers are merged with the trace 
amplitudes and the tah data sent down the pipe for sftahmakeevent.  The 
Traces are sent to STDOUT to have nmo applied and data to be written to 
disk.  Data is also sent to /dev/null (the bit bucket).

PARAMETERS
   none yest, but eventually ude this template:
   strings key= no default

        list of header keys print.  Look at the sfsegyread for a list
	of header names.

''')
rsf.doc.progs['sftahmakeevent']=sftahmakeevent

sftahheadermath = rsf.doc.rsfprog('sftahheadermath','user/karl/Mtahheadermath.c','''read Trace and Header (tah), compute header values''')
sftahheadermath.par('verbose',rsf.doc.rsfpar('int','1','','''\n
       flag to control amount of print
       0 terse, 1 informative, 2 chatty, 3 debug
    '''))
sftahheadermath.par('output',rsf.doc.rsfpar('string ',desc='''Describes the output in a mathematical notation. '''))
sftahheadermath.par('outputkey',rsf.doc.rsfpar('string ',desc='''name of the header key to put the results of the output equation '''))
sftahheadermath.version('1.7')
sftahheadermath.synopsis('''sftahheadermath < in.rsf > out.rsf verbose=1 output= outputkey=''','''
   Known functions for float data: 
   cos,  sin,  tan,  acos,  asin,  atan, 
   cosh, sinh, tanh, acosh, asinh, atanh,
   exp,  log,  sqrt, abs, erf, erfc, sign

   Known functions for int data: sign, abs

   modeled on sfheademath.  This program outputs the whole header.  It was
   a building block for sftahheadermath.

   tah is the abbreviation of Trace And Header.  Madagascar programs 
   that begin with sftah are a designed to:
   1- read trace and headers from separate rsf files and write them to 
   standard output (ie sftahread)
   2- filter programs that read and write standard input/output and 
   process the tah data (eg sftahnmo, sftahstack)
   3- read tah data from standard input and write separate rsf files for 
   the trace and headers data (ie sftahwrite)

   These programs allow Seismic Unix (su) like processing in Madagascar.  
   Some programs have su like names.

   Some programs in this suite are sftahread, sftahgethw, ftahhdrmath, 
   and sftahwrite.

   The sftahheadermath updates a trace header with a new value computed from
   input trace headers.  

   See also sftahmakeskey.

   EXAMPLE:

   sftahread \\
   verbose=1 \\
   input=npr3_gathers.rsf \\
   | sftahgethw \\
   verbose=0  \\
   key=sx,sy,gx,gy,offset  \\
   >/dev/null

   The headers are in the file npr3_gathers_hdr.rsf, 
   the headers parameter default.  The headers are merged with the trace 
   amplitudes and the tah data sent down the pipe for sftahgethw.  The 
   source and group coordinates and offset (sx,sy,gx,gy,offset) are 
   printed to STDERR.  Traces are sent to STDOUT, which is directed to
   /dev/null (the bit bucket).

   PARAMETERS
   string output= no default

   An equation to compute using the header keys.  Equations should
   problable be enclosed in quotes, ie ", to the equation can include
   multiplication, *, or blanks.  
   For example, to compute the midpoint x input:
   output="(sx+gx)/2.0)"

   string outputkey= no default
   the name of the output trace header key to put the evaluation of
   output.  For example to put the average of sx and gx into cdpx input:
   outputkey=cdpx

''')
rsf.doc.progs['sftahheadermath']=sftahheadermath

sftahmute = rsf.doc.rsfprog('sftahmute','user/karl/Mtahmute.c','''Read Trace And Header (tah) from standard input, MUTE ''')
sftahmute.par('xmute',rsf.doc.rsfpar('floats','','',''' [numxmute]'''))
sftahmute.par('tmute',rsf.doc.rsfpar('floats','','',''' [numtmute]'''))
sftahmute.par('verbose',rsf.doc.rsfpar('int','1','','''\n
       flag to control amount of print
       0 terse, 1 informative, 2 chatty, 3 debug
    '''))
sftahmute.par('ntaper',rsf.doc.rsfpar('int','12','','''\n
       length of the taper on the stack mute
    '''))
sftahmute.version('1.7')
sftahmute.synopsis('''sftahmute < in.rsf > out.rsf xmute= tmute= verbose=1 ntaper=12''','''''')
rsf.doc.progs['sftahmute']=sftahmute

sftahremoveclick = rsf.doc.rsfprog('sftahremoveclick','user/karl/Mtahremoveclick.c','''Trace And Header REMOVE electricl CLICK.''')
sftahremoveclick.par('key',rsf.doc.rsfpar('strings','','',''' [numkeys]'''))
sftahremoveclick.par('verbose',rsf.doc.rsfpar('int','1','','''\n
     flag to control amount of print
     0 terse, 1 informative, 2 chatty, 3 debug
  '''))
sftahremoveclick.version('1.7')
sftahremoveclick.synopsis('''sftahremoveclick < in.rsf > out.rsf key= verbose=1''','''
tah is the abbreviation of Trace And Header.  Madagascar programs 
that begin with sftah are a designed to:
1- read trace and headers from separate rsf files and write them to 
   standard output (ie sftahread)
2- filter programs that read and write standard input/output and 
   process the tah data (eg sftahnmo, sftahstack)
3- read tah data from standard input and write separate rsf files for 
   the trace and headers data (ie sftahwrite)

These programs allow Seismic Unix (su) like processing in Madagascar.  
Some programs have su like names.

Some programs in this suite are sftahread, sftahgethw, ftahhdrmath, 
and sftahwrite.

The sftahremoveclick program removes electrical noise clicks.  This noise has
the same shape and same time on each trace, but the amplitude varies on each trace.  The noise is create by electrical interference. 
EXAMPLE:

sftahread \\
   verbose=1 \\
   input=npr3_gathers.rsf \\
| sftahclickremove verbose=1 \\
| sftahwrite \\
  output=clickremove.rsf \\
  o2=1 n2=2969636 label2=tracl   \\
>/dev/null

The headers are in the file npr3_gathers_hdr.rsf, the headers parameter 
default.  The headers are merged with the trace amplitudes and the tah data 
sent down the pipe for sftahgethw.  Electrical clicks are moved from the data.
Traces are sent to STDOUT, which is directed to
/dev/null (the bit bucket).

PARAMETERS
   strings key= no default

        list of header keys print.  Look at the sfsegyread for a list
	of header names.

''')
rsf.doc.progs['sftahremoveclick']=sftahremoveclick

sftahgain = rsf.doc.rsfprog('sftahgain','user/karl/Mtahgain.c','''Read Trace And Header (tah) from standard input and apply GAIN''')
sftahgain.par('xxstart',rsf.doc.rsfpar('floats','','',''' [numxstart]'''))
sftahgain.par('tstart',rsf.doc.rsfpar('floats','','',''' [numtstart]'''))
sftahgain.par('verbose',rsf.doc.rsfpar('int','1','','''\n
       flag to control amount of print
       0 terse, 1 informative, 2 chatty, 3 debug
    '''))
sftahgain.par('scale',rsf.doc.rsfpar('float','1.0','','''multiply data by this float '''))
sftahgain.par('tpow',rsf.doc.rsfpar('float','0.0','','''multiply data by t^tpow '''))
sftahgain.par('epow',rsf.doc.rsfpar('float','0.0','','''multiply data by exp(epow*t) '''))
sftahgain.par('agc',rsf.doc.rsfpar('float','0.0','','''Length of agc window in seconds.  0.0 means no agc '''))
sftahgain.version('1.7')
sftahgain.synopsis('''sftahgain < in.rsf > out.rsf xxstart= tstart= verbose=1 scale=1.0 tpow=0.0 epow=0.0 agc=0.0''','''
   tah is the abbreviation of Trace And Header.  Madagascar programs 
   that begin with sftah are a designed to:
   1- read trace and headers from separate rsf files and write them to 
   standard output (ie sftahread)
   2- filter programs that read and write standard input/output and 
   process the tah data (eg sftahnmo, sftahstack)
   3- read tah data from standard input and write separate rsf files for 
   the trace and headers data (ie sftahwrite)

   These programs allow Seismic Unix (su) like processing in Madagascar.  
   Some programs have su like names.

   Some programs in this suite are sftahread, sftahgethw, ftahhdrmath, 
   and sftahwrite.

   The sftahgain program is designed to apply various amplitude gain 
   functions.  These gain functions include multiply by a constant, 
   trace balance, clipping, AGC, t**pow, exp(epow*t) and AGC.  Trace 
   and header data (tah) are read from standard input (usually a pipe).
   Data is scaled:
   out(t) = scale * BAL{CLIP[AGC{[t^tpow * exp(epow * t)}]}
   Then trace and header data is written to standard output.

   EXAMPLE:

   sftahsort input=shots-receivers-23900_headfix.rsf          \\
   sort="xline:600,601 offset"                             \\
   | sftahgain agc=.5                                         \\
   | sftahmakeskey pkey=xline skey=cdpt                       \\
   | sftahwrite                                               \\
   verbose=1                                                \\
   label2=cdpt  o2=1 n2=100 d2=1                            \\
   label3=xline o3=600 n3=1 d3=1                            \\
   output=agccmps.rsf                                       \\
   >/dev/null

   sfgrey <agccmps.rsf | sfpen

   In this example the shot organized prestack data in the file 
   shots-receivers-23900_headfix.rsf are read in xline offset order by 
   sftahsort program.  The headers are in the file 
   shots-receivers-23900_headfix_hdr.rsf, the headers parameter default.
   The headers are merged with the trace amplitudes and the tah data sent 
   down the pipe for scaling (agc).

   sftahagc applies a .5 second automatic gain control (agc)

   The program sftahmakeskey is used to create a secondary key used 
   in the following sftahwrite to define the location to wrte the trace 
   in the output file. Sftahmakeskey makes a secondary key (skey=cdpt) 
   the count the traces starting in the a primary key gather (pkey=xline).
   The input traces gathered by xline by sftahsort. Sftahmakeskey sets 
   cdpt to 1 when the trace has a new xline.  If the trace has the same 
   xline as the previous trace cdpt is incremented

   Sftahwrite writes the the trace data to agccmp.rsf and the headers are 
   written to the file agccmp_hdr.rsf.  The order of the data in the output 
   file is defined by the cdpt and xline trace headers, so the  data order
   is (time,cmpt,xline).  Finally, the output volume is displayed using
   sfgrey.

   PARAMETERS
   int verbose=1
   flag to control amount of print
   0 terse, 1 informative, 2 chatty, 3 debug

   float scale=1.0
   multiply data by this float

   float tpow=0.0
   multiply data by t^tpow

   float epow=0.0
   multiply data by exp(epow*t)

   float agc=0.0
   Length of agc window in seconds.  0.0 means no agc

   Operation order:

   out(t) = scale * BAL{CLIP[AGC{[t^tpow * exp(epow * t)}]}	
''')
rsf.doc.progs['sftahgain']=sftahgain

sftahfilter = rsf.doc.rsfprog('sftahfilter','user/karl/Mtahfilter.c','''Read Trace And Header (tah) from standard input and FILTER ''')
sftahfilter.par('filter_file',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftahfilter.par('filter',rsf.doc.rsfpar('floats','','',''' [numfilter]'''))
sftahfilter.par('verbose',rsf.doc.rsfpar('int','1','','''\n
     flag to control amount of print
     0 terse, 1 informative, 2 chatty, 3 debug
  '''))
sftahfilter.par('filt_indx_t0',rsf.doc.rsfpar('int','0','','''\n
     indx to time 0 in the filter.  Must be in the range [0,numfilter)
    '''))
sftahfilter.par('filter_file',rsf.doc.rsfpar('string ',desc='''\n
     name of the rsf file containing the filter(s)
  (auxiliary input file name)'''))
sftahfilter.version('1.7')
sftahfilter.synopsis('''sftahfilter < in.rsf > out.rsf filter_file=filter_file.rsf filter= verbose=1 filt_indx_t0=0''','''
tah is the abbreviation of Trace And Header.  Madagascar programs 
that begin with sftah are a designed to:
1- read trace and headers from separate rsf files and write them to 
   standard output (ie sftahread)
2- filter programs that read and write standard input/output and 
   process the tah data (eg sftahnmo, sftahstack)
3- read tah data from standard input and write separate rsf files for 
   the trace and headers data (ie sftahwrite)

These programs allow Seismic Unix (su) like processing in Madagascar.  
Some programs have su like names.

Some programs in this suite are sftahread, sftahgethw, ftahhdrmath, 
and sftahwrite.

The sftahfilter program is designed to apply a filter. Trace and 
header data (tah) are read from from standard input (usually a pipe).
A filter is read from the command line or from a file.  If the filter
is read from a file, it can be a single filter, or one filter for each
trace.  Future enhancements would be to use trace headers to define
a location in the filter file and read that filter or even interpolate
a filter.  That would support shot or receiver dependent filter for
surface consistant decon.  Another enhancement would be to add 
frequency domain bandpass filters.  

EXAMPLE:

sftahsort input=shots-receivers-23900_headfix.rsf           \\
   sort="xline:600,601 offset"                              \\
| sftahfilter filt=dephase.rsf                              \\
| sftahmakeskey pkey=xline skey=cdpt                        \\
| sftahwrite                                                \\
  verbose=1                                                 \\
  label2=cdpt  o2=1 n2=100 d2=1                             \\
  label3=xline o3=600 n3=1 d3=1                             \\
  output=dephasecmps.rsf                                    \\
>/dev/null

sfgrey <mutecmps.rsf | sfpen

In this example a deterministic dephase filter is applied to a prestack
datafile.

The shot organized prestack cmp data, shots-receivers-23900_headfix.rsf 
are read in xline offset order by sftahsort program.  The headers are 
in the file shots-receivers-23900_headfix_hdr.rsf, the headers 
parameter default.  The headers are merged with the trace amplitudes 
and the tah data sent down the pipe to apply a filter.

The sftahfilter program applies a filter contained in the dephase.rsf
file.
The program sftahmakeskey is used to create a secondary key used 
in the following sftahwrite to define the location to wrte the trace 
in the output file. Sftahmakeskey makes a secondary key (skey=cdpt) 
the count the traces starting in the a primary key gather (pkey=xline).
The input traces gathered by xline by sftahsort. Sftahmakeskey sets 
cdpt to 1 when the trace has a new xline.  If the trace has the same 
xline as the previous trace cdpt is incremented

Sftahwrite writes the the trace data to dephasecmp.rsf and the headers
are written to the file mutecmp_hdr.rsf.  The order of the data in the 
file is defined by the cdpt and xline trace headers, so the  data order
is (time,cmpt,xline).  Finally, the output volume is displayed using
sfgrey.

PARAMETERS

   floats filter=NULL

        A list of floats that is the filter to convolve on the input 
	traces.

   string filter_file=NULL

       Name of an rsf file that contains the filter(s)

   int filter_index_t0

        Index of time=0 on the filter

   int  verbose=1       
        
        flag to control amount of print
        0 terse, 1 informative, 2 chatty, 3 debug
	
''')
rsf.doc.progs['sftahfilter']=sftahfilter

