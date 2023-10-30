#ifndef LISTS_H
#define LISTS_H

/* Standard library headers */
#include <stdio.h>

/**
 * struct listint_t - Singly linked list
 * @n: Integer stored in the node
 * @next: Pointer to the next node
*/
typedef struct listint_t
{
	int n;
	struct listint_t *next;
} listint_t;

/* Custom prototypes */
int check_Cycle(listint_t *list);

#endif
