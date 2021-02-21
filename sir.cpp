//an euler-method numerical approximation of an sir-model for viral pandemics

#include "main.h"

long double disease::iter(long double newinf) {
	this->dailyinf = newinf;
	long double ded = (this->data->u+this->data->v)*this->infected;
	long double ret = this->infected * (1-(this->data->u + this->data->v))/(this->data->il);
	this->infected += newinf;
	this->infected -= ded;
	this->dead += ded;
	this->recovered += ret;
	this->infected -= ret;
	ded += this->recovered * this->data->u;
	this->recovered -= this->recovered * this->data->u;
	return ded;
}

void disease::printhead() {
	cout << ",daily " << name << " infected,total " << name << " infected," << name << " recovered";
}

void disease::output() {
	cout << "," << (int) this->dailyinf << "," << (int) this->infected << "," << (int) this->recovered;
}

void pandemic::iter() {
	this->curtime++;
	this->population += this->birthrate-this->deathrate*this->uninfected;
	long double totinfected = 0.0;
	long double totdead = 0.0;
	for(auto &dis : this->ongoing) {
		if(dis->data->starttime == this->curtime) {dis->infected = dis->data->startinf;}
		if(dis->data->starttime <= this->curtime) {
			totinfected += this->uninfected * (dis->infected) * ((dis->data)->b);
			totdead += dis->iter(this->uninfected*(dis->infected)*((dis->data)->b));
		}
		else {
			totdead += dis->iter(0.0);
		}
	}
	this->uninfected += this->birthrate-this->deathrate*this->uninfected;
	this->population -= totdead;
	this->uninfected -= totinfected;
}

void pandemic::printhead() {
	cout << "date,";
	if(DEBUG) cout << "uninfected,";
	cout << "total infected,total daily infections,total recovered";
	for(auto &dis : this->ongoing) {dis->printhead();}
	std::cout << std::endl;
}

void pandemic::output() {
	cout << this->curtime << ",";
	if(DEBUG) cout << (int) this->uninfected << ",";
	cout << (int) this->infected() << "," << (int) this->totdailyinf() << "," << (int) this->totrec();
	for(auto &dis : this->ongoing) {dis->output();}
	std::cout << std::endl;
}
