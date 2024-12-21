cmake_minimum_required(VERSION 3.15)
project(hypertext VERSION 0.1.0 LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Options
option(BUILD_TESTS "Build test suite" ON)
option(BUILD_DOCS "Build documentation" ON)

# Main compiler executable
add_executable(ht
    src/compiler/main.cpp
    src/compiler/lexer.cpp
    src/compiler/parser.cpp
    src/compiler/codegen.cpp
)

# Standard library
add_library(htlib SHARED
    src/stdlib/core.cpp
    src/stdlib/web.cpp
    src/stdlib/io.cpp
)

# Installation rules
install(TARGETS ht DESTINATION bin)
install(TARGETS htlib DESTINATION lib)
install(DIRECTORY include/hypertext DESTINATION include)

# Testing
if(BUILD_TESTS)
    enable_testing()
    add_subdirectory(tests)
endif()

# Documentation
if(BUILD_DOCS)
    find_package(Doxygen)
    if(DOXYGEN_FOUND)
        configure_file(${CMAKE_SOURCE_DIR}/docs/Doxyfile.in
                     ${CMAKE_BINARY_DIR}/Doxyfile @ONLY)
        add_custom_target(docs
            ${DOXYGEN_EXECUTABLE} ${CMAKE_BINARY_DIR}/Doxyfile
            WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
            COMMENT "Generating API documentation with Doxygen"
        )
    endif()
endif()
