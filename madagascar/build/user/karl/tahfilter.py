sftahfilter = rsf.doc.rsfprog('sftahfilter','user/karl/Mtahfilter.c','''Read Trace And Header (tah) from standard input and FILTER ''')
sftahfilter.par('filter_file',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftahfilter.par('filter',rsf.doc.rsfpar('floats','','',''' [numfilter]'''))
sftahfilter.par('verbose',rsf.doc.rsfpar('int','1','','''\n
     flag to control amount of print
     0 terse, 1 informative, 2 chatty, 3 debug
  '''))
sftahfilter.par('filt_indx_t0',rsf.doc.rsfpar('int','0','','''\n
     indx to time 0 in the filter.  Must be in the range [0,numfilter)
    '''))
sftahfilter.par('filter_file',rsf.doc.rsfpar('string ',desc='''\n
     name of the rsf file containing the filter(s)
  (auxiliary input file name)'''))
sftahfilter.version('1.7')
sftahfilter.synopsis('''sftahfilter < in.rsf > out.rsf filter_file=filter_file.rsf filter= verbose=1 filt_indx_t0=0''','''
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

The sftahfilter program is designed to apply a filter. Trace and 
header data (tah) are read from from standard input (usually a pipe).
A filter is read from the command line or from a file.  If the filter
is read from a file, it can be a single filter, or one filter for each
trace.  Future enhancements would be to use trace headers to define
a location in the filter file and read that filter or even interpolate
a filter.  That would support shot or receiver dependent filter for
surface consistant decon.  Another enhancement would be to add 
frequency domain bandpass filters.  

EXAMPLE:

sftahsort input=shots-receivers-23900_headfix.rsf           \\
   sort="xline:600,601 offset"                              \\
| sftahfilter filt=dephase.rsf                              \\
| sftahmakeskey pkey=xline skey=cdpt                        \\
| sftahwrite                                                \\
  verbose=1                                                 \\
  label2=cdpt  o2=1 n2=100 d2=1                             \\
  label3=xline o3=600 n3=1 d3=1                             \\
  output=dephasecmps.rsf                                    \\
>/dev/null

sfgrey <mutecmps.rsf | sfpen

In this example a deterministic dephase filter is applied to a prestack
datafile.

The shot organized prestack cmp data, shots-receivers-23900_headfix.rsf 
are read in xline offset order by sftahsort program.  The headers are 
in the file shots-receivers-23900_headfix_hdr.rsf, the headers 
parameter default.  The headers are merged with the trace amplitudes 
and the tah data sent down the pipe to apply a filter.

The sftahfilter program applies a filter contained in the dephase.rsf
file.
The program sftahmakeskey is used to create a secondary key used 
in the following sftahwrite to define the location to wrte the trace 
in the output file. Sftahmakeskey makes a secondary key (skey=cdpt) 
the count the traces starting in the a primary key gather (pkey=xline).
The input traces gathered by xline by sftahsort. Sftahmakeskey sets 
cdpt to 1 when the trace has a new xline.  If the trace has the same 
xline as the previous trace cdpt is incremented

Sftahwrite writes the the trace data to dephasecmp.rsf and the headers
are written to the file mutecmp_hdr.rsf.  The order of the data in the 
file is defined by the cdpt and xline trace headers, so the  data order
is (time,cmpt,xline).  Finally, the output volume is displayed using
sfgrey.

PARAMETERS

   floats filter=NULL

        A list of floats that is the filter to convolve on the input 
	traces.

   string filter_file=NULL

       Name of an rsf file that contains the filter(s)

   int filter_index_t0

        Index of time=0 on the filter

   int  verbose=1       
        
        flag to control amount of print
        0 terse, 1 informative, 2 chatty, 3 debug
	
''')
rsf.doc.progs['sftahfilter']=sftahfilter

