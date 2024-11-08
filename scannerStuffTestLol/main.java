import java.util.Scanner;

public class main
{
	public static void watsGood(){
		System.out.println("hi");
	}
	
	public void watsGoodie(){
		System.out.println("hi2");
	}
	
	public static void main(String[] args)
	{
		
		main np = new main();
		Scanner sc = new Scanner(System.in);
		
		System.out.println("type your name:");
		
		String name = sc.nextLine();
		
		System.out.println("Hello, "+name+"!");
		
		System.out.println("type a whole number:");
		
		int number = sc.nextInt();
		
		watsGood();
		watsGoodie();
		
		System.out.println("Hello the number you typed: "+number+"!");
		
		for(int i = 1; i <= 11; i++){
			System.out.println(i);
		}
		

		for(int i = 10; i <= 100; i+=10){
			System.out.println(i);
		}
	}
}