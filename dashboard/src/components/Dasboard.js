// Dashboard.js will serve as the container for charts, summaries, and any other analytical tools
// components/Dashboard.js

// designed to display real-time data received over a WebSocket connection.

import React, { useEffect, useState } from 'react';
import { disconnectSocket, subscribeToData, unsubscribeFromData } from '../services/socketService';
import Chart from './Chart';
import Summary from './Summary';


function Dashboard() {
    const [data, setData] = useState([]);
    // An array (initialised to an empty array []) that holds all the data packages received from the WebSocket server
    const [recentPackage, setRecentPackage] = useState({});
    // Stores the most recent data package received

    useEffect(() => {
        // Set up a listener for new data

        // Define a new function 'handleNewData' that takes in 'packageData' - the new data received from the server.
        // within 'handleNewData', we update our component's state:
        // we take the current data 'currentData' and add the new 'packageData' to it using the spread operator '[...currentData, packageData],
        // then update the state with 'setData'
        // spread operator: used for expanding elements of an iterable like an array or an object
        // e.g. 
        // const array1 = [1,2,3]
        // const array2 = 4
        // const combinedArray = [...array1, array2] // [1,2,3,4]

        const handleNewData = (packageData) => {
            setData(currentData => [...currentData, packageData]);
            setRecentPackage(packageData);
        };


        subscribeToData(handleNewData);

        // Clean up function to unsubscribe and disconnect when components unmounts
        // what happens when the component is unmounted/removed from the screen
        // this function closes the connection to the server/preventing any further communication

        return () => {
            disconnectSocket();
            // 
        };
        
    }, []);
    // , '[]' - dependencies array: 

    return (
        <div>
            <Summary recentPackage={recentPackage} />
            <Chart data={data} />
        </div>
    );
}

export default Dashboard;

