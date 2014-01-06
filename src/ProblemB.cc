
#include "Edge.h"
#include "Node.h"
#include "Graph.h"
#include "Path.h"

#include "ProblemB.h"
#include <fstream>
#include <iostream>
#include <vector>


using namespace std;
int main ()
{



    ofstream file_graph;
    ofstream file_path;

    file_graph.open("latex/graph_ProblemB.tex");
    file_path.open("latex/path_ProblemB.tex");
    	Node * nd11=NULL;
	Node * nd22=NULL;
        Node * nd21=NULL;
        Node * nd31=NULL;
        Node * nd41=NULL;

        Edge* edg1 = new Edge("edge1",2.0,nd11,nd21);
        Edge* edg5 = new Edge("edge5",1.0,nd21,nd31);
        Edge* edg6 = new Edge("edge6",0.1,nd31,nd22);
        Edge* edg7 = new Edge("edge7",0.5,nd31,nd41);
        Edge* edg8 = new Edge("edge8",2.0,nd22,nd41);
        Edge* edg9 = new Edge("edge9",0.1,nd22,nd31);

        Node * nd1 = new Node("node1");

        Edge* edg2 = new Edge("edge2",0.5,nd1,nd11);
        Edge* edg3 = new Edge("edge3",2.5,nd1,nd22);

        Graph * gr1 = new Graph("graph1");

        gr1->setEdge(edg1);
        gr1->setEdge(edg2);
        gr1->setEdge(edg3);
        gr1->setEdge(edg5);
        gr1->setEdge(edg6);
        gr1->setEdge(edg7);
        gr1->setEdge(edg8);
        gr1->setEdge(edg9);

        cout<<*gr1;
        cout<<"\n\n";

        gr1->setLatex();
        file_graph<<*gr1;

        ProblemB prblmB(gr1);
 //       Path path1 = prblmB.getShortestPath(nd1,nd22);
        Path path1 = prblmB.getShortestPath(nd1,nd41);
        cout<<path1;
        cout<<"\n\n";

        path1.setLatex();
        cout<<path1;
        cout<<"\n\n";

        file_path<<path1;

        delete nd11;
        delete nd22;
        delete nd31;
        delete nd41;
        delete nd1;
        delete gr1;
        delete edg1;
        delete edg5;
        delete edg6;
        delete edg7;
        delete edg9;

        file_graph.close();
        file_path.close();

return 0;
}
