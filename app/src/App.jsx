import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import { Sidebar } from './Sidebar'
import { Review } from './Review'

import { Box, Flex, Heading, Button, ButtonGroup } from '@chakra-ui/react'

const Container = (props) => {
  return <Box {...props}/>
}

const Select = (props) => {
  return <Button 
  padding='16px'
  fontSize='20px'
  _hover={{
    background: '#fb5012'
  }}
  {...props}/>
}

function App() {
  const [reviews, setReviews] = useState(null);
  const [shop, setShop] = useState('/kings_bridge_auto')
  useEffect(()=>{
    fetch(`http://127.0.0.1:8000/api/garage-reviews?ref=${shop}`)
    .then(res=>res.json()
    ).then(data=>{
      console.log(data)
      setReviews(data)
    })
  }, [shop])

  return (
    <>
    <ButtonGroup
    pos='absolute'
    left='50%'
    top='10%'>
      <Select onClick={()=>{setShop('/kings_bridge_auto')}}>Kings Bridge Auto</Select>
      <Select onClick={()=>{setShop('/max_auto_repair')}}>Max Auto Repair</Select>
    </ButtonGroup>
    <Box id='test'>yeah</Box>
    <Heading>{shop.replace(/[^a-zA-Z]+/g, ' ').toUpperCase()}</Heading>
    <Flex
    height='100vh'
    background='#E0ECF1'
    align='center'
    gap='16px'>
      <Sidebar/>
      <Box 
      padding='16px'
      borderRadius='16px'
      height='65vh'
      background='#fff'>
        <Heading size='xl'>Rating & Reviews</Heading>
        <Flex
        maxH='100%'
        overflow='scroll'
        flexDir='column'>
          {reviews && (
            reviews.map(e=>{
              return <Review name={e.name} avatar={e.avatar} rating={e.rating} date={e.date} content={e.content} full_node={e.full_node} full_review={e.full_review}/>
            })
          )}
        </Flex>
      </Box>
    </Flex>
    </>
  )
}

export default App
