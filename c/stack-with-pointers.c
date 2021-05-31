#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#define STACKSIZE 6000
#define SIZE 256

//char item[SIZE];

struct stack
{
    int top;
    int items[STACKSIZE];
};

struct stack s;

int isEmpty(struct stack *pStack)
{
    return pStack->top == -1 ? true : false;
}

int pop(struct stack *pStack)
{
    if (isEmpty(pStack))
    {
        printf("Stack empty");
        exit(1);
    }
    else
    {
        printf("Poped from the stack\n");
        return (pStack->items[pStack->top--]);
    }
}

void push(struct stack *pStack, int item)
{
    if (pStack->top == STACKSIZE - 1)
    {
        printf("Stack overflow");
        exit(1);
    }
    else
    {
        pStack->items[++(pStack->top)] = item;
        printf("Pushed to stack\n");
    }

    return;
}

int main()
{
    printf("===^^===\n");
    printf("Stack data structure: \n");
    printf("\n");
    printf("Push function: \n");

    push(&s, 1);
    push(&s, 2);
    push(&s, 3);
    push(&s, 4);

    printf("%x <---- stack size ", s.top);
    printf("\n");

    printf("\n");

    printf("===^^===\n");
    printf("Pop function: \n");

    pop(&s);

    printf("%x <---- stack size", s.top);

    return 0;
}