CXXFLAGS = -std=gnu++17 -Wall -O2
CXXDEBUGFLAGS = -DEBUG

CXX = g++

all: sir sir_debug

sir: sir.cpp main.cpp
	$(CXX) -o sir sir.cpp main.cpp $(CXXFLAGS)

sir_debug: sir.cpp main.cpp
	$(CXX) -o sir_debug sir.cpp main.cpp $(CXXFLAGS) $(CXXDEBUGFLAGS)
