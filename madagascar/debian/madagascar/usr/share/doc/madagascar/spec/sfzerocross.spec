[sfzerocross]
Cat:    RSF/user/saragiotis
Desc:   Zero crossings
DocCmd: sfzerocross | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  levels int  -  3 		levels of quantization [2,3,5].
LDesc:        levels=2	1: zero crossing or zero; 0: otherwise
LDesc:        levels=3	1: positive to negative zc; -1 negative to positive zc; 0: otherwise
LDesc:        levels=5	+/-2: positive/negative values; +/-1: as in levels=3; 0: zero. 
LDesc:      

