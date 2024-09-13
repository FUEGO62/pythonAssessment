import java.util.Scanner;

public class MortgageCalculator{

public static void main (String...args){

Scanner input = new Scanner(System.in);

System.out.println("Enter the principal amount: ");

double principal = input.nextInt();

System.out.println("Enter the annual interest rate: ");

double annualRate = input.nextInt();

System.out.println("Enter the duration in years: ");

double yearlyDuration = input.nextInt();

double monthlyRate = annualRate/1200;

double timeInMonths = yearlyDuration*12;

double monthlyRateplus1 = monthlyRate +1;

double factor = (double)Math.pow(monthlyRateplus1,timeInMonths);

double monthlyPayment =principal*((monthlyRate*factor)/(factor-1));

System.out.printf("your monthly payment is %.2f",monthlyPayment);














}

}