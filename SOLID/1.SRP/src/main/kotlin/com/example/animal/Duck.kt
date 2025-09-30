package com.example.animal

import java.lang.reflect.Type

class Duck (
    type: String,
    name: String,
    age: Int?,
    size: String
) : Animal(type, name, age), Volador {

    override fun fly() {
        println("The duck $name is flying...")
    }

    override fun eat() {
        println("The duck $name is eating")
    }

    override fun talking() {
        println("Duck $name says cuac...")
    }
}