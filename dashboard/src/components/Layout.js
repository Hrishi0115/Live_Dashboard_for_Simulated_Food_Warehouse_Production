// Main Layout Component - a component that will serve as the layout framework

import * as React from 'react';
import { Box, CssBaseline } from '@mui/material';

function Layout({ children }) {
    return (
        <Box sx={{ display: 'flex' }}>
            <CssBaseline />
            {/* AppBar and Drawer can be added here if needed */}
            <Box component="main" sx={{ flexGrow: 1, p:3 }}>
                {children}
            </Box>
        </Box>
    );
}

export default Layout;

