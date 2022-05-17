function createAnalytics(){
    let counter = 0;

    const listener = () => counter++;

    document.addEventListener('click', listener);

    return { 
        destroy(){
            document.removeEventListener('click', listener);
            isDestroyes = true;
        },

        getClick(){
            if(isDestroyes){
                console.log("testing");
            }
            return counter;
        }
    }
}

window.analytics = createAnalytics();