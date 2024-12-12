package fr.univtln.haouas.TPs;

public class Chien  extends Mammifere implements ICarnivore{
    private String collier;

    public Chien(String nom, String id,int gestation,String collier, int age) {
        super(nom, id, gestation, age);
        this.collier = collier;
    }

    @Override
    public void crier() {
        super.crier("Chien");
    }

    @Override
    public String toString(){
        return super.toString() + " Chien "+" collier: " + collier;
    }

    @Override
    public String getInfo(){
        if (collier == null)
            return super.getInfo() + " Je suis un Chien ";
        else
            return super.getInfo() + " Je suis un Chien avec un collier " + collier+ " et mon nom est " + getNom();
    }

    @Override
    public String moyenExpression(){
        return super.moyenExpression() + " Wouf Wouf";
    }

    @Override
    public void manger(Animal x) {
        System.out.println("Je mords " + x.getNom());
    }
}
