[sfspike]
Cat:    RSF/system/main
Desc:   Generate simple data: spikes, boxes, planes, constants
DocCmd: sfspike | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing spike data)
Param:  d# float  -   -  		sampling on #-th axis 
LDesc:  (defaults to: [0.004,0.1,0.1,...])
Param:  k# int-list  -   -  		spike starting position  [nsp]
LDesc:  (defaults to: [0,...])
Param:  l# int-list  -   -  		spike ending position  [nsp]
LDesc:  (defaults to: [k1,k2,...])
Param:  label# string  -   -  		label on #-th axis 
LDesc:  (defaults to: [Time,Distance,Distance,...])
Param:  mag float-list  -   -  		spike magnitudes  [nsp]
Param:  n# int  -   -  		size of #-th axis 
Param:  nsp int  -  1 		Number of spikes 
Param:  o# float  -   -  		origin on #-th axis 
LDesc:  (defaults to: [0,0,...])
Param:  p# float-list  -   -  		spike inclination (in samples)  [nsp]
LDesc:  (defaults to: [0,...])
Param:  title string  -   -  		title for plots 
Param:  unit# string  -   -  		unit on #-th axis 
LDesc:  (defaults to: [s,km,km,...])

