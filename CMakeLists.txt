cmake_minimum_required( VERSION 3.0 )

project (degaussing_tests)

set(INCLUDES src/include )
include_directories(${INCLUDES})

add_executable( parser src/parser.cpp )
install( TARGETS parser 
		DESTINATION ${CMAKE_SOURCE_DIR}/execs )
