import { Box, Text } from "@chakra-ui/react"
import { useState, useRef } from "react"
import { AiFillStar, AiOutlineStar } from 'react-icons/ai'
import DomPurify from 'dompurify'
export const Review = ({name, avatar, rating, date, content, full_node, full_review}) => {
    const {review, services} = content
    const numRating = Number(rating.split(' ')[1])
    const stars = []
    for (let i = 1; i <= 5; i++) {
        if (numRating >= i) {
            stars.push(<AiFillStar/>)
        } else {
            stars.push(<AiOutlineStar/>)
        }
    }
    const sanitizedNode = DomPurify.sanitize(full_node)
    // console.log(sanitizedNode)
    
    const ref = useRef(null)
    if (full_review !== 'None') {
        // console.log(full_review.replace('style="display:"'))
        document.getElementById('test').innerHTML = full_review.replace('style="display:none"', '')
    }
    return (
        <Box>
            {/* <Box dangerouslySetInnerHTML={{__html: sanitizedNode.replace('style="display:none"', '')}}></Box> */}
            <img
            src={avatar} alt={name}/>
            <Box>
                <Text>{name}</Text>
                <Box>
                    <Box>{stars.map(e=>e)}</Box>
                    <Text>{date}</Text>
                    {/* <Box>{full_review}</Box> */}
                    <Box>
                        {full_review !== 'None' ? <Box dangerouslySetInnerHTML={{__html: full_review.replace('style="display:none"', '')}}></Box>
                        : 
                        <>
                        <Box>{review}</Box>
                        <Box>{services}</Box>
                        </>}
                    </Box>

                </Box>
                <Text ref={ref} id='' onLoad={()=>{

                }}></Text>
                <Box ref={ref}></Box>
            </Box>
        </Box>
    )
}