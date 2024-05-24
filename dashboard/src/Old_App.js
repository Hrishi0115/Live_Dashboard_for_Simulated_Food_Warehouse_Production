// // src/App.js
// import React, { useEffect, useState } from 'react';
// import io from 'socket.io-client';
// import { Typography, Paper, Box } from '@material-ui/core';
// import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip } from 'recharts';

// function App() {
//   const [data, setData] = useState([]);
//   const [recentPackage, setRecentPackage] = useState({});

//   useEffect(() => {
//     const socket = io('http://localhost:8080');
//     socket.on('update_dashboard', (packageData) => {
//       setData(currentData => [...currentData, packageData]);
//       setRecentPackage(packageData);
//     });
//   }, []);

//   return (
//     <div style={{ padding: 20 }}>
//       <Typography variant="h4" component="h1" gutterBottom>
//         Package Count Dashboard
//       </Typography>
//       <Paper style={{ padding: 20, marginBottom: 20 }}>
//         <Typography variant="h6">Most Recent Package:</Typography>
//         <Box marginTop={2}>
//           <Typography>Shape: {recentPackage.shape}</Typography>
//           <Typography>Size: {recentPackage.size && `${recentPackage.size[0]} x ${recentPackage.size[1]}`}</Typography>
//         </Box>
//       </Paper>
//       <BarChart width={600} height={300} data={data.map(item => ({...item, size: item.size[0]}))}>
//         <CartesianGrid strokeDasharray="3 3" />
//         <XAxis dataKey="shape" />
//         <YAxis />
//         <Tooltip />
//         <Bar dataKey="size" fill="#8884d8" />
//       </BarChart>
//     </div>
//   );
// }

// export default App;
