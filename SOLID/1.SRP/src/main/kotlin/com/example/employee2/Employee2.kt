package com.example.employee2

data class Employee2 (
    val id : Int,
    val name: String,
    internal var hoursWorked: Int,
    var hourlyRate: Double
)