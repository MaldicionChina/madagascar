[sftentwt]
Cat:    RSF/user/gee
Desc:   Tent-like weight for patching
DocCmd: sftentwt | cat
Port:   stdout rsf w req 	RSF standard output (containing wallwt data)
Port:   windwt rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  a int-list  -   -  		filter size  [dim]
Param:  center int-list  -   -  		 [dim]
Param:  dim int  -  2 		number of dimensions 
Param:  k int-list  -   -  		number of windows  [dim]
Param:  tent enum-bool  -  y 		if y, use tent-like weight; n, cosine weight 
Param:  w int-list  -   -  		window size  [dim]

