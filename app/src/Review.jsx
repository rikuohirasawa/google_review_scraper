import { Box, Text } from "@chakra-ui/react"
import { useState, useRef } from "react"
import { AiFillStar, AiOutlineStar } from 'react-icons/ai'
export const Review = ({name, avatar, rating, date, content}) => {
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
    const testHTML = 'HELLO<br>HELLO<br>WHAT'
    document.getElementById('lol').innerHTML = testHTML
    const ref = useRef(null)
    console.log(ref.current.innerHTML)
    return (
        <Box ref={ref}>
            <img
            src={avatar} alt={name}/>
            <Box>
                <Text>{name}</Text>
                <Box>
                    <Box>{stars.map(e=>e)}</Box>
                    <Text>{date}</Text>
                    <Box>
                        {content.review && <Box>{review}</Box>}
                    </Box>
                    {content.services && <Box>{services}</Box>}
                </Box>
            </Box>
        </Box>
    )
}