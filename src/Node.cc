#include "Edge.h"
#include "Node.h"

#include <fstream>
#include <iostream>
#include <vector>


using namespace std;
int main ()
{

//	Node<Edge> * nd1 = new Node <Edge>("node1");
//	Node<Edge> * nd2 = new Node<Edge>("node2");
	

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
/*
	nd22->setEdge(edg2);

	cout<<*nd22;	
*/

/*
	nd1->setEdge(edg1);
	cout<<*nd1;
*/
	

/*	Edge * edg2 = new Edge("edge2",1.0,nd22,nd2);
	Edge * edg3 = new Edge("edge3",.4,nd1,nd2);
*/
        delete nd11;
        delete nd22;
        delete edg1;
        delete edg2;

        delete nd1;

return 0;
}
