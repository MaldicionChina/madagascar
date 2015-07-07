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

