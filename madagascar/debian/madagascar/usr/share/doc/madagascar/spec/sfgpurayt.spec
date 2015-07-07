[sfgpurayt]
Cat:    RSF/user/jmonsegny
Desc:   Parallel shortest path ray tracing
DocCmd: sfgpurayt | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  bs   -   -  		Cuda block is a square with bs*bs threads. Must divide dimensions of in.rsf, bs >= 1 (int)
LDesc:  (defaults to: 16)
Param:  ctime   -   -  		Output rsf file for computation time. Empty for no computation time output.
Param:  dx   -   -  		Horizontal and vertical separation between nodes, dx > 0.0 (float)
LDesc:  (defaults to: 1.0f)
Param:  ord   -   -  		Forward star has (ord*ord-1) nodes, ord >= 1 (int)
LDesc:  (defaults to: 3)
Param:  ray   -   -  		Output file for a sfgraph compatible ray file. Empty for no ray output.
Param:  sx   -   -  		Horizontal node source coordinate (int)
LDesc:  (defaults to: 0)
Param:  sz   -   -  		Vertical node source coordinate (int)
LDesc:  (defaults to: 0)

