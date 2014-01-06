#include "DivisorsHash.h"
#include <fstream>
#include <iostream>


using namespace std;
int main ()
{

	DivisorsHash dh;
	dh.setKey(10);
	std::vector<int> divs = dh.findDivisors();
//	for (int i=0; i<divs.size();i++) cout<<divs[i]<<endl;
	cout<<dh; cout<<"\n";

return 0;
}
