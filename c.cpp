#include <iostream>
#include <string>
#include <algorithm>


int main(){
    string a, b, c, mi;
    nextline(cin, a);
    nextline(cin, a);
    nextline(cin, a);
    if(a.length()>b.length()>c.length()){
        mi = a;
    }else if(a.length()<b.length()<c.length()){
        mi= b;
    }else{
        mi= c;
    }
    int i=0,k=mi.length();
    mi=mi[i:k];
    for(int i =0 ;i<mi.length(); i++){
        if(a.find(mi)!=std::string::npos && b.find(mi)!=std::string::npos && c.find(mi)!=std::string::npos){
            cout << mi;
            break;   
        }else{
            if(k=0){
                k--;
                string lol;
                for(int j=i; j<k; j++){
                    lol.append(mi[j]);
                }
                mi=lol;
            }else{
                i++;
                k=mi.length();
            }
        }
    }
}