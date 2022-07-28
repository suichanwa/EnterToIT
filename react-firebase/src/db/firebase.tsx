import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

const firebaseConfig = {
  apiKey: "AIzaSyDw06gRXGaDhyp5C-HkKbf_RGYt8ERkWl8",
  authDomain: "react-firebase-57d4c.firebaseapp.com",
  projectId: "react-firebase-57d4c",
  storageBucket: "react-firebase-57d4c.appspot.com",
  messagingSenderId: "850074312687",
  appId: "1:850074312687:web:ee10b0ebc6e03b680d201a",
  measurementId: "G-G5BL415CG0"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

export default app;