#include <string>
#include <iostream>
#include <vector>
#include <iostream>
#include <sstream>  
#include <stdio.h>
#include <math.h>

#ifndef Edge_h
#define Edge_h




class Node;

class Edge 
{
public:


//	Edge() ;
	Edge (const char * _name,double wgt, Node *  & orig, Node *  & target);
 

	~Edge() {}
	 
	double getWeight () const { return weight;} 
	std::string getName() const {return name;}
	Node* getOrigin ()  const { return origingNode;}
	Node * getTarget ()  const { return targetNode;}

	friend std::ostream & operator <<(std::ostream & out, const Edge & right); 

        bool setLatex();
        bool getLatex() const { return latex;}

private:

std::string name;
double weight;
Node * origingNode;
Node * targetNode;
bool latex;

};

#endif