/* This file is automatically generated. DO NOT EDIT! */

#ifndef _abcpass2_h
#define _abcpass2_h


void bd_init(int n1,  int n2    /*model size:x*/,
             int nb1, int nb2  /*top, bottom*/,
             int nb3, int nb4  /*left, right*/,
             float c1, float c2 /*top, bottom*/,
             float c3, float c4 /*left, right*/);
/*< initialization >*/


void bd_close(void);
/*< free memory allocation>*/


void bd_decay(float **a /*2-D matrix*/);
/*< boundary decay>*/


void bdz_init(int n1, int n2, int n3 /*model size:x*/,
             int nb1, int nb2  /*top, bottom*/,
             int nb3, int nb4  /*left, right*/,
             float c1, float c2 /*top, bottom*/,
             float c3, float c4 /*left, right*/);
/*< initialization >*/


void bdz_decay(float ***a /*3-D matrix*/);
/*< boundary decay>*/


void abc_cal(int abc /* decaying type*/,
             int nb  /* absorbing layer length*/, 
             float c /* decaying parameter*/,
             float* w /* output weight[nb] */);
/*< find absorbing coefficients >*/

#endif
