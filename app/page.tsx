'use client'
import { Box, Button, Typography } from '@mui/material'
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import { useRouter } from 'next/navigation'

const contentCards = [
  {title: "What is it?", content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin dapibus condimentum urna ut sagittis. Phasellus et lobortis leo. Nunc accumsan ante ipsum, at rhoncus libero vestibulum ut. Donec volutpat lorem dui. Duis eu sodales magna, euismod vehicula magna. Sed pretium nec nisi quis fringilla. Mauris egestas ligula tristique feugiat dictum. Proin euismod, diam et iaculis accumsan, velit urna lobortis nulla, ac aliquet sapien nunc sit amet ipsum. Vestibulum sed rutrum eros, ut ornare ante. Sed faucibus gravida mauris, nec laoreet massa volutpat sed. Nunc sagittis ipsum vel libero tincidunt faucibus. Ut turpis sapien, finibus ut neque sit amet, sollicitudin euismod enim. Integer ultricies dui eu nulla ornare, imperdiet facilisis tellus convallis. Pellentesque dui nunc, tempus id efficitur venenatis, varius at sapien.", image: ""},
  {title: "How it works", content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin dapibus condimentum urna ut sagittis. Phasellus et lobortis leo. Nunc accumsan ante ipsum, at rhoncus libero vestibulum ut. Donec volutpat lorem dui. Duis eu sodales magna, euismod vehicula magna. Sed pretium nec nisi quis fringilla. Mauris egestas ligula tristique feugiat dictum. Proin euismod, diam et iaculis accumsan, velit urna lobortis nulla, ac aliquet sapien nunc sit amet ipsum. Vestibulum sed rutrum eros, ut ornare ante. Sed faucibus gravida mauris, nec laoreet massa volutpat sed. Nunc sagittis ipsum vel libero tincidunt faucibus. Ut turpis sapien, finibus ut neque sit amet, sollicitudin euismod enim. Integer ultricies dui eu nulla ornare, imperdiet facilisis tellus convallis. Pellentesque dui nunc, tempus id efficitur venenatis, varius at sapien.", image: ""},
  {title: "The inspiration", content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin dapibus condimentum urna ut sagittis. Phasellus et lobortis leo. Nunc accumsan ante ipsum, at rhoncus libero vestibulum ut. Donec volutpat lorem dui. Duis eu sodales magna, euismod vehicula magna. Sed pretium nec nisi quis fringilla. Mauris egestas ligula tristique feugiat dictum. Proin euismod, diam et iaculis accumsan, velit urna lobortis nulla, ac aliquet sapien nunc sit amet ipsum. Vestibulum sed rutrum eros, ut ornare ante. Sed faucibus gravida mauris, nec laoreet massa volutpat sed. Nunc sagittis ipsum vel libero tincidunt faucibus. Ut turpis sapien, finibus ut neque sit amet, sollicitudin euismod enim. Integer ultricies dui eu nulla ornare, imperdiet facilisis tellus convallis. Pellentesque dui nunc, tempus id efficitur venenatis, varius at sapien.", image: ""}
]

export default function Home() {
  const router = useRouter();
  return (
    <Box id="page-container" sx={{ width: '100%', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
      <Box id="hero-card" sx={{ width: '100%', height: 'calc(100vh - 74px)'}}>
        <Box id="hero" sx={{ height: '50%', width: '100%', display: 'flex' , flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
          <Typography sx={{ fontSize: '72px', fontWeight: '600', mb: 3}}>
            SONG RANKER
          </Typography>
          <Button variant='contained' sx={{width: '200px', height: '55px'}} onClick={() => router.push("/play")}>
            Start Ranking
          </Button>
        </Box>
        <Box id="image-placeholder" sx={{ backgroundColor: 'grey', width: '100%', height: '50%', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'flex-end' }}>
          <Typography sx={{ color: 'white', fontSize: '18px' }}>
            Scroll for more info!
          </Typography>
          <KeyboardArrowDownIcon sx={{ marginBottom: '20px', color: 'white', fontSize: '24px', marginTop: '5px' }} />
        </Box>
      </Box>
      {contentCards.map((item, idx) => (
        <>
          <Box key={item.title} sx={{ width: '100%', paddingTop: '80px', paddingBottom: '20px', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
            <Typography sx={{ fontSize: '60px', marginBottom: '60px', fontWeight: '600' }}>
              {item.title}
            </Typography>
            <Typography sx={{ fontSize: '24px', paddingRight: '40px', paddingLeft: '40px', textAlign: 'center', paddingBottom: '60px' }}>
              {item.content}
            </Typography>
          </Box>
          <Box key={item.title} id="image-placeholder" sx={{ backgroundColor: 'grey', width: '100%', height: '200px' }}>

          </Box>
        </>
      ))}
      <Box id="creator-card" sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
        <Typography sx={{ fontSize: '60px', fontWeight: '600', paddingTop: '60px', paddingBottom: '60px' }}>
          The Creator
        </Typography>
        <Box id="image-placeholder" sx={{ backgroundColor: 'grey', height: '300px', width: '250px' }}>

        </Box>
        <Typography sx={{ fontSize: '18px', marginTop: '10px' }}>
          John Doe
        </Typography>
        <Typography sx={{ fontSize: '24px', paddingTop: '30px', paddingBottom: '60px' }}>
          Contact: johndoe@gmail.com
        </Typography>
      </Box>
    </Box>
  )
}
