sftahheadermath = rsf.doc.rsfprog('sftahheadermath','user/karl/Mtahheadermath.c','''read Trace and Header (tah), compute header values''')
sftahheadermath.par('verbose',rsf.doc.rsfpar('int','1','','''\n
       flag to control amount of print
       0 terse, 1 informative, 2 chatty, 3 debug
    '''))
sftahheadermath.par('output',rsf.doc.rsfpar('string ',desc='''Describes the output in a mathematical notation. '''))
sftahheadermath.par('outputkey',rsf.doc.rsfpar('string ',desc='''name of the header key to put the results of the output equation '''))
sftahheadermath.version('1.7')
sftahheadermath.synopsis('''sftahheadermath < in.rsf > out.rsf verbose=1 output= outputkey=''','''
   Known functions for float data: 
   cos,  sin,  tan,  acos,  asin,  atan, 
   cosh, sinh, tanh, acosh, asinh, atanh,
   exp,  log,  sqrt, abs, erf, erfc, sign

   Known functions for int data: sign, abs

   modeled on sfheademath.  This program outputs the whole header.  It was
   a building block for sftahheadermath.

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

   The sftahheadermath updates a trace header with a new value computed from
   input trace headers.  

   See also sftahmakeskey.

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
   string output= no default

   An equation to compute using the header keys.  Equations should
   problable be enclosed in quotes, ie ", to the equation can include
   multiplication, *, or blanks.  
   For example, to compute the midpoint x input:
   output="(sx+gx)/2.0)"

   string outputkey= no default
   the name of the output trace header key to put the evaluation of
   output.  For example to put the average of sx and gx into cdpx input:
   outputkey=cdpx

''')
rsf.doc.progs['sftahheadermath']=sftahheadermath

