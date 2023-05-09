
#include <bits/stdc++.h>
 
using namespace std;
int main(){
int a[10]= {1, 3 , 5, 7, 9,11, 2, 4, 6, 8};
  long long  n, k;
    cin >> n >> k;
    long long i = 1;
    long long r=0;
    if(k>n/2){
        if(n%2==0){
            k=k-n/2;
        }
        else if( n% 2!=0){
             k=k -(n+1)/2;
        }
        i=2;
        while (i<=n){
              r=r+1;
         if ( r>=k ){
                break;
            }
         i=i+2;
          
           
        }
return 0;    }
else{
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
    
cout << i;
}}