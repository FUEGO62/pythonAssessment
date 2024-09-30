import java.util.Scanner;
public class IncreasingOrder{

    public static void main(String[] args){

	Scanner input = new Scanner(System.in);

	int [] numbers = new int [3];

	for(int count = 0; count <3;count++){

		System.out.println("Enter a number");

		numbers[count] = input.nextInt();

	}

	for(int count = 0 ;count< numbers.length; count++){
	
		for(int counter = 0; counter<numbers.length-1; counter++){

			if(numbers[counter]>numbers[counter+1]){

				numbers[counter+1]= numbers[counter] + numbers[counter+1];
				numbers[counter] = numbers[counter+1]- numbers[counter];
				numbers[counter+1] = numbers[counter+1] - numbers[counter];
		
			}
	
		}

		
	}


	for(int count = 0; count < numbers.length; count++){

		System.out.print(numbers[count]+" ");

	}




    }

}