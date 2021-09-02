package com.example.ex01;

import java.util.function.*;

public class Foo {

    public static void main(String[] args){
        RunSomething runSomething = (number) -> {
            return number + 10;
        };

        System.out.println(runSomething.doIt(1));

        Plus10 plus10 = new Plus10();
        System.out.println(plus10.apply(1));

        Function<Integer, Integer> plus20 = (i) -> i+20;
        System.out.println(plus20.apply(1));

        Function<Integer, Integer> multiply2 = (i) -> i * 2;
        System.out.println(multiply2.apply(1));

        //BiFunction

        Function<Integer, Integer> functionMix =plus20.compose(multiply2);// a -> multiply2 -> plus20
        System.out.println(functionMix.apply(2));

        plus20.andThen(multiply2); // a -> plus20 -> multiply2
        System.out.println(plus20.andThen(multiply2).apply(2));

        Consumer<Integer> printT = (i) -> System.out.println(i);
        printT.accept(10);

        Supplier<Integer> get10 = () -> 10;
        System.out.println(get10);

        Predicate<String> startsWithS = (s) -> s.startsWith("s");
        startsWithS.negate();

        UnaryOperator<Integer> plus30 = (i) -> i+30;

        //BinaryOperator

        BinaryOperator<Integer> get100 = (Integer a, Integer b) -> a+b;

        Foo foo = new Foo();


    }

    private void run(){
        int baseNum = 10; //final

        //로컬클래스 : 쉐도잉 O
        class LocalCass{
            void printBaseNum(){
                int baseNum = 11;
                System.out.println(baseNum); //11
            }
        }

        //익명클래스 : 쉐도잉 O
        Consumer<Integer> integerConsumer = new Consumer<Integer>() {
            @Override
            public void accept(Integer baseNum) {
                System.out.println(baseNum);
            }
        };
        
        //람다 : 쉐도잉 X
        IntConsumer printInt = (i) -> {
            //int baseNum = 11; 컴파일에러
            System.out.println(i + baseNum);
        };

        printInt.accept(10);
    }
}
