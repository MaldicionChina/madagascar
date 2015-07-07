[sfbilat2]
Cat:    RSF/user/fomels
Desc:   2-D bilateral filtering
DocCmd: sfbilat2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  a1 float  -   -  		vertical attenuation factor 
LDesc:  (defaults to: 0.0f)
Param:  a2 float  -   -  		horizontal attenuation factor 
LDesc:  (defaults to: a1)
Param:  a3 float  -   -  		data attenuation factor 
LDesc:  (defaults to: 0.0f)
Param:  r1 int  -  1 		vertical smoothing radius 
Param:  r2 int  -  1 		horizontal smoothing radius 
Param:  repeat int  -  1 		repeat the operation 

