/* This file is automatically generated. DO NOT EDIT! */

#ifndef _helicon_h
#define _helicon_h


void helicon_init( sf_filter bb);
/*<  Initialized with the filter. >*/


void helicon_lop( bool adj, bool add, 
		  int nx, int ny, float* xx, float*yy);
/*< linear operator >*/

#endif
