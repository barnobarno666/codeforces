
#include <bits/stdc++.h>
 
using namespace std;
int main(){ 
    int n;
    cin >> n;
    for(int i=0;i<n;i++){
        int a;
        cin >> a;
        int ara[a];
        int bara[a];
        for(int i=0;i< a;i++){
            cin >> ara[i];
            bara[i]=ara[i];
        }
        int k=0;
        sort(ara,ara+a);
        for(int i=0;i <a;i++){
            if(ara[a-1]==bara[i]){
                k=i;
            }

        }
       // cout  << bara[k] <<endl;
          int b=ara[a-1];
        //cout << b <<endl  ;
        for(int i=0; i< a;i++ ){
           
            if(i==k){
               // cout <<1;
                cout << bara[i]-ara[a-2] <<endl; 
            }
            else{
            int x= bara[i]-b  ;
            std::cout << x <<endl ;
            }
            }
          
        }
        //cout << endl;


}
    
    