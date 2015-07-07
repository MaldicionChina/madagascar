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

