/*
Author: Kushal Katta
Date Created: 14 Aug 2017
Date Last Modified: 16 Aug 2017
*/

import java.util.Scanner;
class Arrays
{
    //Declaring Scan Object To Scan Values
    Scanner scan = new Scanner(System.in);
    
    //Method to Read Array Values of a Given Size
    int[] readArray (int size)
    {
        int array[] = new int [size];
        for(int i=0; i<size; i++)
        {
            System.out.print("Enter a Value ("+i+"): ");
            array[i]=scan.nextInt();
        }
        return array;
    }

    //Method to Display
    void display(int array[])
    {
        System.out.println("Array Contents: ");
        for(int i=0; i<array.length; i++)
        {
            System.out.print(array[i]+ " ");
        }
        System.out.println();
    }

    //Method To Add Two Arrays.
    int[] addArray(int array1[], int array2[])
    {
        int sumArray[]=new int[array1.length];
        if(array1.length!=array2.length)
        {
            System.out.println("Arrays Are Of Different Sizes, So Can't be added.");
            return sumArray;
        }
        for(int i=0; i<array1.length;i++)
        {
            sumArray[i]=array1[i]+array2[i];
        }
        return sumArray;
    }

    //Method To Return The Common Elements in 2 given Arrays.
    int[] commonElements(int array1[], int array2[])
    {
        int maxLength=0;
        if(array1.length>array2.length)
        {
            maxLength=array1.length;
        }
        else
        {
            maxLength=array2.length;
        }
        int common[] = new int[maxLength];
        
        int count=0;
        for(int i=0;i<array1.length;i++)
        {
            for(int j=0;j<array2.length;j++)
            {
                if(array1[i]==array2[j])
                {
                    common[count]=array1[i];
                    count++;
                    break;
                }
            }
        }

        int commonElements[]=new int[count];
        
        for(int z=0; z<count; z++)
        {
            commonElements[z]=common[z];
        }
        return commonElements;
    }

    //Method To Sort An Array.
    int[] sortArray(int array[])
    {
        for(int i=0;i<array.length;i++)
        {
            for(int j=i;j<array.length;j++)
            {
                if(array[i]>array[j])
                {
                    int temp=array[i];
                    array[i]=array[j];
                    array[j]=temp;
                }
            }
        }
        return array;
    }

    //Method To Return Initials of Name
    String initials(/*char array[]*/)
    {
        System.out.print("Enter a Name: ");
        String input = scan.nextLine();

        char array[]=input.toCharArray();

        if(array.length==0)
        {
            return "";
        }

        String str = array[0]+"";
        for(int i=1; i<array.length;i++)
        {
            if(array[i]==' ')
            {
                str += array[i+1];
            }
        }
        return str;
    }
}

class Main
{
    public static void main(String[] args) {
        //Object of Arrays Class
        Arrays arr = new Arrays();

        //Declaring array1 to Store 1st Array
        System.out.println("\n1st Array: ");
        int array1[] = arr.readArray(5);
        //Declaring array2 to Store 2nd Array
        System.out.println("\n2nd Array: ");
        int array2[] = arr.readArray(5);
        

        //Displaying 1st Array
        System.out.println("\n1st Array: ");
        arr.display(array1);
        //Displaying 2nd Array
        System.out.println("\n2nd Array: ");
        arr.display(array2);
        
        
        //Declaring sum Array to store sum of above 2 arrays
        int sum[] = arr.addArray(array1,array2);
        System.out.println("\nSum of Arrays: ");
        //Displaying Sum Array
        arr.display(sum);


        //Declaring commonElements Array to store common Elements of above 2 arrays
        int commonElements[] = arr.commonElements(array1,array2);
        System.out.println("\nCommon Elements of Arrays: ");
        //Displaying Common Elements Array
        arr.display(commonElements);

        //Sorting Array
        int array3[] = arr.sortArray(array1);
        //Display Sorted Array
        System.out.println("\nSorted Elements of Arrays: ");
        arr.display(array3);

        //Input Name and Display Initials
        System.out.println("Initials of Your Entered Name: " + arr.initials());
    }
}