import { Box, Heading, Text, Flex } from "@chakra-ui/react"

const Container = (props) => {
    return <Box 

    border='1px solid'
    {...props}/>
} 

const HeadingSmall = (props) => {
    return <Heading as={'h3'} 
    size='md'
    {...props}/>
}

const NavText = (props) => {
    return <Text {...props}/>
}

const FlexCol = (props) => {
    return <Flex 
    flexDir='column'
    align='flex-start'
    {...props}/>
}
export const Sidebar = () => {
    return (
        <Flex
        flexDir='column'
        align='flex-start'
        gap='8px'
        background='#fff'
        padding='16px'
        borderRadius='16px'
        height='65vh'>
            <HeadingSmall>Garage</HeadingSmall>
                <FlexCol>
                    <NavText>Garage Overview</NavText>
                    <NavText>Calendar Settings</NavText>
                    <NavText>Services</NavText>
                    <NavText color='#fb5012'>Ratings & Reviews</NavText>
                </FlexCol>
            <HeadingSmall>Accounts</HeadingSmall>
                <FlexCol>
                    <NavText>Garage Profile</NavText>
                    <NavText>Staff Management</NavText>
                </FlexCol>
            <HeadingSmall>Messages</HeadingSmall>
                <FlexCol>
                    <NavText>Message Template</NavText>
                    <NavText>Promotions & Promo Codes</NavText>
                </FlexCol>
            <HeadingSmall>Reports</HeadingSmall>
                <FlexCol>
                    <NavText>Daily Statements</NavText>
                </FlexCol>

        </Flex>
    )
}