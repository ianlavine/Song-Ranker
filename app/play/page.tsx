"use client"
import { Box, Button, TextField, Typography } from "@mui/material";
import React, { useState } from "react";
import prisma from "../../lib/prisma";

const mockArtists = ["Kanye West", "Russ", "Taylor Swift",  "P!ink"]
const mockAlbums = [
    {name: "Folklore", selected: true}, 
    {name: "Lover", selected: true}, 
    {name: "Reputation", selected: true}, 
    {name: "1989", selected: true}, 
    {name: "Evermore", selected: true}, 
    {name: "Fear USS", selected: false}, 
    {name: "Rea", selected: false}, 
    {name: "Speak Now", selected: false}, 
    {name: "Taylor Swift", selected: false}
]
const mockSongs = [{name: "Champagne Problems", album: "Evermore", image: ""}, {name: "Illicit Affairs", album: "Folklore", image: ""}]

export default function Play() {
    const [activeArtist, setActiveArtist] = useState("Taylor Swift")
    return (
        <>
            {/* <Box id="page-container-1" sx={{ display: 'flex', flexDirection: 'row', alignContent: 'center', justifyContent: 'center', height: 'calc(100vh - 124px)' }}>
                <Box id="column-1" sx={{ width: '20%', padding: '20px', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'space-between' }}>
                    <Box id="overall-stats" sx={{ backgroundColor: 'lightgrey', padding: '40px', width: 'calc(100% - 80px)' }}>
                        <Typography sx={{ fontWeight: '600' }}>
                            Overall Stats
                        </Typography>
                        <Typography>
                            Artists:
                        </Typography>
                        <Typography>
                            Rounds Played:
                        </Typography>
                        <br/>
                        <Typography sx={{ fontWeight: '600' }}>
                            Current Artist Stats
                        </Typography>
                        <Typography>
                            Rounds Played:
                        </Typography>
                        <Typography>
                            Artist Rank:
                        </Typography>
                    </Box>
                    <Box id="choose-artist" sx={{ backgroundColor: 'lightgrey', padding: '40px', width: 'calc(100% - 80px)', height: '100%', marginTop: '20px', display: 'flex', flexDirection: 'column', alignItems: 'flex-start', justifyContent: 'space-between' }}>
                        <Box sx={{ width: '100%' }}>
                            <Typography sx={{ fontSize: '28px', fontWeight: '600', marginBottom: '20px' }}>
                                Choose An Artist
                            </Typography>
                            {mockArtists.map((item) => (
                                <Typography key={item} sx={{ color: activeArtist == item ? "blue" : "black"  ,marginBottom: '10px', '&:hover': { color: 'blue' }, cursor: 'pointer' }} onClick={() => setActiveArtist(item)}>
                                    {item}
                                </Typography>
                            ))}
                        </Box>
                        <Box sx={{ display: 'flex', flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', width: '100%' }}>
                            <TextField
                                id="artistname"
                                label="Artist Name"
                                fullWidth
                                name="artistname"
                                type="text"
                                color="success"
                                InputProps={{  }}
                                sx={{
                                '& .MuiOutlinedInput-root': {
                                    '& fieldset': {
                                    borderColor: 'grey', // Change the focused border color
                                    },
                                    '&:hover fieldset': {
                                    borderColor: '#161716', // Change the hover border color
                                    },
                                    '&.Mui-focused fieldset': {
                                    borderColor: 'black', // Change the focused border color
                                    },
                                },
                                '& .MuiInputLabel-root': {
                                    color: 'grey', // Change the unfocused label color
                                    '&.Mui-focused': {
                                    color: 'black', // Change the focused label color
                                    },
                                },
                                }}
                            />
                            <Button variant="contained" sx={{ height: '55px' }}>Add</Button>
                        </Box>
                    </Box>
                </Box>
                <Box id="column-2" sx={{ width: '60%', padding: '20px', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', textAlign: 'left' }}>
                    {activeArtist !== "" && (
                        <>
                            <Typography sx={{ fontSize: '100px', flexGrow: 1 }}>
                                {activeArtist}
                            </Typography>
                            {mockSongs.map((item, idx) => (
                                <Box key={item.name} sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
                                    <Box id="image-placeholder" sx={{ backgroundColor: 'grey', height: '200px', width: '200px' }}>

                                    </Box>
                                    <Typography sx={{ fontWeight: '600' }}>
                                        {item.name}
                                    </Typography>
                                    <Typography>
                                        ({item.album})
                                    </Typography>
                                    {idx == 0 && (
                                        <Typography sx={{ margin: '40px' }}>
                                            OR
                                        </Typography>
                                    )}
                                </Box>
                            ))}
                            <Button variant="contained" sx={{ marginTop: '20px' }}>See Rankings</Button>
                        </>
                    )}
                    
                </Box>
                <Box id="column-3" sx={{ width: '20%', padding: '20px', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
                    <Box id="included" sx={{ backgroundColor: 'lightgrey', padding: '40px', width: 'calc(100% - 80px)' }}>
                        <Typography sx={{ fontWeight: '600' }}>
                            Included Albums
                        </Typography>
                        {mockAlbums.map((item) => (
                            <>
                                {item.selected == true && (
                                    <Typography>
                                        {item.name}
                                    </Typography>
                                )}
                            </>
                        ))}
                    </Box>
                    <Box id="excluded" sx={{ backgroundColor: 'lightgrey', padding: '40px', width: 'calc(100% - 80px)', marginTop: '20px' }}>
                        <Typography sx={{ fontWeight: '600' }}>
                            Excluded Albums
                        </Typography>
                        {mockAlbums.map((item) => (
                            <>
                                {item.selected == false && (
                                    <Typography>
                                        {item.name}
                                    </Typography>
                                )}
                            </>
                        ))}
                    </Box>
                </Box>
            </Box> */}
            <Box id="page-container-2" sx={{ display: 'flex', flexDirection: 'column', alignContent: 'center', justifyContent: 'top', height: 'calc(100vh - 124px)' }}>
                <Box id="row1" sx={{ border: '1px solid red', textAlign: 'left', width: '100%', padding: '40px' }}>
                    <Typography sx={{ fontSize: '72px' }}>
                        {activeArtist}
                    </Typography>
                </Box>
                <Box id="row2" sx={{ border: '1px solid blue' }}>
                    <Box id="col1">
                        <Box id="" sx={{ width: '20%', padding: '20px', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
                            <Box id="included" sx={{ backgroundColor: 'lightgrey', padding: '40px', width: 'calc(100% - 80px)' }}>
                                <Typography sx={{ fontWeight: '600' }}>
                                    Included Albums
                                </Typography>
                                {mockAlbums.map((item) => (
                                    <>
                                        {item.selected == true && (
                                            <Typography>
                                                {item.name}
                                            </Typography>
                                        )}
                                    </>
                                ))}
                            </Box>
                            <Box id="excluded" sx={{ backgroundColor: 'lightgrey', padding: '40px', width: 'calc(100% - 80px)', marginTop: '20px' }}>
                                <Typography sx={{ fontWeight: '600' }}>
                                    Excluded Albums
                                </Typography>
                                {mockAlbums.map((item) => (
                                    <>
                                        {item.selected == false && (
                                            <Typography>
                                                {item.name}
                                            </Typography>
                                        )}
                                    </>
                                ))}
                            </Box>
                        </Box>
                    </Box>
                </Box>
                
            </Box>
            <Box id="footer" sx={{ height: '50px', width: '100%', backgroundColor: 'black', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                <Typography sx={{ color: 'white', margin: '20px' }}>Ian Lavine | Contact</Typography>
                <Typography sx={{ color: 'white', marginRight: '20px' }}>Copyright 2023</Typography>
            </Box>
        </>
    )
}