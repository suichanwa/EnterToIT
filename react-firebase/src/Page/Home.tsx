import React from "react";
import {firestore} from "../firebase";
import {addDoc, collection} from "@firebase/firestore";


export default function Home(){
    const messageRef = React.useRef<any[]>([]);

    const ref = collection(firestore,"messages");

    const HandleSave = async(e: any) => {
        e.preventDefault();

        let data = {
            message: messageRef.current?.values,
        }

        try{
            addDoc(ref, data);
        } catch(e: any){
            console.log(e);
        }
    }

    return(
        <div>
            <form onSubmit={HandleSave}>
                <input type="text" ref={messageRef} />
                <button type="submit">Save</button>
            </form>
        </div>
    ) 
}