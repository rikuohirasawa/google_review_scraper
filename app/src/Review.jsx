import { Box, Text } from "@chakra-ui/react"
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
    return (
        <Box>
            <img src={avatar} alt={name}/>
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