#include <stdio.h>
#include <Python.h>

double sum(double a, double b){
    return a + b;
}


static PyObject* sum_int(PyObject *self, PyObject *args) {
    int a, b;
     if (PyTuple_Size(args) != 2) {
        PyErr_SetString(self, "func_ret_str args error");
    }

    PyArg_ParseTuple(args, "ii", &a, &b); // ii - (int - int)

    return Py_BuildValue("i",sum(a,b));
}


static PyObject* scalar_product(PyObject *self, PyObject *args)
 {
    PyObject *pList;
    PyObject *pItem;
    Py_ssize_t n;
    double item;
    if (!PyArg_ParseTuple(args, "O!", &PyList_Type, &pList))
    {
        PyErr_SetString(PyExc_TypeError, "parameter must be a list.");
        return NULL;
    }
    n = PyList_Size(pList);
    PyObject* new_array = PyList_New(n);
    for(int i = 0; i < n; i++)
    {
        pItem = PyList_GetItem(pList, i);
        item = PyFloat_AsDouble(pItem);
        PyObject*  value_ = Py_BuildValue("d", sum(item, item));
        PyList_SetItem(new_array, i, value_);
    }
    return new_array;

}



static PyMethodDef methods[] = { 
    {    
        "sum", sum_int, METH_VARARGS,   // Название функции в питоне, Функция в СИ, ЕСТЬ/НЕТ аргументов
        "Print 'hello world' from a method defined in a C extension."
    },  
    {
        "dot",scalar_product,METH_VARARGS,
        "hz"
    },

    {NULL, NULL, 0, NULL}
};

// Module definition
// The arguments of this structure tell Python what to call your extension,
// what it's methods are and where to look for it's method definitions
static struct PyModuleDef hello_definition = { 
    PyModuleDef_HEAD_INIT,
    "linsum",
    "A Python module that prints 'hello world' from C code.",
    -1, 
    methods
};


//Важно PyInit_НазваниеЛибы
PyMODINIT_FUNC PyInit_linsum(void) {
    Py_Initialize();
    return PyModule_Create(&hello_definition);
}