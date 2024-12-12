package fr.univtln.haouas.TPs;

public class Lapin  extends Mammifere implements IHerbivore{
    private String nbDents;

    public Lapin(String nom, String id,int gestation,String nbDents, int age) {
        super(nom, id, gestation, age);
        this.nbDents = nbDents;
    }

    @Override
    public void crier() {
        super.crier("Lapin");
    }

    @Override
    public String toString(){
        return super.toString() +" Lapin "+ " nbDents: " + nbDents;
    }

    public String getInfo(){
        return super.getInfo() + " Je suis un Lapin avec " + nbDents + " dents"+ " et mon nom est " + getNom();
    }

    @Override
    public String moyenExpression(){
        return " Je Clappit. Yacine est allégique aux lapins rip mon lappin albinos.";
    }

    @Override
    public void manger(Plante x) {
        System.out.println("Je grignotte " + x.getNom());
    }
}
