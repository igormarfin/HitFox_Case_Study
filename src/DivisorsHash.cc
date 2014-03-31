#include "DivisorsHash.h"
#include <fstream>
#include <iostream>


using namespace std;
int main ()
{

	DivisorsHash dh;
	dh.setKey(10);
	std::vector<int> divs = dh.findDivisors();
	cout<<dh; cout<<"\n";

return 0;
}
