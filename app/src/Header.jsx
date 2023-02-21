import { Flex, Box, Heading, Text, Icon } from "@chakra-ui/react"
import { AiOutlineBell } from 'react-icons/ai'
import { RxPerson } from 'react-icons/rx'

export const Header = () => {
    return (
        <Flex 
        alignItems='flex-end'
        justifyContent='space-between'
        margin='1rem 0'>
            <Heading>Settings</Heading>
            <Flex alignItems='center'
            gap='1rem'>
                <Text color='#FB5012'
                fontWeight={700}
                fontSize='1.5rem'>10:32 AM</Text>
                <Text>16 Feb, 2023</Text>
                <Icon
                boxSize={6} 
                as={AiOutlineBell}/>
                <Icon
                boxSize={6}
                as={RxPerson}/>
            </Flex>
        </Flex>
    )
}