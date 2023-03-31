const { initializeApp } = require("firebase/app");
const { getDatabase, ref, onValue, get, child } = require("firebase/database");

// TODO: Replace the following with your app's Firebase project configuration
// See: https://firebase.google.com/docs/web/learn-more#config-object
const firebaseConfig = {
    apiKey: "AIzaSyAniDY1wwh_wPHr_URVRdBY2UBpB1ccJoQ",
    authDomain: "mm-scraper-db-1f403.firebaseapp.com",
    databaseURL: "https://mm-scraper-db-1f403-default-rtdb.firebaseio.com",
    projectId: "mm-scraper-db-1f403",
    storageBucket: "mm-scraper-db-1f403.appspot.com",
    messagingSenderId: "49215773608",
    appId: "1:49215773608:web:92b6d0045a0905753fdb9d",
    measurementId: "G-R2KT55LKXG"
};

exports.handler = async (event, context) => {
    const response = {
        headers: {
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
        }}
    try {
    // Initialize Firebase
    const app = initializeApp(firebaseConfig);
    // Initialize Realtime Database and get a reference to the service
    const db = getDatabase(app);
    const dbRef = ref(db)
    await get(dbRef, 'kings_bridge_auto').then((ss)=> {
        if (ss.exists()){
            response.statusCode = 200;
            response.body = JSON.stringify(ss.val())
        } else {
            response.statusCode = 404;
            response.body = JSON.stringify('404 Data not found')
        }
    })} catch (err) {
        response.statusCode = 500;
        response.body = JSON.stringify('500 ERROR' + err.message)
    } finally {
        return response
    }
}