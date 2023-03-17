#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints some basic info about Python bytes objects
 *
 * @p: Pointer to a PyObject object
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes;
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    PyBytes_AsStringAndSize(p, &str, &size);
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    printf("  first %ld bytes: ", size < 10 ? size : 10);
    for (i = 0; i < size && i < 10; i++)
        printf("%02hhx%c", str[i], i == 9 ? '\n' : ' ');
}

/**
 * print_python_list - Prints some basic info about Python lists
 *
 * @p: Pointer to a PyObject object
 */
void print_python_list(PyObject *p)
{
    PyListObject *list;
    Py_ssize_t size, i;
    PyObject *element;

    printf("[*] Python list info\n");

    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    list = (PyListObject *)p;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        element = PyList_GET_ITEM(p, i);
        printf("Element %ld: ", i);
        if (PyBytes_Check(element))
            print_python_bytes(element);
        else
            printf("%s\n", Py_TYPE(element)->tp_name);
    }
}
