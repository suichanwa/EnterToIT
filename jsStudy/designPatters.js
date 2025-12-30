function Employee(name){ 
    this.name = name;

     this.say = function () {
        console.log("I am employee " + name);
    };
}

function EmployeeFactory(){
    this.create = function(name){
        return new Employee(name);
    };
}

function Vendor(name){ 
    this.create = function(name){
        return new Vendor(name);
    }
}

function VendorFactory(name){
    this.name = name;

    this.create = function(name){
        return new Vendor(name);
    }
}

function run(){
    var persons = [];

    var employeeFactory = new EmployeeFactory();
    var vendorFactory = new VendorFactory();

    persons.push(employeeFactory.create("some name"));
    persons.push(vendorFactory.create("some name"));

    for(var i = 0, len = persons.length; i < len; i++){
        persons[i].say();
    } 
} 
run();