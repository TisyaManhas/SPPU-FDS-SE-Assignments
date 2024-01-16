/*
A double-ended queue (deque) is a linear list in which additions and deletions may be
made at either end. Obtain a data representation mapping a deque into a one- dimensional 
array. Write C++ program to simulate deque with functions to add and
delete elements from either end of the deque.
*/

#include <bits/stdc++.h>
using namespace std;
class Node
{
    public:
    int data;
    Node *prev;
    Node *next;

    Node(int x)
    {
        this->data=x;
        this->prev = NULL;
        this->next = NULL;
    }
};
void addfront(Node* &head,Node* &tail,int x)
{
    Node* ptr=new Node(x);
    if(head==NULL)
    {
        head=ptr;
        tail=ptr;
        return;
    }
    else
    {
        ptr->next=head;
        head->prev=ptr;
        head=ptr;
    }
}
void addlast(Node* &head,Node* &tail,int x)
{
    Node* ptr=new Node(x);
    if(head==NULL)
    {
        head=ptr;
        tail=ptr;
        return;
    }
    else
    {
        tail->next=ptr;
        ptr->prev=tail;
        tail=ptr;
    }
}
void removefront(Node* &head)
{
   Node* ptr=head;
    if(head==NULL)
    {
        cout<<"Empty queue!!!"<<endl;
    } 
    else
    {
        cout<<"Removing "<<ptr->data<<endl;
        head=head->next;
        head->prev=NULL;
        ptr->next=NULL;
        delete(ptr);
    }
}
void removelast(Node* &head,Node* &tail)
{
    if(head==NULL)
    {
    cout<<"Empty queue!!!"<<endl;
    }
    else
    {
        Node* ptr=tail;
        cout<<"Removing "<<ptr->data<<endl;
        tail=tail->prev;
        tail->next=NULL;
        delete(ptr);
       /*  ptr->next=tail->next;
        tail->prev=NULL;
        tail->next=NULL;
        delete(ptr->next)  
        tail=tail->next;  */
    }
}
void displaying(Node* &head)
{
    Node* ptr=head;
    while(ptr!=NULL)
    {
        cout<<ptr->data<<" ";
        ptr=ptr->next;
    }
    cout<<endl;
}
int main()
{
    Node *head=NULL;
    Node* tail=NULL;
    addfront(head,tail,4);
    addfront(head,tail,3);
    addfront(head,tail,2);
    addfront(head,tail,1);
    displaying(head);
    addlast(head,tail,6);
    displaying(head);
    removefront(head);
    displaying(head);
    removelast(head,tail);
    displaying(head);
    return 0;
}