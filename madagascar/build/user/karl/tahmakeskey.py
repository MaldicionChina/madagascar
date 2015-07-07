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

