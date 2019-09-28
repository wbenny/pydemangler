# pydemangler

pydemangler is a **Python3** package for demangling MSVC & Itanium C++ symbols.
It is a tiny wrapper around [demumble](https://github.com/nico/demumble).

demumble is a project that extracts small portion of LLVM code that is responsible
for C++ symbol demangling.

### Why?

I couldn't find any existing Python library that could demangle symbols produced
by most recent MSVC.

### Installation

`pip install git+https://github.com/wbenny/pydemangler.git`

### Usage

pydemangler exports just single function `demangle()`.
It accepts only one argument (mangled string) and returns demangled name as a
string.  If the input string cannot be demangled, it returns `None`.

```
>>> import pydemangler
>>> pydemangler.demangle('?Fxi@@YAHP6AHH@Z@Z')
'int __cdecl Fxi(int (__cdecl *)(int))'
```

### FAQ

#### I use Python2, could you...

No

### License

This software is open-source under the Apache 2.0 license. See the LICENSE.txt file in this repository.
