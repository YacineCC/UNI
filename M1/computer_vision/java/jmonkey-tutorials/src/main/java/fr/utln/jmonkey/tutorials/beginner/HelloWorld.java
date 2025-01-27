package fr.utln.jmonkey.tutorials.beginner;

import com.jme3.app.SimpleApplication;
import com.jme3.material.Material;
import com.jme3.scene.Geometry;
import com.jme3.scene.Node;
import com.jme3.scene.shape.Box;
import com.jme3.scene.shape.Sphere;
import com.jme3.system.AppSettings;
import com.jme3.math.ColorRGBA;

/** Sample 1 - how to get started with the most simple JME 3 application.
 * Display a blue 3D cube and view from all sides by
 * moving the mouse and pressing the WASD keys. */
public class HelloWorld extends SimpleApplication {

    /**
     * The main method.
     * @param args the main method arguments
     */
    public static void main(String[] args){
    	
    	AppSettings settings=new AppSettings(true);
    	
        HelloWorld app = new HelloWorld();
        app.setShowSettings(false);
        app.setSettings(settings);
        app.start(); // start the game
    }

    /**
	 * The default constructor. 
	 */
    public HelloWorld(){
	}

    @Override
    public void simpleInitApp() {
        Box b = new Box(1, 1, 1); // create cube shape
        Geometry geom = new Geometry("Box", b);  // create cube geometry from the shape
        Material mat = new Material(assetManager,
          "Common/MatDefs/Misc/Unshaded.j3md");  // create a simple material
        mat.setColor("Color", ColorRGBA.Green);   // set color of material to blue
        geom.setMaterial(mat);                   // set the cube's material

        Sphere s = new Sphere(3, 3, 2);
        Geometry geom2 = new Geometry("Sphere", s);
        Material mat2 = new Material(assetManager,  "Common/MatDefs/Misc/Unshaded.j3md");
        mat2.setColor("Color", ColorRGBA.White);
        geom2.setMaterial(mat2);
        geom2.setLocalTranslation(2, 1, 1);

        Node pivot = new Node("Pivot");
        rootNode.attachChild(pivot);
        pivot.attachChild(geom);
        pivot.attachChild(geom2);
        pivot.rotate(.4f, .4f, 0f);

        Material mat3 = new Material(assetManager, "Common/MatDefs/Misc/ShowNormals.j3md");
        //mat3.setColor("Color", ColorRGBA.White);
        geom2.setMaterial(mat3);


    }
}