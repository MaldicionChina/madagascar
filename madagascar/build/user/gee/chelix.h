/* This file is automatically generated. DO NOT EDIT! */

#ifndef _chelix_h
#define _chelix_h


typedef struct chelixfilter {
    int     nh;
    sf_complex* flt;
    int*   lag;
    bool*  mis;
} *cfilter;


/*------------------------------------------------------------*/
cfilter allocatechelix( int nh);
/*< allocation >*/


/*------------------------------------------------------------*/
void deallocatechelix( cfilter aa);
/*< deallocation >*/


/*------------------------------------------------------------*/
void displaychelix( cfilter aa);
/*< display filter >*/


void helimakelag(cfilter aa,int nx, int ny);
/*< make lags for a filter >*/

#endif
