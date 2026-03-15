// firebase.js (UPDATED WITH REAL KEYS)

const firebaseConfig = {
  apiKey: "AIzaSyARRuy_LK77TV9_xk7qngO6F99Bf63TmjE",
  authDomain: "my-protfolio-36077.firebaseapp.com",
  projectId: "my-protfolio-36077",
  storageBucket: "my-protfolio-36077.firebasestorage.app",
  messagingSenderId: "889602371178",
  appId: "1:889602371178:web:1afebab03b1f1e6bf5a413"
};

// Initialize Firebase
if (!firebase.apps.length) {
  firebase.initializeApp(firebaseConfig);
}

// Export Firestore database
const db = firebase.firestore();