
#include <bits/stdc++.h>
 
using namespace std;
long long num_gen(int n,int j){
    long long sux=0;
    int k;
    for(int i=n;i>0;i--){
        sux=5*pow(10,i)+sux;
        k=n;
    }
    sux=sux/10;
    while (k<=j)
    {
         k=k+1;
        sux=sux*10;
       
        
    }
    return sux/10 ;
    
}
int main(){


    cout << num_gen(2,3);
}