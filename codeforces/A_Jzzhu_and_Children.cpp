

#include <bits/stdc++.h>

using namespace std;
int main(){
    int n,m;
    cin >> n >> m ;
    array<int, 2> a[5050];
    for(int i=0;i<5050;i++){
        //for(int j=0;j<5050;j++){
            a[i][0]=0;
        
    }
    for(int i=0;i<5050;i++){
        //for(int j=0;j<5050;j++){
            a[i][1]=i;
        
    }
 for(int i=0;i<5050;i++){
    cin >> a[i][0];
 }
int r=n;
 for(int i=0;i<5050;i++){
    if( a[i][0]-m >0  ){
        a[r][0]=a[i][0]-m ;
        a[r][1]=a[i][1];
        r++;
    }    
 }
for(int i=5049;i>=0;i--){
    if(a[i][0]!=0){
       // cout << a[i][1] ;
        cout << a[a[i][1]][1] +1 ;
        break;

    }
}
//cout << a[7][0];
}