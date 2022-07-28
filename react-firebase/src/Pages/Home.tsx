import React, { useRef } from "react";


export default function Home(){
    const inputField = React.useRef() as React.MutableRefObject<HTMLInputElement>;

   return(
       <div>
           <form>
               <label>input</label>
                <input type="text" ref={inputField}/>
               <button type="submit">submit</button>
           </form>
       </div>
   ) 
}