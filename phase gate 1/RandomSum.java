import java.util.Scanner;
import java.security.SecureRandom;
public class RandomSum{

    public static void main(String[] args){

	SecureRandom randomNumber = new SecureRandom();
	Scanner input = new Scanner(System.in);

int number1 = randomNumber.nextInt(100);
int number2 = randomNumber.nextInt(100);

int total = number1 + number2;

System.out.println("number 1 is "+ number1+ " number 2 is "+ number2);

System.out.println("Enter the sum of these numbers ");

int answer = input.nextInt();

System.out.println(checkAnswer(total,answer));



}
	

    public static boolean checkAnswer(int total,int answer){

	if(total == answer) return true;

	else return false;

    }

}
