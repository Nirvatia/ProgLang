main.exe: message.o hello.o goodbye.o main.o
	g++ -o main.exe message.o hello.o goodbye.o main.o

message.o: message.cpp message.h
	g++ -c message.cpp

hello.o: hello.cpp hello.h message.h
	g++ -c hello.cpp

goodbye.o: goodbye.cpp goodbye.h message.h
	g++ -c goodbye.cpp

main.o: main.cpp hello.h goodbye.h
	g++ -c main.cpp

