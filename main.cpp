//integrating things

#include "main.h"

int main(int argc, char *argv[]) {
	if(argc < 2) {
		cerr << "simtype days country disease1 disease2 ... diseasen" << endl;
		cerr << "e.g. si_naive 500 usa h1n1" << endl;
		cerr << "reads constantfile, output to std output" << endl;
		return 1;
	}	

	int tottime;
	sscanf(argv[1],"%d",&tottime);
	pandemic p(argv[2]);	
	for(int i = 3; i < argc; i++) {
		p.adddis(argv[i]);
	}

	p.printhead();
	p.output();
	while(p.curtime < tottime) {
		p.iter();
		p.output();
	}
}
