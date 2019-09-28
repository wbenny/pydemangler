#!/usr/bin/env python

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext


class BuildExt(build_ext):
	"""A custom build extension for adding compiler-specific options."""

	def run(self):
		if self.plat_name in ('win32','win-amd64'):
			pydemangler_ext.define_macros.append(('_CRT_SECURE_NO_WARNINGS', '1'))
			pydemangler_ext.extra_compile_args.append('/wd4244')
		elif 'macosx' in self.plat_name:
			pydemangler_ext.extra_compile_args.append('-mmacosx-version-min=10.9')

		build_ext.run(self)


pydemangler_ext = Extension(
	'pydemangler', [
		'pydemangler.cc',
		'demumble/third_party/llvm/lib/Demangle/ItaniumDemangle.cpp',
		'demumble/third_party/llvm/lib/Demangle/MicrosoftDemangle.cpp',
		'demumble/third_party/llvm/lib/Demangle/MicrosoftDemangleNodes.cpp',
	],
	include_dirs=[ 'demumble/third_party/llvm/include' ]
)

setup(
	name='pydemangler',
	version='0.1',
	description='Python C++ demangler',
	author='Petr Benes',
	author_email='w.benny@outlook.com',
	url='https://github.com/wbenny/pydemangler',
	ext_modules=[ pydemangler_ext ],
	cmdclass={ 'build_ext': BuildExt }
)
