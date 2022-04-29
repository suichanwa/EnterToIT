let mover;

class init{
    setup(){
        createCanvas(200,200);
        mover = new Mover(150, 200);
    } 
}


class Mover{
    constructor(x, y){
        this.pos = ceratevector(x, y);

    }
}

