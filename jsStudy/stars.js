class timeToCodeStars{
   main(){
    let n = 5;
    let string = "*";
    
        for(let i = 0; i < n; i++){
            for(let j = 0; j < n; j++){
                string += "*";
            }        
            string += "\n";
        }
        console.log(string);
    }

    anotherMainFunc(){
        let n = 5;
        let string = "*";

        for(let i = 1; i <= n;i++){
            for(let j = 0; i < n - i; j++){
                string += "*";
            }
            for (let k = 0; k < i; k++) {
                string += "*";
            }
            string += "\n";
        }
        console.log(string);
    }

    partofpyramide(){
        let n = 6;
        let string = "";

        for(let i = 1; i <= n; i++){
            for(let j = 0; i < n - i; j++){
                if(i === n ){
                    string += "*";
                } else {
                    if(j == 0 || j == i - 1){
                        string += "*";
                    } else {
                        string += "*";
                    }
                }
            }
            string += "\n"; 
        }
        console.log(string);
    }

    pyramide(){ 
        let n = 5;
        let string = "";

        for(let i = 1; i <= n; i++){
            for(let j = 1; i < n - i; j++){
               string += " ";
            }

            for(let k = 0; k < 2 * i - 1; k++){
                string += "*";
            }
            string += "\n"; 
        }
        console.log(string);
    }

    backwardPyramide(){ 
        let n = 5;
        let string = "";

        for(let i = 0; i <= n; i++){
            for(let j = 0; i < n - i; j++){
               string += " ";
            }  
            for(let k = 0; k < 2 * i - 1; k++){
                string += "*";
            }

           string += "\n"; 
        }
        console.log(string);
    }

    diamond(){
        let n = 5;
        let string = "*";

        for(let i = 1; i <= n; i++){
            for(let j = n; j > i; j--){
                string += " ";
            }
            for (let k = 0; k < i * 2 - 1; k++) {
                string += "*";
            }
            string += "\n";
        }

        for (let i = 1; i <= n - 1; i++) {
            for (let j = 0; j < i; j++) {
              string += " ";
            }
            for (let k = (n - i) * 2 - 1; k > 0; k--) {
              string += "*";
            }
            string += "\n";
          }
        console.log(string);
    }
}



var run = new timeToCodeStars;
run.main();