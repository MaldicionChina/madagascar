[sfwavmod]
Cat:    RSF/user/chen
Desc:   1-2-3D finite difference modeling
DocCmd: sfwavmod | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing dat data)
Port:   ggrid rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sgrid rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  jt int  -  1 		time interval in observation system 
Param:  jtm int  -  100 		time interval of wave movie 
Param:  ot float  -  0.0 		time delay 
Param:  verb enum-bool  -  n 		verbosity 
Param:  wfl string  -   -  		wavefield movie file (auxiliary output file name)

