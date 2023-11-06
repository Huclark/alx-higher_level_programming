#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *half2 = NULL;

	if (slow != NULL && slow->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			slow = slow->next;
		}
		if (fast != NULL)
			slow = slow->next;
		half2 = reverse_listint(&slow);
		while (half2 != NULL)
		{
			if ((*head)->n != half2->n)
				return (0);

			*head = (*head)->next;
			half2 = half2->next;
		}
	}
	return (0);
}


/**
 * reverse_listint - Reverses a singly linked list
 * @head: Pointer to the head of the linked list
 * Return: Pointer to the new head of the reversed linked list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL;

	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	*head = prev;
	return (*head);
}
