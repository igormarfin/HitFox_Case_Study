#include <string>
#include <iostream>
#include <vector>
#include <iostream>
#include <sstream>  
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <utility>


#ifndef ProblemB_h
#define ProblemB_h


class Path;
class Graph;
class Node;


#ifndef INT_MAX
#define INT_MAX 100
#endif

class ProblemB 
{
public:

    ProblemB (Graph * _gr): gr(_gr) {

        if (_gr != NULL) {
            if (dist != NULL)  delete [] dist;
            dist = new float [_gr->getNodes().size()];
        }
    }
	~ProblemB () {delete [] dist;}
         Path getShortestPath (Node * src, Node *trgt) const;



    



private:


    struct ltDist {
bool operator()( const Node & u, const  Node & v ) const {
    return std::make_pair( ProblemB::dist[u.getIndex()], u.getIndex() ) < std::make_pair( ProblemB::dist[v.getIndex()], v.getIndex() );
}
};


    Graph * gr;
    static float * dist;



};



#endif
