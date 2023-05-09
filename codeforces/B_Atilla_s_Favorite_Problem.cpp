

#include <bits/stdc++.h>
 
using namespace std;
int main(){
    int n;
    cin  >> n;
    char fck[26]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' };

    for(int i=0;i<n;i++){
    int a;
    cin >> a;
    string f;
    cin >> f;
    char b[a];
    for(int i=0;i<a;i++){
        b[i]=f[i];

    }
    sort(b,b+a) ;
    char x= b[a-1];
    for(int i=0;i<26;i++){
        if(x==fck[i]){
            cout << i+1 << endl ;
        }

    } 
    
        
    }
}