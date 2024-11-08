import java.util.Scanner;
public class methods
{
    public static void add(double a,double b){
        System.out.println("The sum is: "+(a+b));
    }

    public static void subtract(double a,double b){
        System.out.println("The diffrence is: "+(a-b));
    }

    double multiply(double a,double b){
        return a*b;
    }
    // this method belongs to MyProgram
    public static void myMethod(){
        
        System.out.println("This is my method");
    }
    public static void main(String[] args)
    {
        // How do I create an object of the MyProgram class?
        
        // How do I create an object of the Scanner class?
        
        Scanner sc = new Scanner(System.in);
        methods mp = new methods();
        myMethod();
        add(10,20);
        subtract(10,20);
        
        System.out.println(mp.multiply(10,20));
        
        
        
    }
}