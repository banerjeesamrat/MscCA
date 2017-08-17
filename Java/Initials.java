//Author - Mihir Vohra
//Date - 16/08/2017

import java.util.Scanner;

//begin class
class Initials{
    String full_name;

    //method to accept the full name
    void accept(){
        System.out.print("Enter the full name : ");

        //Scanner object for scanning the input from the console
        Scanner sc=new Scanner(System.in);

        this.full_name=sc.nextLine();
    }

    //method to generate the Initials
    String get_initials(){
        String[] temp=full_name.split(" ");

        //variable to store the initials
        String initals="";

        for(int i=0;i<temp.length;i++)
            initals+=temp[i].charAt(0);
        return initals;
    }

    //main method
    public static void main(String[] args) {
        //object of the class
        Initials initials_object=new Initials();

        //accepting the input
        initials_object.accept();

        //generating and displaying the initials
        System.out.println("The initials of " + initials_object.full_name + " is : " + initials_object.get_initials());
    }
}
