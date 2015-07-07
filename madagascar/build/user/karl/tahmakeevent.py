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

