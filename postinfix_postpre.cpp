#include<bits/stdc++.h>
using namespace std;

bool isOperator(char c)
{
    if(c=='+' or c=='-' or c=='/' or c=='*')
    return true;
    else
    return false;
}

string postfixtoinfix(string expression)
{
    stack<string> s;
    for(char& c: expression)
    {
        if(!isOperator(c))
        {
            string operand(1,c);
            s.push(operand);
        }
        else
        {
            string op2=s.top();
            s.pop();
            string op1=s.top();
            s.pop();

            string infix="("+op1+c+op2+")";
            s.push(infix);     
        }
    }
    return s.top();
}

string postfixtoprefix(string expression)
{
    stack<string> s;
    for(char& c: expression)
    {
        if(!isOperator(c))
        {
            string operand(1,c);
            s.push(operand);
        }
        else{
            string op2=s.top();
            s.pop();
            string op1=s.top();
            s.pop();
            string prefix=c+op1+op2;
            s.push(prefix);
        }
    }
    return s.top();
}
int main() {
    string postfixExp = "ab+cd+ef*-/"; // Replace this with your postfix expression
    string infixExp = postfixtoinfix(postfixExp);
    cout << "Postfix Expression: " << postfixExp <<endl;
    cout << "Infix Expression: " << infixExp <<endl;
    cout<<"Prefix Expression: "<<postfixtoprefix(postfixExp)<<endl;
    return 0;
}
