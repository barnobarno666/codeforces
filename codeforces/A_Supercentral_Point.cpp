
#include <bits/stdc++.h>
 
using namespace std;
int main(){
    int n;
    cin >> n;
    array<int, 2> a[n];
    array<int, 2> b[n];
    for(int i=0;i<n;i++){
        cin  >> a[i][0] >> a[i][1];
        b[i][0]=a[i][1];
        b[i][1]=a[i][0];
        
    }
        sort(a,a+n);
   //  for(int i=1;i<n;i++){
     //     if(a[i][0]==a[i+1][0] && a[i-1][0]){
             
             
       //  } }
        int r=0;
        //vector <int> v;
        for(int i=0;i<n;i++){
            if(a[i][0]==a[i+1][0]){
                r=r+1;
                //if(i==  )
                
            } }
        sort(b,b+n);
        int  k=0;
        //vector <int> v;
        for(int i=0;i<n;i++){
            if(b[i][0]==b[i+1][0]){
                k=k+1;
                //if(i==  )
                
            }
            
        }
        
        cout  << ceil(2*min(r,k)/3 );   
} 


