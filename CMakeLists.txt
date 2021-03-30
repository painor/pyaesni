cmake_minimum_required(VERSION 3.14.7 FATAL_ERROR)
project(pyaesni C)
set(CMAKE_C_STANDARD 99)
set(CMAKE_C_STANDARD_REQUIRED ON)

add_subdirectory(libaesni)

find_package(Python "${PYTHON_VERSION}" EXACT COMPONENTS Development REQUIRED)

include(GNUInstallDirs)

add_library(pyaesni SHARED pyaesni.c)

get_target_property(aesni_includes libaesni INCLUDE_DIRECTORIES)
target_include_directories(pyaesni PRIVATE ${aesni_includes})

target_link_libraries(pyaesni PRIVATE
        Python::Python
        $<TARGET_OBJECTS:libaesni_asm>
        $<TARGET_OBJECTS:libaesni>
        )

set_target_properties(pyaesni PROPERTIES SUFFIX ".pyd" PREFIX "")

add_dependencies(pyaesni libaesni)

install(TARGETS pyaesni RUNTIME DESTINATION ${CMAKE_INSTALL_LIBDIR})
