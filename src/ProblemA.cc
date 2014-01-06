#include "ProblemA.h"
#include <fstream>
#include <iostream>
#include <vector>


using namespace std;
int main ()
{

	int indexs [] = {7,4,2,10,3,6,18,5};
	size_t size = sizeof(indexs)/sizeof(int);
	std::vector<int> vec_indx (size);


	vec_indx.assign(indexs,indexs+size);


	ProblemA prblmA;

	prblmA.setKeys(vec_indx);

	cout<<prblmA;

return 0;
}
