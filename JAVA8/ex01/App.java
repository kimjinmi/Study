package com.example.ex01;

import java.util.Arrays;
import java.util.function.Function;
import java.util.function.Supplier;
import java.util.function.UnaryOperator;

public class App {

    public static void main(String[] args){

        //스테틱 메소드
        UnaryOperator<String> hi = Greeting::hi;

        //인스턴스 메소드
        Greeting greeting = new Greeting();
        UnaryOperator<String> hello = greeting::hello;
        System.out.println(hello.apply("kkkk"));

        Supplier<Greeting> newGreeting = Greeting::new; //문자열받지않음
        newGreeting.get();

        Function<String, Greeting> nneeewGreeting = Greeting::new; //문자열받음


        String[] names ={"A", "B", "C"};

        Arrays.sort(names, String::compareToIgnoreCase);

        System.out.println(Arrays.toString(names));
        

    }
}
