// Utilisation d'une IA Génrative (ChatGPT) pour ce TP
//
package fr.univtln.yhaouas846.IaSymbolique;


public class LatexParser {
    private final String input;
    private int pos = 0;
    private Token cur;

    private enum TokenType { VAR, NOT, AND, OR, IMP, EQU, LPAREN, RPAREN, EOF }
    private static class Token {
        TokenType type;
        String text;
        Token(TokenType t, String txt){ type=t; text=txt; }
    }
    public LatexParser(String input){
        this.input = preprocess(input);
        next();
    }

    // Preprocess: replace LaTeX commands by unique markers (we'll parse them)
    private static String preprocess(String s){
        // normalize spaces
        s = s.replaceAll("\\s+", " ");
        // ensure \neg, \wedge etc are kept
        return s;
    }

    private void next(){
        skipSpaces();
        if (pos >= input.length()){ cur = new Token(TokenType.EOF, ""); return; }
        char c = input.charAt(pos);
        if (c == '('){ pos++; cur = new Token(TokenType.LPAREN, "("); return; }
        if (c == ')'){ pos++; cur = new Token(TokenType.RPAREN, ")"); return; }
        // check for backslash commands
        if (c == '\\'){
            // read command
            int start = pos;
            pos++; // skip '\'
            StringBuilder sb = new StringBuilder();
            while(pos < input.length() && Character.isLetter(input.charAt(pos))){
                sb.append(input.charAt(pos++));
            }
            String cmd = sb.toString();
            switch(cmd){
                case "neg": cur = new Token(TokenType.NOT, "\\neg"); return;
                case "wedge": cur = new Token(TokenType.AND, "\\wedge"); return;
                case "vee": cur = new Token(TokenType.OR, "\\vee"); return;
                case "rightarrow": cur = new Token(TokenType.IMP, "\\rightarrow"); return;
                case "leftrightarrow": cur = new Token(TokenType.EQU, "\\leftrightarrow"); return;
                default:
                    // unknown command -> treat as var name (rare)
                    cur = new Token(TokenType.VAR, "\\"+cmd);
                    return;
            }
        }
        // also accept textual -> and <-> and symbols like ->, <->, ^, v, ~, !
        if (input.startsWith("->", pos) || input.startsWith("\\to", pos)){
            pos += input.startsWith("->", pos) ? 2 : 3;
            cur = new Token(TokenType.IMP, "->"); return;
        }
        if (input.startsWith("<->", pos)){
            pos += 3; cur = new Token(TokenType.EQU, "<->"); return;
        }
        if (input.charAt(pos) == '!'){
            pos++; cur = new Token(TokenType.NOT, "!"); return;
        }
        if (input.charAt(pos) == '~'){
            pos++; cur = new Token(TokenType.NOT, "~"); return;
        }
        if (input.charAt(pos) == '^'){
            pos++; cur = new Token(TokenType.AND, "^"); return;
        }
        if (input.charAt(pos) == 'v' || input.charAt(pos) == 'V'){
            // ambiguous with var; check surrounding spaces or if it's "vee" handled earlier.
            // If single letter 'v' with spaces, interpret as OR
            boolean isOr = (pos==0 || Character.isWhitespace(input.charAt(pos-1))) &&
                    (pos+1==input.length() || Character.isWhitespace(input.charAt(pos+1)));
            if (isOr){
                pos++; cur = new Token(TokenType.OR, "v"); return;
            }
        }
        // variable: letters, digits, underscore
        if (Character.isLetterOrDigit(c) || c=='_'){
            int start = pos;
            while(pos < input.length() && (Character.isLetterOrDigit(input.charAt(pos)) || input.charAt(pos)=='_')) pos++;
            String name = input.substring(start,pos);
            cur = new Token(TokenType.VAR, name); return;
        }
        // if none matched, skip char
        pos++;
        next();
    }

    private void skipSpaces(){
        while(pos < input.length() && Character.isWhitespace(input.charAt(pos))) pos++;
    }

    // Grammar (precedence):
    // expr := equiv
    // equiv := imp ( (<->) imp )*
    // imp := or ( (->) imp )?
    // or := and ( (vee) and )*
    // and := unary ( (wedge) unary )*
    // unary := NOT unary | atom
    // atom := VAR | '(' expr ')'
    public Formula parse(){
        Formula r = parseEquiv();
        if (cur.type != TokenType.EOF) {
            // allow trailing tokens, ignore
        }
        return r;
    }

    private Formula parseEquiv(){
        Formula left = parseImp();
        while(cur.type == TokenType.EQU){
            next();
            Formula right = parseImp();
            left = F.equiv(left, right);
        }
        return left;
    }

    private Formula parseImp(){
        Formula left = parseOr();
        if (cur.type == TokenType.IMP){
            next();
            Formula right = parseImp(); // right-assoc
            left = F.imp(left, right);
        }
        return left;
    }

    private Formula parseOr(){
        Formula left = parseAnd();
        while(cur.type == TokenType.OR){
            next();
            Formula right = parseAnd();
            left = F.or(left, right);
        }
        return left;
    }

    private Formula parseAnd(){
        Formula left = parseUnary();
        while(cur.type == TokenType.AND){
            next();
            Formula right = parseUnary();
            left = F.and(left, right);
        }
        return left;
    }

    private Formula parseUnary(){
        if (cur.type == TokenType.NOT){
            next();
            Formula f = parseUnary();
            return F.not(f);
        } else {
            return parseAtom();
        }
    }

    private Formula parseAtom(){
        if (cur.type == TokenType.VAR){
            String name = cur.text;
            next();
            return F.var(name);
        } else if (cur.type == TokenType.LPAREN){
            next();
            Formula f = parseEquiv();
            if (cur.type == TokenType.RPAREN) next();
            return f;
        } else {
            // unexpected token -> treat as false
            next();
            return F.var("?" + (pos));
        }
    }

    public static Formula readFromLatex(String latex){
        // we will replace common LaTeX shortcuts like \neg, \wedge, \vee, \rightarrow, \leftrightarrow
        String s = latex;
        s = s.replaceAll("\\\\,", " ");
        // keep commands; parser checks backslash commands directly
        LatexParser p = new LatexParser(s);
        return p.parse();
    }
}