let a = 3

setTimeout(() => {
    console.log("request");

    const data = {
        one : 'test', 
        another: 'af'
    }

    console.log('data resive');
    setTimeout(() => {
        data.one = 'not test'
       console.log(data);
    }, 1000)
}, 2000)

const p = new Promise(function(resolve, reject){
   setTimeout(() => {
    console.log('data resive');

    
   },1000) 
})