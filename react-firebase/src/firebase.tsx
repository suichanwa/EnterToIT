import { initializeApp } from "firebase/app";
import {getFirestore} from "@firebase/firestore"

const firebaseConfig = {
  apiKey: "AIzaSyDjiwz23nwvPeHb7gw7zhU8tYgi8zQRVWU",
  authDomain: "firibasiapp.firebaseapp.com",
  projectId: "firibasiapp",
  storageBucket: "firibasiapp.appspot.com",
  messagingSenderId: "240637051000",
  appId: "1:240637051000:web:97f50f358cfaa00563ad8d"
};

const app = initializeApp(firebaseConfig);
export const firestore = getFirestore(app);