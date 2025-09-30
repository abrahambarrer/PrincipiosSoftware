package com.example.animal

abstract class Animal (
    protected val type: String,
    protected val name: String,
    protected var age: Int?) {

    constructor(): this(type = "Unknown", name = "Unkown", age = null)

    abstract fun talking() // Abstract method
}