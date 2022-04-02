class SomeClass{
    constructor(name){ this.name = name; }
    sayhi(){ alert(this.name); }
}

//getters and setters 

class Testing{
    constructor(name){
        this.name = name;
    }

    get name(){
        return this.name;
    }

    set name(value){
        if(value.length < 4){
            console.log("do not work");
            return;
        }
        this._name = value;
    }
}

(function(){
    let user = new Testing("somee");
    console.log(user._name);

    user = new User("__");
})


//clock

class Clock {
    constructor({template}){ this.template = template; }

    render() {
        let date = new Date();

        let hours = date.getHours();
        if (hours < 10) hours = '0' + hours;

        let mins = date.getMinutes();
        if (mins < 10) mins = '0' + mins;

        let secs = date.getSeconds();
        if (secs < 10) secs = '0' + secs;

        let output = this.template
        .replace('h', hours)
        .replace('m', mins)
        .replace('s', secs);

        console.log(output);


    }

    start(){
        this.render();
        this.timer = setInterval(() => this.render(), 1000);
    }

    stop(){
        clearInterval(timer);
    }
}

class ExtenedeClock extends Clock{
    constructor(options){
        super(options);
        let {precision = 1000} = options;
        this.precision = precision;
    }

    start(){
        this.render();
        this.timer = setInterval(() => this.render(), this.precision());
    }
}

let clock = new Clock({template: 'h:m:s'});
//clock.start();

class Animal {

    constructor(name) {
        this.name = name;
    }

    static compare(animalA, animalB) {
        return animalA.speed - animalB.speed;
    }
}

class Rabbit extends Animal {
    constructor(name) {
        super(name);
        this.name = name;
    }
}

let rabbits = [
    new Rabbit("Белый кролик", 10),
    new Rabbit("Чёрный кролик", 5)
];

let compare = rabbits.sort(Rabbit.compare);
let created = new Rabbit(Date.now());
let rabbit = new Rabbit("1Белый кролик"); // Error: this is not defined


console.log(rabbit.name, created);
console.log(compare);

