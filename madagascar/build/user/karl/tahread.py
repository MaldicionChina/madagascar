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

