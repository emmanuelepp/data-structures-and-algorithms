#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define QUEUESIZE 200

struct queue
{
    int items[QUEUESIZE];
    int tail, head;
};

struct queue q;

bool isEmpty(struct queue *pQueue)
{
    return (pQueue->head == pQueue->tail) ? true : false;
}

void enqueue(struct queue *pQueue, int item)
{
    (pQueue->tail == QUEUESIZE - 1) ? pQueue->tail = 0 : pQueue->tail++;

    if (pQueue->tail == pQueue->head)
    {
        printf("Overflow");
        exit(1);
    }

    pQueue->items[pQueue->tail] = item;
}

int dequeue(struct queue *pQueue)
{
    if (isEmpty(pQueue))
    {
        printf("Underfolow\n");
        exit(1);
    }

    (pQueue->head == QUEUESIZE - 1) ? pQueue->head = 0 : pQueue->head++;

    return (pQueue->items[pQueue->head]);
}

void print()
{
    printf("Queue: ");
    for (int i = q.head; i < q.tail; i++)

        printf("%d ", q.items[i]);
    printf("\n");
}

int main()
{

    printf("===^^===\n");
    printf("Stack data structure: \n");
    printf("\n");
    printf("Enqueue function: \n");

    enqueue(&q, 22);
    enqueue(&q, 26);
    enqueue(&q, 89);
    enqueue(&q, 64);
    enqueue(&q, 73);
    print();
    printf("\n");

    printf("\n");

    printf("\n");

    printf("===^^===\n");
    printf("Dequeue function: \n");

    printf("\n");
    dequeue(&q.items[0]);
    dequeue(&q.items[0]);
    dequeue(&q.items[0]);
    print();

    printf("\n");

    return 0;
}
