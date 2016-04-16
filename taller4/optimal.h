#define K unsigned long
#define I long

#include <vector>
#include <map>

using namespace std;

void printM(std::map< unsigned long  , std::map< unsigned  long , K > > m){
    for(I i=0;i<m.size();i++){
        for(I j=0;j<m[i].size();j++){
            cout<<m[i][j]<<" ";
        }
        cout<<endl;
    }
    cout<<endl;
}


std::map< unsigned long  , std::map< unsigned long  , K > > optimal_binary_tree_MI( std::map< unsigned long  , K > &p, std::map< unsigned long  , K > &q ) {

    //std::map< unsigned long long , std::map< unsigned long long , K > >
    //  std::cout<<"llega"<<std::endl;
    std::map< unsigned long  , std::map< unsigned long  , K > > m;
    std::map< unsigned long  , std::map< unsigned long  , K > > t_;
    std::map< unsigned long  , K > wq;
    std::map< unsigned long  , K > wp;
    //std::cout<<"llega"<<std::endl;
    //std::cout<<"El tamanio del mapa es " << q.size() << std::endl;
    for( K i=0 ; i<q.size() ; i++ ){

        m[i][i]=q[i];
          //std::cout<<"El tamanio del mapa es " << q.size() << std::endl;
    }
    //std::cout<<"llega"<<std::endl;
    //printM(m);
    for(K i=0;i<p.size();i++){
        wp[i+1]=wp[i]+p[i];
        wq[i+1]=wq[i]+q[i];
    }
    wq[q.size()]=wq[q.size()-1]+q[q.size()-1];
    I i,k;
    K temp;
    for(I g=0;g<p.size()+1;g++){
        i=0;
        for (I j=g;j<p.size()+1;j++){
            for (I n=0;n<g;n++){
                k=i+n;
                //cout<<" i: "<<i<<" j: "<<j<<" k: "<<k<<" "<<(wq[j+1]-wq[i])+(wp[j]-wp[i])<<endl;
                temp=m[i][(k+1)-1]+m[(k)+1][j]+(wq[j+1]-wq[i])+(wp[j]-wp[i]);
                if( n==0 || m[i][j] > temp ){
                    m[i][j]=temp;
                    t_[i][j]=k+1;
                }
            }
            i++;
        }
        //cout<<endl;
    }
    return m;
     //printM(m);
     //printM(t_);
}
