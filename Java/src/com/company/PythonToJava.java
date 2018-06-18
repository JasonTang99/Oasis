package com.company;

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


    public static void main(String args[]) {
        double[] lst1 = {100};
        double[] lst2 = {75.0, 5, 20.0};
        double[] lst3 = {13.5, 124.9};

        System.out.println(listOf100(lst1));
        System.out.println(listOf100(lst2));
        System.out.println(listOf100(lst3));

        System.out.println("---------------------------");

        System.out.println(isNum("1234"));
        System.out.println(isNum("123.4"));
        System.out.println(isNum("1.2/3.4"));

        System.out.println("---------------------------");

        System.out.println(isNum("12a34"));
        System.out.println(isNum("123a.4"));
        System.out.println(isNum("1.2/a3.4"));

        System.out.println("---------------------------");

        System.out.println("---------------------------");

        System.out.println("---------------------------");
    }
}

