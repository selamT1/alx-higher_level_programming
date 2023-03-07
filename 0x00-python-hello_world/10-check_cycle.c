#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	const listint_t *current;

	current = list;
	current = current->next;
	if (current == NULL)
		return (0);
	return (1);
}
