#include <bits/stdc++.h>
using namespace std;
#define ll long long


int main(){ 
long long t;
cin >> t;
while (t--)
{
    long long sum=0;
    long long offset=0;
    long long n, k;
    cin >> n >> k;
    long long a[n];
    for(int i=0;i<n;i++){
        cin >> a[i];
        sum=sum+a[i];
    }
    for(int i=0;i<n-1;i++){
        if (a[i+1]-a[i] >0){
            offset =offset+a[i+1]-a[i];
        }
    }
    long long f=offset+sum-a[0];
    long long ans=sum+(k/2)*(k+1)*f;
    cout << ans ;
}
