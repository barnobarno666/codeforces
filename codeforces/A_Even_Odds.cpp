
#include <bits/stdc++.h>
 
using namespace std;
int main(){
    //1,2,3,4,5,6,7,8,9,10
    /*/ // {1, 3, 5, 7, 9, 2, 4, 6, 8, 10}
    long long  n, k;
    cin >> n >> k;
    if(n%2==0){
        int x=n%2 ;
        if( k<=x ){
        for(int i=0;i<n;i++){

        }    
        }

    }
    else{


    }
    
/**/
  long long  n, k;
    cin >> n >> k;
    long long i = 1;
    long long r=0;
    while (i<=n )
    {   r=r+1 ;
         if (r>=k){
            break;
        }
        i=i+2;
       
       
    }
    if(r<k){
        i=2;
        while (i<=n){
              r=r+1;
         if ( r>=k ){
                break;
            }
         i=i+2;
          
           
        }
        
    }
    
cout << i ;

}