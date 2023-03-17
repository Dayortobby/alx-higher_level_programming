#ifndef PYTHON_H
#define PYTHON_H

#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/* Prints some basic information about a Python list */
void print_python_list(PyObject *p);

/* Prints some basic information about a Python bytes object */
void print_python_bytes(PyObject *p);

#endif /* PYTHON_H */
