#include "Edge.h"
#include "Node.h"

#include <fstream>
#include <iostream>
#include <vector>


using namespace std;
int main ()
{

	

	Node * nd11=NULL;
	Node * nd22=NULL;
	Edge* edg1 = new Edge("edge1",2.0,nd11,nd22);



        edg1->setLatex();

	cout<< *edg1;

	cout<<"\n";
	cout<<"\n";

	cout<<*nd11;

	cout<<"\n";
	cout<<"\n";

	cout<<*nd22;	

	cout<<"\n";
	cout<<"\n";


	Node * nd1 = new Node("node1");

	cout<<*nd1;	

	cout<<"\n";
	cout<<"\n";



        Edge* edg2 = new Edge("edge2",.5,nd1,nd11);


        edg2->setLatex();

        cout<<*edg2;


       cout<<"\n\n";
        delete nd11;
        delete nd22;
        delete edg1;
        delete edg2;

        delete nd1;

return 0;
}
