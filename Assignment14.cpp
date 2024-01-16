/*Priority Queue*/
#include<bits/stdc++.h>
using namespace std;

template<typename T>
class Node
{
    public:
    Node* next;
    T data;
    int priority;
    Node()
    {
        next=NULL;
    }
    Node(T data, int priority)
    {
        this->data=data;
        this->priority=priority;
        next=NULL;
    }
};
template<typename T>
class PriorityQueue
{
    private:
    Node<T>* head;

    public:
    PriorityQueue()
    {
        head=NULL;
    }

    void enqueue(T item,int priority)
    {
        Node<T>* t=new Node<T>(item,priority);
        if(head==NULL or priority>head->priority)
        {
            t->next=head;
            head=t;
        }
        else
        {
            Node<T>* temp=head;
            while(temp->next!=NULL and temp->next->priority>=priority)
            {
                temp=temp->next;
            }
            t->next=temp->next;
            temp->next=t;
        }
    }

    void dequeue()
    {
        if(head==NULL)
        {
            cout<<"Empty!!!"<<endl;
        }
        else
        {
            T data1=head->data;
            Node<T>* temp=head;
            head=head->next;
            delete(temp);
            cout<<data1<<" is removed"<<endl;
        }
    }

    void display()
    {
        if(head==NULL)
        {
            cout<<"Empty!!!"<<endl;
        }
        else
        {
            cout<<"Displaying: "<<endl;
            Node<T>* temp=head;
            while(temp!=NULL)
            {
                cout<<"Data= "<<temp->data<<", Priority= "<<temp->priority<<endl;
                temp=temp->next;
            }
        }
    }
};
int main()
{
  PriorityQueue<int> p;
  p.enqueue(30,2);
  p.enqueue(31,1);
  p.enqueue(32,3);
  p.enqueue(33,4);
  p.display();
  p.dequeue();
  p.display();
return 0;
}