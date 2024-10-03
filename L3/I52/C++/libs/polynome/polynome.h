#ifndef POLY_H
#define POLY_H
class Polynome
{
	private:
		int deg;
		float* coeff;
	public:
		Polynome();
		Polynome(const Polynome&);
		~Polynome();
		Polynome(int, float*);
		Polynome& operator=(const Polynome&);
		void Affic();

};
#endif
