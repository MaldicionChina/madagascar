/* This file is automatically generated. DO NOT EDIT! */

#ifndef _oc_h
#define _oc_h


#ifndef _LARGEFILE_SOURCE
#define _LARGEFILE_SOURCE
#endif
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>


#include <rsf.h>


void oc_invert(off_t n, FILE *wall);
/*< write out 1/wall >*/


void oc_zero (off_t n, FILE *wall);
/*< set wall=0 >*/


void oc_dump (off_t n, FILE *wall, sf_file out);
/*< write wall to out >*/


void oc_divide (off_t n, FILE *data, FILE *wall, sf_file out);
/*< write data/wall to out >*/

#endif
