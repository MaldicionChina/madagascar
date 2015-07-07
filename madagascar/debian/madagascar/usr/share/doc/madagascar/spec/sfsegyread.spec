[sfsegyread]
Cat:    RSF/system/seismic
Desc:   Convert a SEG-Y or SU dataset to RSF
DocCmd: sfsegyread | cat
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  bfile string  -   -  		output binary data header file 
Param:  endian enum-bool  -  y 		Whether to automatically estimate endianness or not 
Param:  format int  -   -  		Data format. The default is taken from binary header.
LDesc:  	   1 is IBM floating point
LDesc:  	   2 is 4-byte integer
LDesc:  	   3 is 2-byte integer
LDesc:  	   5 is IEEE floating point
LDesc:         6 is native_float (same as RSF binary default)
LDesc:  	
LDesc:  (defaults to: segyformat (bhead))
Param:  hfile string  -   -  		output text data header file 
Param:  mask string  -   -  		optional header mask for reading only selected traces (auxiliary input file name)
Param:  n2 int  -  0 		number of traces to read (if 0, read all traces) 
Param:  ns int  -   -  		
LDesc:  (defaults to: itrace[ segykey("ns")])
Param:  read string  -   -  		what to read: h - header, d - data, b - both (default) 
Param:  su enum-bool  -   -  		y if input is SU, n if input is SEGY 
Param:  suxdr enum-bool  -  n 		y, SU has XDR support 
Param:  tape string  -   -  		input data 
Param:  tfile string  -   -  		output trace header file (auxiliary output file name)
Param:  verb enum-bool  -  n 		Verbosity flag 

