#include <string>
#include <string.h>
#include <iostream>
#include <vector>
#include <list>
#include <iostream>
#include <sstream>  
#include <stdio.h>
#include <math.h>
#include <algorithm>

#ifndef Path_h
#define Path_h


class Node;
class Edge;
//class Path;

class Path/*: public Graph*/
{
public:

 	Path (const char * _name): name(_name),latex(false) {}
        Path (const char * _name, std::list<Node> lst ): name(_name), nodes(lst),latex(false) {}
	~Path () {}
	 

	void setNode (Node *  node) {

	if (node!=NULL) nodes.push_back(*node);
	
	return ;
	}




        std::list<Edge *>   getEdges() const  {

            std::list<Node>::const_iterator i = nodes.begin();

                const Node * prev= &*i;
                ++i;

            std::list<Edge *> lst_edges;

            for (;i!=nodes.end();++i){
  //              std::cout<<"In loop 1\n\n";
                std::vector<Edge *>  edges = prev->getEdges();
 //               std::cout<<"Edges size "<<edges.size()<<std::endl;

                for (unsigned int j=0; j<edges.size();++j)
                {
                    /*
                    std::cout<<"(1)in edge:" <<edges[j]->getOrigin()->getName()<<"\n\n";
                    std::cout<<"(2)in edge:" <<edges[j]->getTarget()->getName()<<"\n\n";
                    std::cout<<"name iterator:" <<i->getName()<<"\n\n";
                    std::cout<<"prev: "<<prev->getName()<<"\n\n";
                    */

                    if ( edges[j]->getOrigin()->getName() == prev->getName() &&
                    edges[j]->getTarget()->getName() == i->getName() )
                    {  lst_edges.push_back(edges[j]); /*std::cout<<"got it\n\n";*/ }

            }
                                    prev = &*i;
                    //std::cout<<"Last \n\n";


            }

            return  lst_edges;

        }


        std::list<Node *>   getNodes() const  {
            std::list<Node *> lst;

            for (std::list<Node>::const_iterator i=nodes.begin();i!=nodes.end();++i)
                lst.push_back(const_cast<Node *>(&*i));
            return lst;

        }

	std::string getName() const {return name;}

        float getTotalWeight() const {
            float res=0;
            std::list<Edge* > edges = getEdges();
            for (std::list<Edge *>::iterator i=edges.begin();i!=edges.end();++i)   res+=(*i)->getWeight();

            return res;
        }



        bool setLatex();
        bool getLatex() const { return latex;}



/// to print out the Node
friend std::ostream & operator <<(std::ostream & out, const Path & right);


private:

std::string name;
std::list<Node > nodes;
bool latex;


};





#endif
