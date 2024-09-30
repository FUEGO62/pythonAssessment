import java.util.Scanner;
public class SumOfDigits{

    public static void main(String[] args){

	Scanner input = new Scanner(System.in);

	System.out.print("Enter your number ");

	int number = input.nextInt();
	int sum = 0;
	int digits = 0;

	if(number>0 & number<1000){

		while(number!=0){

			digits = number%10;

			sum+= digits;

			number /=10;
		}

		System.out.print(sum);

	}

	else System.out.print("invalid number");





   }	

}