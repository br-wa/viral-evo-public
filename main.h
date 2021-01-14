//integrating header

#include<fstream>
#include<iostream>
#include<string>
#include<sstream>
#include<vector>

using namespace std;

#define LOOKUP "temp/"

#ifdef DEBUG
#define LOOKUP "constants/"
#endif

#ifndef DEBUG
#define DEBUG false
#endif

struct params {
public:
	int starttime;
	long double b; //infectivity
	long double u; //death rate
	long double v; //increased death rate from infection (aka virulence)
	long double il; //infection length
	long double startinf;

	params(string filename, long double deathrate): starttime(0), u(deathrate) {
		ifstream inf((string) LOOKUP + "disease/" + filename);
		string line;
		string datatype;
		il = -1;
		while(getline(inf,line)) {
			stringstream ss(line);
			ss >> datatype;
			if(datatype[0] == 'd') {ss >> this->u;}
			if(datatype[0] == 'v') {ss >> this->v;}
			if(datatype[0] == 's') {ss >> this->il;}
			if(datatype[0] == 'i') {ss >> this->b;}
			if(datatype[0] == 'a') {ss >> this->starttime;}
			if(datatype[0] == 'h') {ss >> this->startinf;}
		}
		if(il < 0) {il = 1/(u+v);}
		inf.close();
	}
};

struct disease {
public:
	string name;
	params* data;
	long double infected;
	long double dailyinf;
	long double r0;
	long double recovered;
	long double dead;
	void computer0(long double birthrate) {
		r0 = data->b * birthrate * data->il / data->u;
	}

	disease(string filename, long double birthrate, long double deathrate): name(filename), data(new params(filename, deathrate)), infected(0.0), dailyinf(0.0), recovered(0.0){
		computer0(birthrate);	
		if(data->starttime <= 0) {infected = data->startinf;}
	}

	long double iter(long double newinf);
	void printhead();
	void output();
};

struct pandemic {
public:
	int curtime;
	long double deathrate;
	long double population;
	long double uninfected;
	long double birthrate;
	vector<disease*> ongoing;

	void iter();
	void printhead();
	void output();
	void readprot();

	long double infected() {
		long double totdead = 0.0;
		for (auto &dis : ongoing) {totdead += dis->infected;}
		return totdead;
	}
	long double totrec() {
		long double rec = 0.0;
		for(auto &dis : ongoing) {rec += dis->recovered;}
		return rec;
	}
	long double totdailyinf() {
		long double ret = 0.0;
		for(auto &dis : ongoing) {ret += dis->dailyinf;}
		return ret;
	}

	void adddis(string filename) {
		disease* newdis = new disease(filename,birthrate,deathrate);
		uninfected -= newdis->infected;
		ongoing.push_back(newdis);
	}

	pandemic(string filename): curtime(0) {
		ifstream inf((string) LOOKUP + "region/" + filename);
		string line;
		string datatype;
		while(getline(inf,line)) {
			stringstream ss(line);
			ss >> datatype;
			if(datatype[0] == 'i') {ss >> this->population; this->uninfected = population;}
			if(datatype[0] == 'b') {ss >> this->birthrate;}
			if(datatype[0] == 'd') {ss >> this->deathrate;}
		}
		inf.close();
	}
};

int main(int argc, char *argv[]);
