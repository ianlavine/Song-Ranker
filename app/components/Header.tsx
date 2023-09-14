"use client"
import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import MusicVideoIcon from '@mui/icons-material/MusicVideo';
import MenuIcon from '@mui/icons-material/Menu';
import { useRouter } from 'next/navigation';

export default function Header() {
    const [loggedIn, setLoggedIn] = React.useState(false);
    const router = useRouter();
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static" sx={{ backgroundColor: 'black', paddingTop: '5px', paddingBottom: '5px' }}>
        <Toolbar>
            <MusicVideoIcon sx={{ marginRight: 2, fontSize: '36px' }}/>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1, fontFamily: 'inter', fontSize: '24px', cursor: 'pointer' }} onClick={() => router.push("/")}>
                SongRanker
            </Typography>
            {loggedIn ? (
                <>
                    <Typography sx={{ fontSize: '24px', mr: 2 }} onClick={() => setLoggedIn(false)}>Umer Kazi</Typography>
                </>
            ) : (
                <>
                    <Button color="inherit" onClick={() => setLoggedIn(true)}>Login</Button>
                    <Button color="inherit" sx={{ marginLeft: 2 }}>Sign Up</Button>
                </>
            )}
            
        </Toolbar>
      </AppBar>
    </Box>
  );
}