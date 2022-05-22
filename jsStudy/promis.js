function times() {
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
}

const p = new Promise(function(resolve, reject){
   setTimeout(() => {
    console.log('data resive');
    const another = {
        server: 'servername',
        port: 2000,
        status: 'working'
    }
    resolve(another);
   },1000) 
})

p.then((another => {
   return new Promise(function(resolve, reject){
    another.modified = true; 
    resolve(another);
   }, 2000) 

})).then(clientData => {
    console.log('data', clientData);
})