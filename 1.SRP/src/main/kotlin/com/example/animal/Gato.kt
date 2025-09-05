package com.example.animal

import java.lang.reflect.Type

class Gato(
    type: String,
    name: String,
    age: Int?,
    private val race: String)
    : Animal(type, name, age) {

    override fun talking(){
        println("The cat $name is talking...")
    }
}