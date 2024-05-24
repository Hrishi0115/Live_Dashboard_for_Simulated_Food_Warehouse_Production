// src/components/Chart.js
import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip } from 'recharts';

function Chart({ data }) {
    return (
        <BarChart width={600} height={300} data={data.map(item => ({...item, size: item.size[0]}))}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="shape" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="size" fill="#8884d8" />
        </BarChart>
    );
}

export default Chart;
