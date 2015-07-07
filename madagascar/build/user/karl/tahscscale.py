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

