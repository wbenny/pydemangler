#include <Python.h>

#include "llvm/Demangle/Demangle.h"

static
PyObject*
pydemangler_demangle(
	PyObject* self,
	PyObject* args
	)
{
	(void)(self);

	const char* input;

	if (!PyArg_Parse(args, "s", &input))
	{
		Py_RETURN_NONE;
	}

	if (char* output = llvm::itaniumDemangle(input, NULL, NULL, NULL)) {
		PyObject* result = Py_BuildValue("s", output);
		free(output);
		return result;
	}
	else if (char* output = llvm::microsoftDemangle(input, NULL, NULL, NULL)) {
		PyObject* result = Py_BuildValue("s", output);
		free(output);
		return result;
	}

	Py_RETURN_NONE;
}

static PyMethodDef pydemangler_methods[] = {
	{ "demangle", (PyCFunction)pydemangler_demangle, METH_O, nullptr },
	{ nullptr, nullptr, 0, nullptr }
};

static PyModuleDef pydemangler_module = {
	PyModuleDef_HEAD_INIT,
	"pydemangler",           // Module name to use with Python import statements
	"Python C++ demangler",  // Module description
	0,
	pydemangler_methods      // Structure that defines the methods of the module
};

PyMODINIT_FUNC
PyInit_pydemangler()
{
	return PyModule_Create(&pydemangler_module);
}
