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

