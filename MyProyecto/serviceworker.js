var CACHE_NAME = 'my-site-cache-v2';
var urlsToCache = [
    '/',
    '/galeria/',
];

self.addEventListener('install', function(event) {
    // Perform install steps
    event.waitUntil(
        caches.open(CACHE_NAME)
        .then(function(cache) {
            console.log('Opened cache');
            return cache.addAll(urlsToCache);
        })
    );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(

        fetch(event.request)
        .then((result) => {
            return caches.open(CACHE_NAME)
                .then(function(c) {
                    c.put(event.request.url, result.clone())
                    return result;
                })

        })
        .catch(function(e) {
            return caches.match(event.request)
        })



    );
});



//codigo para notificaciones push

importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var firebaseConfig = {
    apiKey: "AIzaSyC1Xx1cpBEcc-N4NpfEhgX57T0GzDpJX5E",
    authDomain: "floreria-266c9.firebaseapp.com",
    databaseURL: "https://floreria-266c9.firebaseio.com",
    projectId: "floreria-266c9",
    storageBucket: "floreria-266c9.appspot.com",
    messagingSenderId: "15323339718",
    appId: "1:15323339718:web:8dd985bb7294e910a6f0c7"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

let messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function (payload) {
    let title = payload.notification.title;

    let options = {
        body:payload.notification.body,
        icon:payload.notification.icon
    }

    self.registration.showNotification(title, options);
    
});