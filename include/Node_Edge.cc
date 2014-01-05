#include "Edge.h"
#include "Node.h"
#include "Graph.h"
#include "Path.h"
#include "ProblemB.h"
#include <stdio.h>
#include <map>

unsigned int Node::index=0;
float * ProblemB::dist = NULL;

//Edge::Edge (const char * _name,double wgt, Node * & orig, Node *  & target): name(_name),weight(fabs(wgt))
Edge::Edge (const char * _name,double wgt, Node * & orig, Node *  & target): name(_name),weight(wgt)
{


                latex=false;

 
		std::string orig_name = name+std::string("-orig");
		std::string target_name = name+std::string("-target");
		if (orig != NULL ) orig->setEdge(this);
		else { orig  = new Node(orig_name.c_str()); /* std::cout<<orig_name<<std::endl; */ orig->setEdge(this); }

		if (target != NULL ) target->setEdge(this);
		else { target  = new Node(target_name.c_str()); /*std::cout<<target_name<<std::endl;*/ target->setEdge(this); }
		origingNode = orig;
		targetNode = target;




}

bool Edge::setLatex() {

     latex = !latex;


     if (origingNode != NULL)
     if (origingNode->getLatex()!= latex) origingNode->setLatex();
     if (targetNode != NULL)
     if (targetNode->getLatex()!= latex)targetNode->setLatex();

     return latex;
}

bool Node::setLatex() {
    latex = !latex;

    std::vector<Edge *>  Edges = getEdges();
    for (unsigned int i=0; i<Edges.size();++i)
    if (Edges[i] != NULL) if ( Edges[i]->getLatex()!=latex) Edges[i]->setLatex();

    return latex;

}



bool Graph::setLatex() {

        latex = !latex;
       	std::vector<Edge *>  Edges = getEdges();
        for (unsigned int i=0; i<Edges.size();++i)
        if (Edges[i] != NULL) if ( Edges[i]->getLatex()!=latex) Edges[i]->setLatex();


        return latex;
}

bool Path::setLatex() {

    latex = !latex;
//    std::cout<<getName()<<" : "<<latex<<"\n\n";
       	std::list<Node *> nodes = getNodes();
        for (std::list<Node *>::iterator i=nodes.begin();i!=nodes.end();++i)  {
       //     std::cout<<i->getName()<<" : " <<i->getLatex()<<"\n\n";
            if ( (*i)->getLatex() != latex ) (*i)->setLatex();
         //   std::cout<<i->getName()<<" : " <<i->getLatex()<<"\n\n";
     
        }
  
        return latex;
}


/// to print out the Node
std::ostream & operator <<(std::ostream & out, const Node & right)
{
//		out<<"in Node printing \n";
		std::vector<Edge *>  Edges = right.getEdges();
//                out<<right.getName(); out<<"\n\n";
//                out<<right.getLatex(); out<<"\n\n";

                if (!right.getLatex()) {
		out<<right.getName();
		out<<" == > [";
		out<<"\n";
		for (int i=0;i<Edges.size();i++) 
			{
				out<<*Edges[i];
				out<<"\n";
			}
		out<<"]\n";
                }
                else {



                out<<"\\tikzset{VertexStyle/.append  style={fill}}\n";
                char buf[100];
                sprintf(buf,"\\Vertex[x=%.1f ,y=%.1f]{%s}\n",right.getX(),right.getY(),right.getName().c_str());
                out<<buf;


                 }
}



/// to print out the Edge
std::ostream & operator <<(std::ostream & out, const Edge & right)
{

                if (!right.getLatex()) {
//		out<<"in Edge printing \n";
  //              out<<right.getName(); out<<"\n";
		out<<"{";out<<right.getName(); out<<":  ";
		out<<"(";out<<right.getWeight(); out<<",";out<<right.getOrigin()->getName(); out<<",";
		out<<right.getTarget()->getName(); out<<")";
		out<<"}";
                } else {

                char buf[100];
                out<<*right.getOrigin();
                out<<*right.getTarget();

                out<<"\\tikzset{EdgeStyle/.style={->}}\n";
                sprintf(buf,"\\Edge[label=$%.2f$](%s)(%s)\n",right.getWeight(),right.getOrigin()->getName().c_str(),right.getTarget()->getName().c_str());
                out<<buf;
                }

}



/// to print out the Graph
std::ostream & operator <<(std::ostream & out, const Graph & right)
{
                if (!right.getLatex()) {

//	std::vector<Node * > nodes = right.getNodes();
	std::set<Node > nodes = right.getNodes();
	out<<"Graph: "; out<<right.getName(); out<<" <<< \n";
//	for (int i=0;i<nodes.size();i++)   out<<*nodes[i];
	for (std::set<Node>::iterator it = nodes.begin();  it!=nodes.end();++it)   out<<*it;
	out<<" <<<\n";
       } else {

       out<< "\\documentclass[11pt]{scrartcl}\n \\usepackage{tkz-graph} \n \\begin{document} \n \\begin{center} \n";
       out<< "\\begin{tikzpicture}  \n \\SetVertexNormal[Shape      = circle, FillColor  = orange, LineWidth  = 2pt]\n";
       out<<"\\SetUpEdge[lw  = 2pt,  color      = black,  labelcolor = white,  labeltext  = red, labelstyle = {sloped,draw,text=blue}]\n";
       out<<"\\GraphInit[vstyle=Normal] \n   \\SetGraphUnit{10} \n";

       std::vector<Edge* > edges = right.getEdges();
       for (unsigned int i=0; i<edges.size();  ++i)   out<<*edges[i];

       out<<"\\end{tikzpicture}\n \\end{center}  \n \\end{document}\n";


       }


}


/// to print out the Path
std::ostream & operator <<(std::ostream & out, const Path & right)
{
    Path nonconstPath = static_cast<Path>(right);
    std::list<Node *> nodes = nonconstPath.getNodes();
//    std::cout<<"Before"<<"\n";

    std::list<Edge* > edges = nonconstPath.getEdges();

//    std::cout<<"edges size"<<edges.size()<<"\n";


    if (!right.getLatex()) {

        out<<"Path: "; out<<right.getName(); out<<"  with total weight: "; out<<right.getTotalWeight();
        out<<"   ****** \n";
	for (std::list<Node *>::iterator i=nodes.begin();i!=nodes.end();++i)   out<<*(*i);
	out<<" ******\n";

        } else {

       out<< "\\documentclass[11pt]{scrartcl}\n \\usepackage{tkz-graph} \n \\begin{document} \n \\begin{center} \n";
       out<< "\\begin{tikzpicture}  \n \\SetVertexNormal[Shape      = circle, FillColor  = orange, LineWidth  = 2pt]\n";
       out<<"\\SetUpEdge[lw  = 2pt,  color      = black,  labelcolor = white,  labeltext  = red, labelstyle = {sloped,draw,text=blue}]\n";
       out<<"\\GraphInit[vstyle=Normal] \n   \\SetGraphUnit{10} \n";
       
       //for (std::list<Node *>::iterator i=nodes.begin();i!=nodes.end();++i)   out<<*(*i);
       for (std::list<Edge *>::iterator i=edges.begin();i!=edges.end();++i)   out<<*(*i);
       out<<"\\end{tikzpicture}\n"; out<<"\\mbox{Total weight: "; out<<right.getTotalWeight(); out<<"}\n";
       out<<"\\end{center}  \n \\end{document}\n";
        }


}




Path ProblemB::getShortestPath(Node *src, Node *trgt) const
{

    if (src == NULL || trgt == NULL || gr == NULL )     return Path("shortest-path");

    std::set<Node> nodes = gr->getNodes();
    std::vector<Edge *> edges = gr->getEdges();
    std::map<int, std::list<Node> > paths;
    std::list<Node> path;
    std::list<Node>::iterator it3;


    unsigned int nNodes=nodes.size();
    std::list<std::pair<Node,float> > *adj = new std::list<std::pair<Node,float> >[nNodes];    // Pointer to an array containing adjacency lists
    unsigned int i,j;
    std::list<std::pair<Node,float> >::iterator it;
    for (i=0;i<edges.size();++i) adj[edges[i]->getOrigin()->getIndex()].push_back(std::make_pair(*edges[i]->getTarget(),edges[i]->getWeight()));


//    int graph[nNodes][nNodes]; // -1 means "no edge"/ 1 means "the edge"



    unsigned int srcIndx= src->getIndex();
    unsigned int trgtIndx=trgt->getIndex();

    i=0.;
    std::set<Node>::iterator it1, it2;
    for ( it1=nodes.begin(); it1!=nodes.end(); ++it1) {
        if (i==srcIndx) dist[i]=0.;
        else dist[i]=INT_MAX;
        ++i;
    }



/*

        for ( it2=nodes.begin(); it2!=nodes.end(); ++it2)
            graph[i++][j++]=-1;

            }
            for (i=0;i<edges.size();++i)
            graph[edges[i]->getOrigin()->getIndex()][edges[i]->getTarget()->getIndex()]=edges[i].getWeight();

*/

    std::set< Node, ltDist > q;
    q.insert( *src );
    paths[src->getIndex()].push_back(*src);

    while( !q.empty() ) {
        Node u = *q.begin();   // like u = q.front()
        q.erase( q.begin() ); // like q.pop()
       /*
        std::cout<<"Current min-dist node is "<<std::endl;
        std::cout<<u;
        std::cout<<"\n\n";
        std::cout<<"with index "<<u.getIndex();
        std::cout<<"\n\n";
        */
//        path.push_back(u);
        if(trgtIndx==u.getIndex())
//            return Path("shortest-path",path);
              return Path("shortest-path",paths[trgtIndx]);

        for(it = adj[u.getIndex()].begin(); it != adj[u.getIndex()].end(); ++it)
        {
                  /*
      
            if(paths.find(it->first.getIndex())==paths.end())
            {
                paths[it->first.getIndex()] = paths [u.getIndex()];
                paths[it->first.getIndex()].push_back(it->first);
            }
            if(trgtIndx==it->first.getIndex())
            return Path("shortest-path",paths[trgtIndx]);
            */
            //   else {
/*
            std::cout<<" in loop:: " <<std::endl;
            std::cout<<it->first;
            std::cout<<"\n";
            std::cout<<"\n";
            std::cout<<"with weight and index::"<<  it->second <<"  " << it->first.getIndex() <<"\n\n";
*/
            float newDist = dist[u.getIndex()] + it->second;
//            std::cout<<"newDist = "<<newDist<<"\n\n";
//            std::cout<<"oldDist = "<<dist[it->first.getIndex()]<<"\n\n";

            if (newDist < dist[it->first.getIndex()] )
            {
                /*
                std::cout<<"inserting \n\n";
                std::cout<<it->first;
                std::cout<<"\n";
                std::cout<<"\n";
                */
                if( q.count( it->first ) ) q.erase( it->first );
                dist[it->first.getIndex()] = newDist;
                q.insert( it->first );
                paths[it->first.getIndex()]=paths[u.getIndex()];
                paths[it->first.getIndex()].push_back(it->first);

            } /*else { it3=path.begin();++it3; while(it3 != path.end()) path.erase(it3++);}*/
           // }
        }


    }

    return Path("shortest-path");


    }

