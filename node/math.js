function square(num){
    if(check(num)){
        return num * num;
    } else {
        return null;
    }
}

function cube(num){
    if (check(num)){
        return num * num * num
    } else {
        return false;
    }
}

function check(num){
    if(num > 0){
        return true;
    } else {
        return false;
    }
}

exports.square = square;
exports.cube = cube;
