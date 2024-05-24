// Integrate real-time data with WebSockets

// Handle WebSocket connections outside components for better abstraction and management

// What is a WebSocket server?

// A technology that enables real-time communication between a client (like a web browser) and a server over a single, long-lived connection.
// Unlike traditional HTTP connections, which are stateless (...) and require a new connection for each request, WebSocket connections remain open, allowing
// for full-duplex (...) communication, where both the client and server can send messages to each other at any time.

// Stateless communication mean that each request from a client to a server is independent and not reliant on any previous requests. In the case of HTTP, which is 
// a stateless protocol, each request from a client to a server is treated as a new transaction, and the server doesn't retain any information about previous 
// requests from the same client. This lack of state means that every request must contain all the necessary information
// for the server to process it, including authentication credentials, session data, etc. Statelessness simplifies server 
// design and scaling but can be limiting for applications that

// Full-duplex communication refers to the ability for both the client and the server to send messages to each other simultaneously over the same connection. In a 
// full-duplex communication model, there is no need to wait for one party to finish sending a message before the other can respond. This allows for more efficient and 
// real-time communication, as both parties can send and receive data concurrently. WebSocket technology enables full-duplex communication, allowing for bi-directional 
// data flow between clients and servers without the overhead of multiple HTTP requests and responses.This is particularly useful for applications that require real-time
// updates or interactive features, such as chat applications, multiplayer games, 
// and collaborative editing tools.

// services/socketService.js

import io from 'socket.io-client';
const socket = io('http://localhost:8080');

const subscribeToData = (callback) => {
    // this is a function you can call to start listening to updates from the server.
    // you provide a 'callback' function, a function that will be called whenever new data comes in from the server
    socket.on('update_dashboard', data => {
        // socket.on: sets up an event listener for a specific event type - in this case, it's listening for an event called 'update_dashboard',
        // which indicates the new data related to the dashboard is being sent from the server
        // the actual data that is received from the server when the 'update_dashboard' event occurs - what the server sends to the client
        callback(data);
        // provided function that is called whenever new data is received from the server.
    });
};

const unsubscribeFromData = () => {
    socket.off('update_dashboard');
};

const disconnectSocket = () => {
    if(socket.connected) {
        socket.disconnect();
    }
};

export { subscribeToData, unsubscribeFromData, disconnectSocket };