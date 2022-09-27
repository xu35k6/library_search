#include <iostream> 
#include <iomanip> 
#include <new> 
#include <string> 
#include <cstdlib> 
#include <ctime>
#include<algorithm>
using namespace std;
void perm(int*,int,int);
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
		int N; // permutation length
		int i;
		switch (command){ 
			case 0: 
				break;
			case 1: {
				cout<<endl<<"Input a number: ";
				cin >> N; // 輸入要排列幾個數字
				while (N > 9 or N < 1){
					cout << endl << "### It is NOT in [1,9] ###";
					cout << endl << "Input a number: ";
					cin >> N;
				} 
				int *num = new int[N];  
				for( i = 0; i < N; i ++ ){
					num[i] = i+1;
				}
				perm(num,N,0);//
				delete num;
				break;
			}
			case 2:{
				cout<<endl<<"Input a number: ";
				cin >> N; // 輸入要排列幾個數字
				while (N > 9 or N < 2){
					cout <<endl<< "### It is NOT in [2,9] ###";
					cout<<endl<<"Input a number: ";
					cin >> N;
				} 
				int *num = new int[N];
				for( i = 0; i < N; i ++ ){
					cout<<endl<<"Input a number: ";
					int num_temp = 0;
					cin >> num_temp;//暫存數字判斷是否重複 
					while (find(num,num+N,num_temp)!= num + N){
						cout <<endl<< "### Duplicate! Still need 1 numbers! ###";
						cout <<endl<<endl<<"Input a number: ";
						cin >> num_temp;
					} 
					num[i] = num_temp;
				}
				perm(num,N,0);
				delete num;
				break;
			}
			case 3:{
				/*cout<<"Input a number: ";
				cin >> N;
				int *num = new int[N];  
				for( i = 0; i < N; i ++ ){
					num[i] = i+1;
				}
				perm3(num,N)*/ 
				break;
			}
			default:
				cout<<endl<<"Command does not exist!"<<endl;
		}
		tittle = 1;
	}while(command != 0);
	return 0;
}

void perm(int* num,int N, int i){
	int j, k, temp; 
    if(i == N) { //代表 
        cout<<"["<<tittle<<"]";
    	tittle++;
        for(j = 0; j < N; j++) 
            cout<<' '<<num[j];
        cout<<endl;
    } 
    else {  
        for(j = i; j < N; j++) { 
            temp = num[j]; 
            // 旋轉該區段最右邊數字至最左邊 
            for(k = j; k > i; k--) 
                num[k] = num[k-1]; 
            num[i] = temp; 

            perm(num,N,i+1); 

            // 還原 
            for(k = i; k < j; k++) 
                num[k] = num[k+1]; 
            num[j] = temp; 
        } 
    } 
}  

