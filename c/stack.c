/*
#Notes

# A Stack is a linear data structure in which elements can be inserted and
# deleted only from one side of the list, called the top.
# A stack follows the LIFO. (Last In First Out)
# Stack has a dynamic and fixed size.
# Stack remove remove from the top.

# STACK

#####
# 0 #    <------- TOP
#####
# 1 #
#####
# 2 #
#####
# 3 #
#####
*/

#include <stdio.h>
#include <stdbool.h>
#define STACKSIZE 200

int top = -1;
int stack[STACKSIZE];

int isEmpty()
{
    return top == -1 ? true : false;
}

void push(int item)
{
    if (top == STACKSIZE - 1)
    {
        printf("Stack overflow");
        return;
    }
    else
    {
        stack[top++] = item;

        printf("Pushed to stack\n");
    }
}

void pop()
{
    (top == -1) ? printf("Stack not have elements") : top--;
}

void print()
{
    printf("Stack: ");
    for (int i = 0; i <= top; i++)

        printf("%d ", stack[i]);
    printf("\n");
}

int main()
{
    printf("===^^===\n");
    printf("Stack data structure: \n");
    printf("\n");
    printf("Push function: \n");

    push(12);
    push(36);
    push(99);

    printf("\n");
    print();

    printf("\n");

    printf("===^^===\n");
    printf("Pop function: \n");

    printf("\n");
    pop();
    pop();

    print();

    return 0;
}
