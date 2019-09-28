cmake_minimum_required(VERSION 3.12 FATAL_ERROR)
project(pydemangler CXX)

if (UNIX)
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -fno-exceptions -fno-rtti")
	if (${CMAKE_GENERATOR} STREQUAL "Ninja")
		set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fdiagnostics-color")
	endif()

	# 10.9 chosen somewhat arbitrary; it's the first target where clang defaults
	# to libc++ and ld64 defaults to stripping __TEXT,__eh_frame.
	if (APPLE)
		set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -mmacosx-version-min=10.9")
	else()
		set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fno-PIC")
		set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -no-pie")
	endif()
endif()

if (WIN32)
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /Zc:inline /wd4244")
	add_definitions(-D_CRT_SECURE_NO_WARNINGS) # The LLVM build sets this.

	# This is apparently the simplest way to statically link the CRT in CMake:
	string(TOUPPER "${CMAKE_BUILD_TYPE}" build)
	set(flag_var "CMAKE_CXX_FLAGS_${build}")
	if(${flag_var} MATCHES "/MD")
		string(REGEX REPLACE "/MD" "/MT" ${flag_var} "${${flag_var}}")
	endif()
endif()

find_package (Python3 COMPONENTS Interpreter Development)

if (NOT Python3_Development_FOUND)
	message(FATAL_ERROR "Python3 include directory not found!")
endif()

include_directories(demumble/third_party/llvm/include)

Python3_add_library(pydemangler MODULE
                    pydemangler.cc
                    demumble/third_party/llvm/lib/Demangle/ItaniumDemangle.cpp
                    demumble/third_party/llvm/lib/Demangle/MicrosoftDemangle.cpp
                    demumble/third_party/llvm/lib/Demangle/MicrosoftDemangleNodes.cpp)
