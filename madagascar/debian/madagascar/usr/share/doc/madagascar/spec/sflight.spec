[sflight]
Cat:    RSF/user/gee
Desc:   Apply 2-D directional high-pass to highlight data
DocCmd: sflight | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  ax float  -  1. 		x direction 
Param:  ay float  -  1. 		y direction 
Param:  eps float  -  0. 		highpass filter parameter; if eps=0, apply derivative 

