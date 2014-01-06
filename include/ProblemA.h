#include <string>
#include <iostream>
#include <vector>
#include <iostream>
#include <sstream>  
#include <stdio.h>
#include <algorithm>
#include "DivisorsHash.h"

#ifndef ProblemA_H
#define ProblemA_H

bool wayToSort(DivisorsHash i, DivisorsHash j) { return i.getKey() < j.getKey(); }

class ProblemA {
public:

/// ctor by default is empty
/// ctor by default is empty
	ProblemA () {}


	~ProblemA() {}     


	void setKeys (std::vector<int>  _keys) { keys=_keys; return;}

	std::vector<DivisorsHash> generate ( ) const {
		std::vector<DivisorsHash> divisors;
		for (int i=0; i<keys.size();i++) {
		 divisors.push_back(DivisorsHash());
		 divisors.back().setKey(keys[i]);
		 divisors.back().findDivisors();
		}
	
	return divisors;
	}


		
	






/// to print out the ProblemA
friend std::ostream & operator <<(std::ostream & out, const ProblemA & right){

		

		std::vector<DivisorsHash> Divisors = right.generate();
		std::sort(Divisors.begin(),Divisors.end(),wayToSort);
		out<<"{\n";
		for (int i=0; i< Divisors.size(); i++) {out<<"\t"; out<< Divisors[i]; out<<",\n";}
		out<<"}\n";
	}


private:

	std::vector<int> keys;
        std::vector<DivisorsHash> divisors;

}; 

#endif




