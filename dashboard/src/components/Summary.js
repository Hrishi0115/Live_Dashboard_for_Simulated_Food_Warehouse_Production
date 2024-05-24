// src/components/Summary.js
import React from 'react';
import { Typography, Paper, Box } from '@mui/material';

function Summary({ recentPackage }) {
    return (
        <Paper style={{ padding: 20, marginBottom: 20 }}>
            <Typography variant="h6">Most Recent Package:</Typography>
            <Box marginTop={2}>
                <Typography>Shape: {recentPackage.shape}</Typography>
                <Typography>Size: {recentPackage.size && `${recentPackage.size[0]} x ${recentPackage.size[1]}`}</Typography>
            </Box>
        </Paper>
    );
}

export default Summary;
