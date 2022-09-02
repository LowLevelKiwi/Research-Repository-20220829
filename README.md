# Research-Repository

This is my repositrory for the Research Repository assesment,
In this repo I have two different things, a function that will convert a matrix of numbers into an Ascii Image art as well as two different types of sorts a bubble sort and a quick sort

I chose these to do my research on because I've always wanted to learn a bit more about how sorting algorythims worked, and I liked trying to make ascii images so I thought of a way to make creating them easier by using matrixs of numbers 

I got the Python sorting algorithyms code from https://realpython.com/sorting-algorithms-python/

and I was inspired by the "Compete python Development Zero To Mastery udemy series video 76 Our first gui" for the Ascii image generator

## Ascii Image Generator

the Ascii Image Generator works by inputting a matrix of numbers between 0 - 13, and it will then split the matrix into its rows and for each number in the row it will convert it into its asscoiated string and add it to an accumulitve string adding a new line symbol for each row, then once it has proccessed all the rows it will return the accumulitive string so that it can be used elsewhere 

## Bubble Sort Algorithm

the bubble sort algorithm works by starting at the index of zero all the way until the inputed arrays length - 1.
It will make a comparason between the current index and the one next it and if the current index is higher than the one next to it it will exchange its places repeating this process till it reaches the end of the array.
Then it will repeat the entire function again at the index of zero till it reaches the currently "sorted" portion of the array at the end.
Once the function runs once without making any exchanges it will then end the function returning the array at which point should be sorted.

## Quick Sort Algorithm

the quick sort algorithm works by first checking if the inputed array has 0 - 1 items in it, if it does it will return the list otherwise it will continue by randomly picking a item in the inputed array and making that the pivot point.
it will then go through every item in the inputed array and assign them to one of three lists, lower, equal, and higher, depeneding on the value compared to the pivots value.
It will subsequently call itself inputing the lower array, and then call itself again inputing the higher array this time.
It will then finally return an appended array of the result of the lower array self call + the equal array + the result of the higher array self call.

# Reflections

## What is OOP

Object-Oreiented Programing (OOP) is a style of programming charicterized by the identifaction of classes of objects closely linked with methods, as well as includes the idea of inheritnce of attributes and methods. A good way to describe this could be a mechanic, their class would be a mechanic that would inherit from another class of person, the person class may have some base variables like gender or height, and some base methods (functions) like walking or looking.
The mechanic class inheriting this also has access to these base varibles / methods and are able to overwrite these functions as well as have their own base variables or methods like workload or fixing a car.
these new methods aren't apart of the orignal person class so any other class that inherits the person class doesn't have access to the mechainc methods and variables them unless they also inherit the mehcanic class,
Some OOP languages can also allows for deeply nested inheritence, so going back to the mechanic analogy, if there was a class that only inherited the mechanic class it would still also inherit the person class, the same goes for if the person class also inherited from another class lets say mammal, then the class that inherits only the mehcanic class would still have access to the mammal classes variables / methods.
Also some OOP languages also allows for a class to inherit from two different classes like a class of bat could inherit mammal as well as a class for a winged animal

> Inheritence Example
>level:
>1           Mammal     Winged animal 
>           /      \   /
>2    Person        Bat
>        |
>3   Mechanic
>

## What is Python

Python is a "Dynamicly Typed" type of high level programing languge, high level meaning it is desiged to be as readable as functionaly possible, it is designed to be able to support multiple different programming styles like Structured and Object-Oreiented Programing, because of this it has a wide array of uses from machine learing to game design to web pages,





