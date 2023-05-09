
#include <bits/stdc++.h>
 
using namespace std;
int main(){
int n;
cin >> n;
int ara[7];
for(int i=0;i< 7;i++){
    cin >> ara[i];
}
int j;
while (n>=0){
for(int i=0;i< 7;i++){
    if (n>=0) {n-ara[i];
    j++ ;}
    }
if(n<=0){
    break;
}

}
cout << (j&7)+1 ;



}
