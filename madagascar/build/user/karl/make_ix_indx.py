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

