/* This file is automatically generated. DO NOT EDIT! */

#ifndef _vp_plot_h
#define _vp_plot_h


void vp_set_dash (float type
/*
 *	0 continuous   DEFAULT
 *	1 fine dash
 *	2 fine dot
 *	3 dash
 *	4 large dash
 *	5 dot dash
 *	6 large dash small dash
 *	7 double dot
 *	8 double dash
 *	9 loose dash  The part after the decimal point determines 
 *                     the pattern repetition interval
 */);
/*< set dash type >*/


void vp_plot_init(int n2 /* number of lines */);
/*< initialize vector plot >*/


void vp_plot_set (int i2 /* line number */);
/*< select a line >*/


void vp_plot_close (void);
/*< free allocated storage >*/

#endif
