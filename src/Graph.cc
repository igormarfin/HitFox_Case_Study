#include "Edge.h"
#include "Node.h"
#include "Graph.h"
#include "Path.h"

#include <fstream>
#include <iostream>
#include <vector>

#include <stdlib.h>
#include <time.h>


using namespace std;
int main ()
{

        srand(time(NULL));


//	Node<Edge> * nd1 = new Node <Edge>("node1");
//	Node<Edge> * nd2 = new Node<Edge>("node2");
	

	Node * nd11=NULL;
	Node * nd22=NULL;
	Edge* edg1 = new Edge("edge1",2.0,nd11,nd22);

/*
	cout<< *edg1;

	cout<<"\n";
	cout<<"\n";

	cout<<*nd11;

	cout<<"\n";
	cout<<"\n";

	cout<<*nd22;	

	cout<<"\n";
	cout<<"\n";
*/

	Node * nd1 = new Node("node1");
/*
	cout<<*nd1;	

	cout<<"\n";
	cout<<"\n";

*/
	Edge* edg2 = new Edge("edge2",.5,nd1,nd11);
//	nd22->setEdge(edg2);

//	cout<<*nd22;	


/*
	nd1->setEdge(edg1);
	cout<<*nd1;
*/

	Graph * gr1 = new Graph("graph1");
        gr1->setEdge(edg1);
        gr1->setEdge(edg2);

//	gr1->setNode(nd1);
//	gr1->setNode(nd11);
//	gr1->setNode(nd22);

	cout<<*gr1;

	cout<<"\n";
	cout<<"\n";

        gr1->setLatex();
	cout<<*gr1;


	Path * pt1 = new Path("path1");
	pt1->setNode(nd1);
	pt1->setNode(nd11);	
	pt1->setNode(nd22);

	cout<<*pt1;

	delete nd11;
	delete nd22;
	delete edg1;
	delete edg2;
	delete nd1;
	delete gr1;
	delete pt1;

return 0;
}
