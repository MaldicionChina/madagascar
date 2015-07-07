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

