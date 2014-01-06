#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <iostream>
#include <sstream>  
#include <stdio.h>
#include <math.h>
#include <algorithm>

#ifndef Graph_h
#define Graph_h


class Node;

class Edge;

class Graph 
{
public:

	Graph (const char * _name): name(_name),latex(false) {}
	~Graph () {}
	 

/*
	void setNode (Node *  node) {
	if (node!=NULL) nodes.push_back(node);
	return ;
	}

*/


	void setEdge (Edge *  edge) {
	if (edge!=NULL) edges.push_back(edge);
	return ;
	}




//	std::vector<Node *>  getNodes() const { return nodes;}
	std::set<Node>  getNodes() const {
        std::set<Node> nodes;
        for (unsigned int i=0; i<edges.size(); i++)
        {
          nodes.insert(*edges[i]->getOrigin());
          nodes.insert(*edges[i]->getTarget());

        }


        return nodes;

}
	std::vector<Edge *>  getEdges() const { return edges;}


	std::string getName() const {return name;}



        bool setLatex();
        bool getLatex() const { return latex;}



/// to print out the Node
friend std::ostream & operator <<(std::ostream & out, const Graph & right);

private:

std::string name;
//std::vector<Node * > nodes;
std::vector<Edge * > edges;

bool latex;
};


#endif
