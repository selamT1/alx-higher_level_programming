#include "lists.h"
/*
 * insert_node - insert node in the sorted order
 * @numbeer: value of a newly added node
 * Return: new node address if succeded or NULL if fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *prev;
	listint_t *new;

	if (*head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if(new == NULL)
		return (NULL);
	if (current->n > number)
	{
		new->n = number;
		*head = new;
		(*head)->next = current;
	}
	else
	{
		while (current->n < number && current->next != NULL)
		{
			prev = current;
			current = current->next;
		}
		if (current->next == NULL)
		{
		new->n = number;
		current->next = new;
		new->next =NULL;
		}
		else
		{
			new->n = number;
			prev->next = new;
			new->next = current;
		}
	}
	return (new);
}
