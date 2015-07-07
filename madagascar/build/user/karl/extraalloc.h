/* This file is automatically generated. DO NOT EDIT! */

#ifndef _extraalloc_h
#define _extraalloc_h


#ifndef _LARGEFILE_SOURCE
#define _LARGEFILE_SOURCE
#endif
#include <sys/types.h>
#include <unistd.h>


#include <stdlib.h>


#include <rsf.h>
#include "extraalloc.h"


float **sf_floatrealloc2 (float ** ptr,
			  size_t n1 /* fast dimension */, 
			  size_t n2 /* slow dimension */);
/*< reallocate float** array.  only n2, slowest dimension, can change 
    ptr[0][0] points to a contiguous array >*/


char  **sf_alloc2(size_t n1bytes, /* sizeof a vector.  for a 2D float array this
				    will be n1*sizeof(float).  for an array of
				    seqy traces with will be 240 byte header +
				    nt*sizeof(float) */
                  size_t n2 /* slow dimension */);
/*< allocate a two d array.  to allocate a 2d array of floats:
    my2Dfloatarray=(float**) sf_alloc2(n1*sizeof(float),n2);
    to allocate an array of segy traces:
    myarraysegytraces=(segytrace*)sfalloc(sizeof(segytrace)+
                                             (n1-1)*sizeof(float),
					     n2); >*/


char  **sf_realloc2(void** ptrin,
		    size_t n1bytes, /* sizeof a vector.  for a 2D float array 
				       this will be n1*sizeof(float).  for an 
				       array of segy traces with will be 240 
				       byte header + nt*sizeof(float) */
                    size_t n2 /* slow dimension */);
/*< reallocate char** array.  only n2, slowest dimension, can change 
    ptr[0][0] points to a contiguous array >*/

#endif
