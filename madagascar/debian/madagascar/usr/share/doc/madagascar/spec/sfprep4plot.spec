[sfprep4plot]
Cat:    RSF/user/ivlad
Desc:   Resamples a 2-D dataset to the desired picture resolution, with antialias
DocCmd: sfprep4plot | cat
Param:  h string  -   -  		
Param:  inp string  -   -  		input file
Param:  out string  -   -  		output file
Param:  ppi int  -   -  		outp. resolution (px/in). Necessary when unit!=px
Param:  prar enum-bool  -  y 		if y, PReserve Aspect Ratio of input
Param:  unit string  -   -  		unit of h and w. Can be: px, mm, cm, in
LDesc:  (defaults to: px)
Param:  verb enum-bool  -  n 		if y, print system commands, outputs
Param:  w string  -   -  		

