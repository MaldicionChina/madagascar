[sfdijkstra]
Cat:    RSF/user/pwd
Desc:   Dijkstra shortest-path algorithm in 2-D
DocCmd: sfdijkstra | cat
Port:   stdin  rsf r req 	RSF standard input (containing cost data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  fin1 int-list  -   -  		 [nf]
Param:  fin2 int-list  -   -  		final points  [nf]
Param:  nf int  -  0 		number of final points 
Param:  paths string-list  -   -  		 [nf]
Param:  ref1 int  -  0 		
Param:  ref2 int  -  0 		source point 

