package com.example.employeefacade

data class EmployeeData(
    internal val id: Int,
    internal val name: String,
    internal var hoursWorked: Int,
    internal var hourlyRate: Double
)