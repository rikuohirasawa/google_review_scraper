import { Box, Text } from "@chakra-ui/react"
export const Review = ({name, avatar, rating, date, content}) => {
    return (
        <Box 
        border='1px solid'>
            <img src={avatar} alt={name}/>
            <Box>
                <Text>{name}</Text>
                <Box>
                    <Text>{rating}</Text>
                    <Text>{date}</Text>
                    <Box>
                        {content}
                    </Box>
                </Box>
            </Box>
        </Box>
    )
}