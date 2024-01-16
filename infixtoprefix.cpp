#include <bits/stdc++.h>
using namespace std;
int Precedence(char c)
{
    if(c=='^')    return 3;
    else if(c=='/' || c=='*')   return 2;
    else if(c=='-' || c=='+')  return 1;
    else    return -1; 
}
string Infix_To_Prefix(string s1)
{
    reverse(s1.begin(), s1.end());
    for(int i=0; i<s1.size(); i++)
    {
        if(s1[i]=='(')
        {
            s1[i] = ')';
        }  
        else if(s1[i]==')')
        {
            s1[i] = '(';
        }  
    }

    stack<char> st;
    string result="";

    for(int i=0; i<s1.size(); i++)
    {
        if((s1[i]>='a' && s1[i]<='z') || (s1[i]>='A' && s1[i]<='Z') || s1[i]>='0' && s1[i]<='9')
        {
            result += s1[i];
        }
        else if(s1[i] == '(')
        {
            st.push(s1[i]);
        }
        else if(s1[i] == ')')
        {
            while(st.top() != '(')
            {
                result += st.top();
                st.pop();
            }
            st.pop();
        }
        else
        {
            while(!st.empty() && (Precedence(st.top())>=Precedence(s1[i])))
            {
                result += st.top();
                st.pop();
            }
            st.push(s1[i]);
        }
    }
    while(!st.empty())
    {
        result += st.top();
        st.pop();
    }
    reverse(result.begin(), result.end());
    return result;
}
bool Balanced_Paranthesis(string s1)
{
	stack<char> st;
    bool flag = false;
	for(int i=0; i<s1.size(); i++) 
    {
        if(s1[i]!=')' || s1[i]!='(')
        {
            continue;
        }
		else if(st.empty())
        {
			st.push(s1[i]);
		}
		else if((st.top()=='(' && s1[i]==')')) 
        {
			st.pop();
		}
		else 
        {
			st.push(s1[i]);
		}
	}
	if(st.empty())  flag = true;
    return flag;
}
int main()
{
    cout << "*----------Menu----------*" << endl;
    cout << "0. Quit" << endl;
    cout << "1. To check weather the Infix expression is well balanced or not." << endl;
    cout << "2. To convert Infix to Prefix expression." << endl;
    cout << endl;

    while(true)
    {
        cout << "Enter your choice : ";
        int choice;
        cin >> choice;

        if(choice==0)
        {
            cout << "Quit." << endl;
            break;
        }
        else if(choice==1)
        {
            cout << "Enter the Infix expression :";
            string s1;
            cin >> s1;
            if(Balanced_Paranthesis(s1))
            {
                cout << "The Expression is a balanced expression." << endl;
            }
            else
            {
                cout << "The Expression is not a balanced expression." << endl;
            }
        }
        else if(choice==2)
        {
            cout << "Enter the Infix expression :";
            string s1;
            cin >> s1;
            string prefix = Infix_To_Prefix(s1);
            cout << "The Prefix expression for the Infix expression is: " << prefix << endl;
        }
        cout << endl;
    }
}