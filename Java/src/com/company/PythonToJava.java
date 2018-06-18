package com.company;

import java.util.Scanner;

public class PythonToJava {

    public static boolean listOf100(double[] lst) {
        // Checks if the list adds up to 100
        double sum = 0.0;
        for (double item: lst) {
            sum += item;
        }
        return sum == 100.0;
    }

    public static boolean isNum(String input) {
        return input.matches("[\\d\\.\\/]*");
    }

    public static double toDecimal() { // String input
        // Gets input from user
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter a number: ");
        String input = scan.next();

        System.out.println(input);

        if ( !isNum(input) ) {
            System.out.println("Check that you entered the number correctly!");
            return toDecimal();
        }
        else {
            if (input.contains("/")) {
                String[] splt = input.split("/");
                if (splt.length > 2) {
                    System.out.println("You have too many fractions! Try again");
                    return toDecimal();
                }
                else {
                    return Double.parseDouble(splt[0]) / Double.parseDouble(splt[1]);
                }
            }
            else {
                return Double.parseDouble(input);
            }
        }
    }




    public static void main(String args[]) {
//        System.out.println("Wow you typed in a " + toDecimal());
//
//        double[] lst1 = {100};
//        double[] lst2 = {75.0, 5, 20.0};
//        double[] lst3 = {13.5, 124.9};
//
//        System.out.println(listOf100(lst1));
//        System.out.println(listOf100(lst2));
//        System.out.println(listOf100(lst3));
//
//        System.out.println("---------------------------");
//
//        System.out.println(isNum("1234"));
//        System.out.println(isNum("123.4"));
//        System.out.println(isNum("1.2/3.4"));
//
//        System.out.println("---------------------------");
//
//        System.out.println(isNum("12a34"));
//        System.out.println(isNum("123a.4"));
//        System.out.println(isNum("1.2/a3.4"));
//
//        System.out.println("---------------------------");
//
//        System.out.println("---------------------------");
//
//        System.out.println("---------------------------");
    }
}

