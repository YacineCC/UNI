package fr.univtln.jovyan.tp.tp1

/**
 * A very simple class to say Hello
 * @author Emmanuel Bruno
 *
 */

public class HelloWorld {

	/**
	 *  A dummy constructor
	 */
	public HelloWorld() {}

	/**
	 * The entry point of the class
	 *  @param args The first parameter is a firstname
	 */
	public static void main(String[] args) {
		if (args.length==1)
			System.out.println("Bonjour "+args[0]);
		else
			System.out.println("Usage : PremierProgramme [prenom]");
	}

}
