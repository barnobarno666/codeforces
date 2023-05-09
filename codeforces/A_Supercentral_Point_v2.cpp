
#include <bits/stdc++.h>
 
using namespace std;
int main(){

int n;
    cin >> n;
    array<int, 2> a[n];
    array<int, 2> bara[n];
    for(int i=0;i<n;i++){
        cin  >> a[i][0] >> a[i][1];
    }
   
sort(a,a+n);
 cout << a[5][1];
for(int i=0;i<n;i++){
        bara[i][0] =1001;
        bara[i][1]=1001;
    }
    /*/
  for(int i=0;i<n-2;i++){
if(a[i][0]==a[i+1][0]==a[i+2][0]){

}

  //}
  /**/

}
