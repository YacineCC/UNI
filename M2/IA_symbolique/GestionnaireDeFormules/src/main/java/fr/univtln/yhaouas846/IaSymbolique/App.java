package fr.univtln.yhaouas846.IaSymbolique;

/**
 * Hello world!
 */
public class App {
    public static void main(String[] args) {
        System.out.println("Hello World!");
        Var a = new Var("A", new Interpretation(Boolean.TRUE));
        Var b = new Var("B", new Interpretation(Boolean.FALSE));
        Var c = new Var("C", new Interpretation(Boolean.FALSE));
        Var d = new Var("D", new Interpretation(Boolean.TRUE));
        Var e = new Var("E", new Interpretation(Boolean.TRUE));

        VariableSet testSet = new VariableSet(null);
        testSet.addVar(a);
        testSet.addVar(b);
        testSet.addVar(c);
        testSet.addVar(d);
        testSet.addVar(e);
        testSet.addVar(a);
        testSet.addVar(e);

        System.out.println(testSet);

        Formula f = new Formula(new Formula(a), Formula.Connector.AND, new Formula(b));


    }
}
