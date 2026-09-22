// TASK 1 - default constructor

class PersonFirstClass(
    val name: String = "Ion",
    var age: Int = 30
)

val person1 = PersonFirstClass()
println("Name: ${person1.name} | Age: ${person1.age}")

println("---------------")  


// TASK 2 

class PersonSecondClass(val name: String, var age: Int){
    constructor(name: String) : this(name, 20) {
        if (age < 18) {
            println("User $name is underage with age: $age.")
        } else {
            println("User $name is of legal age with age: $age.")
        }
    }

    fun dispalyAge(){
        println(this.age)
    }
}

PersonSecondClass("Alice")
var tets = PersonSecondClass("Bob", 17)
tets.dispalyAge()

println("---------------")  


// TASK 3 

class PersonThirdClass( val name: String, var age: Int){

    constructor(name: String) : this(name, 0) {
        println("Created user with default age: $age and name: $name.")
    }

    constructor() : this("Bob") {
        println("New user with default age and name: $age and name")
    }
}

PersonThirdClass("Alice")
PersonThirdClass()

println("---------------")  
