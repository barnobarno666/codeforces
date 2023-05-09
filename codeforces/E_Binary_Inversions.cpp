
#include <bits/stdc++.h>
 
using namespace std;
int main(){ 
    int t;
    cin >> t;
    for(int i=0;i<t;i++){
        int n;
        cin >> n;
        cout << n;
        int bara[n]; 
     
        for(int j=0;j<n;j++){
            cin >> bara[j];
        } 
        //std::cout << 5;
        //cout << 7  ;
        int oner =0;
        int zero=0;
        for(int i=0;i< n;i++){
            if(bara[i]=1){oner++;}
            else if(bara[i]==0){zero ++;}
        }   
        //if( oner>zero &&  bara[n-1]!=0 ){
          //  bara[n-1]=0;
        //}
        //else if(zero > oner && bara[0]!=0){
          //  bara[0]=1;
        //}
        if(oner > zero){
            for(int i=n-1;i>=0;i--){
                if(bara[i]=1){
                    bara[i]=0;
                    break;
                }
            }

        }
        else if(  zero >oner){
            for(int i=0;i<n;i++){
                if(bara[i]==0){
                    bara[i]=1;
                    break;
                }
            }
        }
        int kk=0;
        for(int i=0;i<n;i++){
            if(bara[i]==1){
                for(int j=i;i<n;j++){
                    if(bara[j]==0){
                        kk++;
                    }
                }
            }

        }
    cout << kk <<endl;
    }
    
    }