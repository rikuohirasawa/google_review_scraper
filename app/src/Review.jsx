import { Box, Text } from "@chakra-ui/react"
import { useState, useRef } from "react"
import { AiFillStar, AiOutlineStar } from 'react-icons/ai'
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
    const ref = useRef(null)
    // console.log(ref.current.innerHTML)
    // console.log(full_node)
    // ref.current.innerHTML = full_node
    if (full_review !== 'None') {
        // console.log(full_review.replace('style="display:"'))
        document.getElementById('test').innerHTML = full_review.replace('style="display:none"', '')
    }
    // full_review.replace('style="display:none"', '')
    // console.log(full_node)
    return (
        <Box>
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