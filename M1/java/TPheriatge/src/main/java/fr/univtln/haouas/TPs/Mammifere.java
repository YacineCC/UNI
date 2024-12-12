package fr.univtln.haouas.TPs;

public abstract class Mammifere extends Animal {

    private int gestation;

    public Mammifere(String nom, String id,int gestation, int age) {
        super(nom, id, age);
        this.gestation = gestation;
    }

    public Mammifere()
    {
        super();
        this.gestation = 0;
    }

    @Override
    public void crier(String espece){
        System.out.println("Je suis un mammifère de l'espèce " + espece + " et je crie !");
    }

    @Override
    public String toString(){
        return super.toString() + " Mammifère "+ " gestation: " + gestation;
    }

    public String getInfo(){
        if (gestation == 0)
            return super.getInfo() + " Je suis un Mammifère ";
        else
            return super.getInfo() + " Je suis un Mammifère avec une gestation de " + gestation;
    }

    @Override
    public String moyenExpression(){
        return "Maaaaaamifeeerree";
    }
}
