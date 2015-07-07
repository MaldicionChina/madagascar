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

