#include <iostream> 
#include <iomanip> 
#include <new> 
#include <string> 
#include <cstdlib> 
#include <ctime>
#include<algorithm>
#include <cstring>
#include <time.h> 

using namespace std;
void perm(int*,int,int);
void mission3(int* num,int N, int i,int fac);
void mission4(int* num,int N, int i,int fac,int M);

int tittle = 1;
int main(void){
	int command = 0; 
	do{
		cout << endl << "** Permutation Generator **";
		cout << endl << "* 0. Quit *";
		cout << endl << "* 1. N numbers from 1..N *";
		cout << endl << "* 2. M numbers from input *";
		cout << endl << "* 3. M numbers from 1..9 *";
		cout << endl << "***************************";
		cout << endl << "Input a choice(0, 1, 2, 3): ";
		cin >> command; 
		double START,END;
		START = clock();
		int N; // permutation length
		int M;
		int i;
		string N_temp;
		switch (command){ 
			case 0: 
				break;
			case 1: {
				cout<<endl<<"Input a number: ";
				cin >> N;
				
				while (N > 9 or N < 1){
					cout << endl << "### It is NOT in [1,9] ###";
					cout << endl << "Input a number: ";
					cin >> N;
				} 
				int *num = new int[N];  
				for( i = 0; i < N; i ++ ){
					num[i] = i+1;
				}
				perm(num,N,0);
				cout <<"Mission 1:"<<tittle-1<<" permutations";
				cout <<endl<<"L="<<N;
				delete num;
				break;
			}
			case 2:{
				cout<<endl<<"Input a number: ";
				cin >> N; // 
				while (N > 9 or N < 2){
					cout <<endl<< "### It is NOT in [2,9] ###";
					cout<<endl<<"Input a number: ";
					cin >> N;
				} 
				int *num = new int[N];
				for( i = 0; i < N; i ++ ){
					cout<<endl<<"Input a number: ";
					int num_temp = 0;
					cin >> num_temp;
					while (find(num,num+N,num_temp)!= num + N){//§PÂ_¬O§_­«½Æ 
						cout <<endl<< "### Duplicate! Still need 1 numbers! ###";
						cout <<endl<<endl<<"Input a number: ";
						cin >> num_temp;
					} 
					num[i] = num_temp;
				}
				perm(num,N,0);
				delete num;
				cout <<"Mission 2:"<<tittle-1<<" permutations";
				END = clock();
				cout <<endl<< "T="<<(END - START)<<"ms"<<endl;
				break;
			}
			case 3:{
				cout<<endl<<"Input a number: ";
				cin >> N;
				
				int *num = new int[9];  
				for( i = 0; i < 9; i ++ ){
					num[i] = i+1;
				}
				int fac = 1,l = 9 - N;
				for( int q = 1; q <= l ; q++ ) {
					fac *= q;
				}
				mission3(num,N,0,fac);
				cout <<"Mission 3:"<<tittle/fac<<" permutations";
				cout <<endl<<"L="<<N;
				delete num;
				break;
			}
			case 4:{
				cout<<endl<<"Input a number: ";
				cin >> M;
				cin >> N;
				
				int *num = new int[M];  
				for( i = 0; i < M; i ++ ){
					num[i] = i+1;
				}
				int fac = 1,l = M - N;
				for( int q = 1; q <= l ; q++ ) {
					fac *= q;
				}
				mission4(num,N,0,fac,M);
				cout <<"Mission 4:"<<tittle/fac<<" permutations";
				cout <<endl<<"L="<<N;
				delete num;
				break;
			}
			default:
				cout<<endl<<"Command does not exist!"<<endl;
		}
		tittle = 1;
	}while(command != 0);
	return 0;
}
void mission3(int* num,int N,int i, int fac){
	int j, k, temp; 
	
    if(i == 9 ) { 
    	if(tittle % (fac*(9-N+1))== 0){
    		cout<<"["<<tittle/fac<<"]";
        	for(j = 0; j < N; j++) 
            	cout<<" "<<num[j];
            cout<<endl;
    	}
    	tittle++;
    } 
    else { 
        for(j = i; j < 9; j++) { 
            temp = num[j]; 
            
            for(k = j; k > i; k--) 
                num[k] = num[k-1]; 
            num[i] = temp;

            mission3(num,N,i+1,fac); 

            for(k = i; k < j; k++)
                num[k] = num[k+1];
            num[j] = temp;
        } 
    } 
}
void mission4(int* num,int N,int i, int fac,int M){
	int j, k, temp; 
	
    if(i == M ) { 
    	if(tittle % (fac*(M-N+1))== 0){
    		cout<<"["<<tittle/fac<<"]";
        	for(j = 0; j < N; j++) 
            	cout<<" "<<num[j];
            cout<<endl;
    	}
    	tittle++;
    } 
    else { 
        for(j = i; j < M; j++) { 
            temp = num[j]; 
            
            for(k = j; k > i; k--) 
                num[k] = num[k-1]; 
            num[i] = temp;

            mission4(num,N,i+1,fac,M); 

            for(k = i; k < j; k++)
                num[k] = num[k+1];
            num[j] = temp;
        } 
    } 
}
void perm(int* num,int N, int i){
	int j, k, temp; 
    if(i == N) { //
        cout<<"["<<tittle<<"]";
    	tittle++;
        for(j = 0; j < N; j++) 
            cout<<' '<<num[j];
        cout<<endl;
    } 
    else {  
        for(j = i; j < N; j++) { 
            temp = num[j]; 
            
            for(k = j; k > i; k--) 
                num[k] = num[k-1]; 
            num[i] = temp; 

            perm(num,N,i+1); 

            
            for(k = i; k < j; k++) 
                num[k] = num[k+1]; 
            num[j] = temp; 
        } 
    } 
}  
