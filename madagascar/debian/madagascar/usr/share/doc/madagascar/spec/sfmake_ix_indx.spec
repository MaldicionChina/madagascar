[sfmake_ix_indx]
Cat:    RSF/user/karl
Desc:   MAKE Iline Xline INDX files for quick 3D data subsets (superbins)
DocCmd: sfmake_ix_indx | cat
Port:   stdin  rsf r req 	RSF standard input (containing infile data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  headers string  -   -  		
LDesc:  
LDesc:       Trace header file name.  Default is the input data file
LDesc:       name, with the final .rsf changed to _hdr.rsf 
LDesc:    
Param:  iline string  -   -  		
LDesc:  
LDesc:       header key for the main index key.  This should be iline, but you 
LDesc:       may have non-standard trace headers or a wierd use of this program 
LDesc:    
Param:  ilineinc int  -  10 		
LDesc:  
LDesc:       incrment in iline for the index
LDesc:    
Param:  ilinemax float  -  -1e31 		
LDesc:  
LDesc:       maximum 'iline' header key to include in the index.  Use this parameter
LDesc:       to remove null trace headers or traces outside project area.
LDesc:    
Param:  ilinemin float  -  -1e31 		
LDesc:  
LDesc:       minimum 'iline' header key to include in the index.  Use this parameter
LDesc:       to remove null trace headers or traces outside project area.
LDesc:    
Param:  indxdir string  -   -  		
LDesc:  
LDesc:       The name of the directory containing the iline,xline index.  This 
LDesc:       directory will be in DATAPATH (probably the environment variable). The 
LDesc:       directory also continues a file 'filenames', a list of the trace and 
LDesc:       header files that contributes to this index. The directory contains files 
LDesc:       with names 'indx#' here # is an integer multiple of ilineinc. These files 
LDesc:       contains a record for each contributing trace with filenumber, 
LDesc:       tracenumber, and the trace header. The file containing the trace is 
LDesc:       determined using the  can be read by using the filenumber and the 
LDesc:       'filenames' file.  The tracenumber defines the location of the trace 
LDesc:       in the file.
LDesc:    
Param:  input string  -   -  		
LDesc:  
LDesc:       Input file for traces amplitudes
LDesc:    
Param:  verbose int  -  1 		
LDesc:  
LDesc:       flag to control amount of print
LDesc:       0 terse, 1 informative, 2 chatty, 3 debug
LDesc:    
Param:  xline string  -   -  		
Param:  xlinemax float  -  -1e31 		
LDesc:  
LDesc:       maximum 'xline' header key to include in the index.  Use this parameter
LDesc:       to remove null trace headers or traces outside project area.
LDesc:    
Param:  xlinemin float  -  -1e31 		
LDesc:  
LDesc:       minimum 'xline' header key to include in the index.  Use this parameter
LDesc:       to remove null trace headers or traces outside project area.
LDesc:    

