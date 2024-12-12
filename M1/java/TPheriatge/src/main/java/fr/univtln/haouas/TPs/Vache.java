package fr.univtln.haouas.TPs;

public class Vache extends Mammifere implements IHerbivore{
    private String couleur;

    public Vache(String nom, String id, int gestation, String couleur, int age) {
        super(nom, id, gestation, age);
        this.couleur = couleur;
    }

    @Override
    public void crier() {
        super.crier("Vache");
    }

    @Override
    public String toString(){
        return super.toString() +" Vache "+ "couleur: " + couleur;
    }

    public String getInfo() {
        return super.getInfo() + " Je suis une Vache de couleur " + couleur;
    }

    @Override
    public String moyenExpression(){
        return super.moyenExpression() + " Meuh Meuh";
    }

    @Override
    public void manger(Plante x) {
        System.out.println("Je broute " + x.getNom());
    }
}
