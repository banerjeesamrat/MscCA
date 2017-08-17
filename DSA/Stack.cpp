//============================================================================
// Name        : Stack.cpp
// Author      : Mihir Vohra
//============================================================================

#include <iostream>
using namespace std;

class Stack{
private:
	int size;
	int top;
	char * info;
public:
	Stack(int SIZE=1){
		if (SIZE<1){
			cerr<<"Improper size";
			exit(1);
		}
		info=new char[SIZE];
		if (info==NULL){
			cerr<<"No memory\n";
			exit(0);
		}
		size=SIZE;
		top=-1;
		cout<<"Creating stack of size "<<size<<"\n";
	}

	~Stack(){
		cout<<"\nDestroying stack of size "<<size<<"\n";
		delete[] info;
	}
	bool empty() const{
		if (top==-1)
			return true;
		return false;
	}

	bool full() const{
		if (top==size-1)
			return true;
		return false;
	}

	void push(char data){
		info[++top]=data;
	}

	char pop(){
		return info[top--];
	}
};

int main(){
	cout<<"Stack as Array in C++\n";
	char ch='A';
	Stack stk(5);

	if(stk.empty()){
		cout<<"Empty Stack\n";
	}
	cout<<"Pushing data";
	while(!stk.full()){
		cout<<endl<<ch;
		stk.push(ch++);
	}

	cout<<"\nPopping data";
	while(!stk.empty()){
		cout<<endl<<stk.pop();
	}
	cout<<"\nEnd of Job";
	return 0;
}//end main
