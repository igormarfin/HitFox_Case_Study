#include <string>
#include <iostream>
#include <vector>
#include <iostream>
#include <sstream>  
#include <stdio.h>
#include <math.h>
#include <algorithm>


#ifndef DivisorsHash_H
#define DivisorsHash_H


bool wayToSortInt(int i, int j) { return i < j; }


class DivisorsHash {
public:

/// ctor by default is empty
/// ctor by default is empty
	DivisorsHash (): key(0){}


	~DivisorsHash() {}     



	void setKey (int i) { key=i; return; }
	int  getKey () const { return key;}


        std::vector<int> findDivisors () {
		if (key<0) key*=-1;
	
                unsigned int  keysqrt = (unsigned int) sqrt (key);
                for (unsigned int i=1; i<=keysqrt;i++ )
                    if (key%i==0) { /*std::cout<<"i="<<i<<std::endl;*/ divisors.push_back(i);
                        if (i>1 && i< key/i) divisors.push_back(key/i); }

                std::sort(divisors.begin(),divisors.end(),wayToSortInt);
                return divisors;
	}

	    std::vector<int> getDivisors() const { return divisors;}
	
	
	






/// to print out the DivisorsHash
friend std::ostream & operator <<(std::ostream & out, const DivisorsHash & right){
		std::stringstream ss;
		std::vector<int> Divisors = right.getDivisors();
		int Key = right.getKey();
 		char str[100];
		sprintf(str, "%d => [", Key);
		std::string tmp = str;
		ss<<tmp;
		for (int i=0;i<Divisors.size()-1;i++) 
			{
				sprintf(str,"%d,",Divisors[i]);
				tmp=str;
				ss<<tmp;
			}
		sprintf(str,"%d]",Divisors[Divisors.size()-1]);
		tmp=str;
		ss<<tmp;	
		out<<ss.str();
	}


private:

	int key;
        std::vector<int> divisors;

}; 


#endif
