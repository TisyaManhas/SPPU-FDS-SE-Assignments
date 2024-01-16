//CIRCULAR QUEUE
#include<bits/stdc++.h>
using namespace std;
class Node
{
    public:
    Node* next;
    int id;
    
    Node ()
    {
        next=NULL;
    }
    Node(int x)
    {
        id=x;
        next=NULL;
    }
};
void enqueue(Node* &rear,Node* &front,int x)
{
    Node* ptr=new Node(x);
    if(front==NULL)
    {
        front=rear=ptr;
    }
    else
    {
        rear->next=ptr;
        rear=ptr;
    }
    rear->next=front;
}
void dequeue(Node* &rear,Node* &front)
{
    if(front==NULL)
    {
        cout<<"Empty!!!"<<endl;
    }
    else
    {
    int data=front->id;
    cout<<data<<" is removed."<<endl;
    front=front->next;
    if(front==rear)
    {
        front=rear=NULL;
    }
    }
}
void display(Node* &rear,Node* &front)
{
    Node* ptr=front;
    cout<<"Displaying:"<<endl;
    while(ptr!=rear)
    {
        cout<<ptr->id<<" ";
        ptr=ptr->next;
    }
    cout<<rear->id;
    cout<<endl;
}
int main()
{
    Node* front=NULL;
    Node* rear=NULL;
    enqueue(rear,front,3);
    enqueue(rear,front,4);
    enqueue(rear,front,5);
    enqueue(rear,front,6);
    enqueue(rear,front,7);
    enqueue(rear,front,8);
    display(rear,front);
    dequeue(rear,front);
    display(rear,front);
    dequeue(rear,front);
    display(rear,front);
}