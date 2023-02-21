import { Box, Text, Flex, Icon } from "@chakra-ui/react"
import { useState, useRef } from "react"
import { AiFillStar, AiOutlineStar } from 'react-icons/ai'
import {FcGoogle} from 'react-icons/fc'
import DomPurify from 'dompurify'
export const Review = ({name, avatar, rating, date, content, full_node, full_review, replies}) => {
    const {review, services} = content
    const numRating = Number(rating.split(' ')[1])
    const stars = []
    for (let i = 1; i <= 5; i++) {
        if (numRating >= i) {
            stars.push(<Icon as={AiFillStar} color='#FFCB45'/>)
        } else {
            stars.push(<Icon as={AiOutlineStar} color='#FFCB45'/>)
        }
    }
    const sanitizedNode = DomPurify.sanitize(full_node)
    // console.log(sanitizedNode)
    if (services) {
      const x = services.split(":").pop()
      console.log(x.trim())
    }
    const repliesArray = JSON.parse(replies)
    console.log(repliesArray)
    const ref = useRef(null)
    return (
        <Flex 
        alignItems='flex-start'
        border='1px solid #E0ECF1'
        maxW='100%'
        padding='1rem'>
            <Flex
            width='100%'
            gap='1rem'
            textAlign='left'>
                <Flex alignItems='flex-start'
                gap='1rem'
                width='30%'
                >
                    <img
                    src={avatar} alt={name}/>
                    <Box>
                    <Flex 
                    alignItems='center'
                    gap='1rem'
                    fontWeight={700}>{name} <Icon as={FcGoogle}/></Flex>
                    {services && (
                        <Text 
                        color='#878790'
                        fontSize='0.9rem'>{services.split(':').pop().trim()}</Text>
                    )}
                    </Box>
                </Flex>
                <Box 
                maxWidth='65%'>
                    <Flex alignItems='center'
                    gap='1rem'>
                        <Flex>{stars.map(e=>e)}</Flex> 
                        <Text
                        color='#878790' 
                        fontSize='0.8rem'>{date}</Text>
                    </Flex>
                    <Box 
                    margin='0.5rem 0'>
                    {full_review !== 'None' ? <Box dangerouslySetInnerHTML={{__html: full_review.replace('style="display:none"', '')}}></Box>
                        : 
                        <>
                        <Box>{review}</Box>
                        </>}
                    </Box>
                    {repliesArray.length > 0 && (
                        <Box>
                            {repliesArray.map(e=>{
                                return (
                                    <Box>
                                        <Flex gap='1rem' alignItems='center'><Text fontWeight={700}>Reply from owner</Text><Text color='#878790' fontSize='0.8rem'>{e.date}</Text></Flex>
                                        <Text>{e.content}</Text>
                                    </Box>
                                )
                            })}
                        </Box>
                    )}
                </Box>

            </Flex>
        </Flex>
    )
}