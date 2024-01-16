/*1s' and 2s's Complement*/
#include<bits/stdc++.h>
using namespace std;
class Node
{
    public:
    Node* next;
    Node* prev;
    bool val;
    Node()
    {
        next=NULL;
        prev=NULL;
    }
    Node(bool data){
        next=NULL;
        prev=NULL;
        val=data;
    }
};
void getbinary(Node* &head,Node* &tail,bool data)
{
    Node* ptr=new Node(data);
    if(head==NULL){
        head=ptr;
        tail=ptr;
    }
    else
    {
        tail->next=ptr;
        ptr->prev=tail;
        tail=ptr;
       /*  Node* temp=head;
        while(temp->next!=NULL)
        {
            temp=temp->next;
        }
        temp->next=ptr;
        ptr->prev=temp;
        temp=ptr; */
    }
}
void display(Node* &head)
{
    cout<<"The binary number is:"<<endl;
    Node* temp=head;
        while(temp!=NULL)
        {
            cout<<temp->val;
            temp=temp->next;   
        }
        cout<<endl;
}
void OnesComplement(Node* &head)
{
    Node* temp=head;
    cout<<"After 1's Complement:"<<endl;
    while(temp!=NULL)
    {
        cout<<!temp->val;
        temp=temp->next;
    }
    cout<<endl;
}
void TwosComplement(Node* &tail,int n)
{
    bool twos[15];
    Node* temp=tail;
    int i=-1;
    while(temp!=NULL and temp->val==0)
    {
        twos[++i]=0;
        temp=temp->prev;
    }
    twos[++i]=1;
    temp=temp->prev;
    while(temp!=NULL)
    {
        twos[++i]=!(temp->val);
        temp=temp->prev;
    }
    cout<<"Twos Complement: ";
    while(i>=0){
    cout<<twos[i];
    i-=1;}
    cout<<endl;
}

int main()
{
    Node* head=NULL;
    Node* tail=NULL;
    int n;
    cout<<"Enter length of Binary Number:";
    cin>>n;
    int n1=n;
    while(n1>0)
    {
        bool x;
        cout<<"Enter binary element:";
        cin>>x;
        getbinary(head,tail,x);
        n1--;
    }
    display(head);

    OnesComplement(head);
    TwosComplement(tail,n);
    return 0;
}