package com.example.ex01;

@FunctionalInterface
public interface RunSomething {

    //function 하나만 가능
    int doIt(int number);
    

    static void printName(){
        System.out.println("hello world");
    }

    default void printSomething(){
        System.out.println("Hello world");
    }
}
