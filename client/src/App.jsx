import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import { Sidebar } from './Sidebar'
import { Review } from './Review'

import { Box, Flex, Heading } from '@chakra-ui/react'

const Container = (props) => {
  return <Box {...props}/>
}

function App() {
  const [reviews, setReviews] = useState(null)
  useEffect(()=>{
    fetch('http://127.0.0.1:8000/api/get-reviews').then(res=>res.json()).then(data=>setReviews(data))
  }, [])
  return (
    <Flex border='1px solid'
    height='100vh'
    background='#E0ECF1'
    align='center'
    gap='16px'>
      <Sidebar/>
      <Box 
      borderRadius='16px'
      height='65vh'
      background='#fff'>
        <Heading size='xl'>Rating & Reviews</Heading>
        <Flex
        flexDir='column'>
          {reviews && (
            reviews.map(e=>{
              return <Review name={e.name} avatar={e.avatar} rating={e.rating} date={e.date} content={e.content}/>
            })
          )}
        </Flex>
      </Box>
    </Flex>
  )
}

export default App
