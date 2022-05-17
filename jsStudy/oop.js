//time to deeply study oop
class Human {
    constructor(name){
        this.name = name;
    }

    say(){
        const show = console.log(`testing ${this.name}`);
        console.log(show);
    }
}

class Man extends Human {
    constructor(name){
        super(name);
    }
}

class Coder extends Human {
    constructor(name){
        super(name);
    }

    say(){
        console.log(`testing ${this.name}`);
    }
}

const first = new Human('first user name');
const another = new Coder('fist username');

first.say();
another.say();
