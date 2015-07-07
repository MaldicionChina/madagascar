/* This file is automatically generated. DO NOT EDIT! */

#ifndef _plvpl_h
#define _plvpl_h


#include <plplot.h>
#include <plplotP.h>
#include <plstrm.h>


void plD_dispatch_init_plvpl (PLDispatchTable *pdt);
/*< initialize >*/


void plD_init_plvpl (PLStream *pls);
/*< Initialize the device. >*/


void plD_line_plvpl (PLStream *pls, short x1a, short y1a, short x2a, short y2a);
/*< Draw a line in the current color from (x1,y1) to (x2,y2). >*/


void plD_polyline_plvpl (PLStream *pls, short *xa, short *ya, PLINT npts);
/*< Draw a polyline in the current color. >*/


void plD_eop_plvpl (PLStream *pls);
/*< End of page. >*/


void plD_bop_plvpl (PLStream *pls);
/*< Set up for the next page. >*/


void plD_tidy_plvpl (PLStream *pls);
/*< Close output or otherwise clean up. >*/


void plD_state_plvpl (PLStream *pls, PLINT op);
/*< Handle change in PLStream state (color, pen width, fill attribute, etc). >*/


void plD_esc_plvpl (PLStream *pls, PLINT op, void *ptr);
/*< Escape function. >*/

#endif
