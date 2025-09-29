package fr.univtln.yhaouas846.IaSymbolique;

// Utilisation d'une IA Génrative (ChatGPT) pour ce TP
//

import java.util.HashMap;
import java.util.Map;

import static fr.univtln.yhaouas846.IaSymbolique.F.*;

public class Main {
    public static void main(String[] args){
        // 1. Création programmatique de la formule
        Formula a = var("a");
        Formula b = var("b");
        Formula c = var("c");
        Formula d = var("d");
        Formula e = var("e");


        Formula and = and(a, b);

        System.out.println("a && b : " + and);
        System.out.println("Vars: " + and.vars());

        Map base = new HashMap<Formula, Boolean>();
        base.put(a, true);
        base.put(b, false);
        base.put(c, false);
        base.put(d, true);
        base.put(e, true);


        Interpretation interp = new Interpretation(base);
        System.out.println(interp);
        System.out.println(and.toString() + " : " + and.value(interp));

        Formula nonA = not(a);
        System.out.println(nonA.toString() + nonA.value(interp));

        Formula f = equiv(and(or(not(a), b), imp(c, d)), or(a,d));
        //System.out.println(and.value(interp));



        //Formula f = equiv(
        //        and(or(not(var("a")), var("b")),imp(var("c"), var("d"))), or(var("a"), var("d")));

        System.out.println("F: " + f);
        System.out.println("Vars: " + f.vars());

        VariableSet test = new VariableSet(f);
        System.out.println(test.getInterpretations());


        // 3. Formes normales
        //System.out.println("\nNNF: " + f.toNormalForm());
        //System.out.println("CNF: " + f.toCNF());
        //System.out.println("DNF: " + f.toDNF());

        // -------------------------------
        // 3.1. Sortie HTML
        // -------------------------------
        //System.out.println("\nAffichage HTML :");
        //System.out.println(f.toHtml());

        // -------------------------------
        // 3.2. Lecture depuis LaTeX
        // -------------------------------
        //String latex = "(((\\neg a \\vee b) \\wedge (c \\rightarrow d)) \\leftrightarrow (a \\vee d))";
        //Formula fromLatex = LatexParser.readFromLatex(latex);

        //System.out.println("\nLecture depuis LaTeX :");
        //System.out.println("Latex: " + latex);
        //System.out.println("Formule: " + fromLatex);
    }
}

