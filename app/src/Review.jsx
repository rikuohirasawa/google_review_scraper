import { Box, Text } from "@chakra-ui/react"
export const Review = ({name, avatar, rating, date, content}) => {
    const {review, services} = content
    const num = Number('5.0')
    console.log(num)
    return (
        <Box>
            <img src={avatar} alt={name}/>
            <Box>
                <Text>{name}</Text>
                <Box>
                    <Text>{rating}</Text>
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