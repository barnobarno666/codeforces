#include <bits/stdc++.h>
using namespace std;
#define ll long long


int main(){ 
ll t;
cin  >> t;
for(int i =0; i < t;i++){
    ll n;
    cin >>  n;
    ll a[n],b[n];
    for(int i=0;i<n;i++){
        cin >> a[i];
    }
    for(int i=0;i< n;i++){
        cin >> b[i];
    }
    bool ff=true;
    for (int i=0;i<n;i++)
    {
        bool check=false;
        for (int j=0;j<n  ;j++)
        {
            if (a[j]%b[i]!=0){
                check=true;
                break;
            }

        }
        if (check==false){
            ff=false;
            break;
            }
    }
    if (ff){
        cout << "YES";
    }
    else{
        cout << "NO";
    }
    bool ans=true;
    int divisor=(a[0]/b[0]);
    int reminder =0;
    for(int i=0;i<n;i++){
        reminder=a[i]%b[i];
        if ((a[i]/b[i])!=divisor){
            ans=false;
            break;
        }
        if(reminder!=0){
            ans=false;
            break;

        }
        

    }
    if (ans){
        cout << "YES";
    }
    else{
        cout << "NO";
    }

    



}
