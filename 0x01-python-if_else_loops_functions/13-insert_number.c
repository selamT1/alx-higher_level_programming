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
	while (current->n < number)
	{
		prev = current;
		current = current->next;
	}
	new->n = number;
	prev ->next = new;
	new->next =current;

	return (new);
}
