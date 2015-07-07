/* This file is automatically generated. DO NOT EDIT! */

#ifndef _tahsub_h
#define _tahsub_h


/* global variables. need a temp array for sf_get_tah to pass non tah
   records read from pipe.  This means sf_get_tah is not thread safe,
   but the intended use is to read stdin, so why whould you want to 
   run multiple sf_get_tah on more then one thread? 
char* sf_get_tah_bytebuffer=NULL;
int sf_get_tah_bytebuffer_len=0;
*/
int counttokens(const char* delimittedtokens, const char* delimiters);
/*< return number of delimiter seperated tokens in string>*/


char** delimittedtokens2list(const char* delimittedtokens, 
			     const char* delimiters, 
			     int* numtoken);
/*<return number of delimitter seperated tokens in string and list of tokens>*/


int getnumpars(const char* key);
/*< get number of pars >*/


char** sf_getnstring(char* key, int* numkeys);
/*< get strings >*/


void put_tah(float* trace, float* header, 
	     int n1_traces, int n1_headers, sf_file file);
/*< put tah >*/


bool get_tah(float* trace, float* header, 
	     int n1_traces, int n1_headers, sf_file file);
/*< get tah.  return 1 if eof encountered, 0 otherwise >*/


void tahwritemapped(int verbose, float* trace, void* iheader, 
		    int n1_traces, int n1_headers,
		    sf_file output,sf_file outheaders,
		    sf_datatype typehead,
		    sf_axis* output_axa_array,
		    int* indx_of_keys, int dim_output,
		    off_t* n_output, off_t* n_outheaders);
/*< tah write mapped >*/

#endif
