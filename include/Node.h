#include <string>
#include <iostream>
#include <vector>
#include <iostream>
#include <sstream>  
#include <stdio.h>
#include <math.h>
#include <algorithm>

#include <stdlib.h>
#include <time.h>

#ifndef Node_h
#define Node_h




class Edge;


class Node 
{
public:

	Node (const char * _name): name(_name),latex(false) { x=getRandom(15.); y=getRandom(20.); _index=index++;        }
	~Node () {}
	 


	bool static sortEdges( Edge * rec1, Edge * rec2) { return rec1->getWeight() < rec2->getWeight(); }

	std::vector<Edge *>  getEdges() const { return edges;}
	std::string getName() const {return name;}


        unsigned int getIndex() const { return _index;}

        bool setLatex();
        bool getLatex() const {return latex;}



                float getRandom( float range) const {

                float x=(float)rand()/((float)RAND_MAX+1);
                x=(rand() + x)/RAND_MAX;
                x=range*(rand() + x)/RAND_MAX;

                return x;
                }

        float getX() const{return x;}
        float getY() const{return y;}
        friend class Edge;




/// to print out the Node
friend std::ostream & operator <<(std::ostream & out, const Node & right);

private:



	void setEdge (Edge *  edg) {

	if (edg!=NULL) edges.push_back(edg);

	std::sort(edges.begin(),edges.end(),Node::sortEdges);
	return ;
	}


std::string name;
std::vector<Edge * > edges;
bool latex;
float x;
float y;
unsigned int _index;
static unsigned int index;
};



         inline   bool operator <(const Node & a, const Node & b) { return a.getIndex()<b.getIndex(); /*return a.getName()<a.getName();*/}

#endif
