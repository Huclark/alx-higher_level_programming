#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new node or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *prev, *new;

	new = malloc(sizeof(listint_t)); /* allocate memory */

	if (!new) /* check for memory failure */
		return (NULL);
	
	/* initialize new node and point it to NULL */
	new->n = number; 
	new->next = NULL;

	/* check if */
	if (*head == NULL)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}

	new->next = current;
	prev->next = new;

	return (new);
}
