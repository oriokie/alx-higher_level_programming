#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info - function that prints a Python list info
 *
 * @p: PyObject representing the list
 * Return: none
 */
void print_python_list_info(PyObject *p)
{
	long int size, i; /* size stores the size of the list */
	PyListObject *list; /* represents a Python list */
	PyObject *item; /* stores individual items from the list */

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	/* checking if the 'p' is a valid python list */
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid list object\n");
		return;
	}

	/* converts the generic PyObject to a PyListObject */
	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	/**
	 * Looping through each element in the list
	 * Obtaining the individual items using PyList_GetItem
	 * and then printing each element
	 */
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
