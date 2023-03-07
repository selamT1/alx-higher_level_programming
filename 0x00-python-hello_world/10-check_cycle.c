#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	 listint_t *current = list;
	 listint_t *forward = list;

	if (list == NULL)
		return (0);
	while (current && forward && forward->next)
	{
		current = current->next;
		forward = forward->next->next;
		if (current == forward)
			return (1);
	}
	return (0);
}
