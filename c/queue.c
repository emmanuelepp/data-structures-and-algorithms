/*
# Notes

# A Queue is a linear structure that follows a particular order in
# which the operations are performed.
# The order is FIFO.(First In First Out)
# The difference between stacks and queues is in removing.
# Stack remove remove from the top and the queue remove the itemmore recent.

               # Rear                # Front
               #|                    #|
               #|                    #|
               #v       # Queue      #v
#Enqueue        ##### ##### ##### #####
# ------>       # 0 # # 1 # # 2 # # 3 #  ------> Dequeue
                ##### ##### ##### #####
*/

#include <stdio.h>
#include <stdbool.h>
#define QUEUESIZE 200

int queue[QUEUESIZE];
int front = -1;
int rear;

bool isEmpty()
{
    return (front == rear) ? true : false;
}

int enqueue(int item)
{
    if (rear == QUEUESIZE - 1)
    {
        rear = 0;
    }
    else
    {
        queue[rear++] = item;
    }

    printf("Pushed to queue\n");

    return 0;
}

void dequeue()
{
    (isEmpty() == false) ? queue[front--] : printf("Queue is empty");
    printf("Delete from the queue\n");
}

void print()
{
    printf("Queue: ");
    for (int i = 0; i <= rear; i++)

        printf("%d ", queue[i]);
    printf("\n");
}

int main(int argc, char const *argv[])
{

    printf("===^^===\n");
    printf("Stack data structure: \n");
    printf("\n");
    printf("Enqueue function: \n");

    enqueue(22);
    enqueue(37);
    enqueue(89);
    printf("\n");
    print();
    printf("\n");

    printf("===^^===\n");
    printf("Dequeue function: \n");

    printf("\n");
    dequeue();
    print();
    printf("\n");

    return 0;
}
