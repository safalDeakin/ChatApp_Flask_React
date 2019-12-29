import React,{useState, useEffect} from 'react';
import './Chat.css';
import queryString from 'query-string';
import io from 'socket.io-client';

import InfoBar from './../InfoBar/InfoBar';
import Input from './../Input/Input';
import Messages from './../Messages/Messages';
import TextContainer from './../TextContainer/TextContainer';

let socket;
let room
const Chat = ({location}) =>{
    const [name,setName]= useState('');
    const[message, setMessage] = useState('');
    const[messages, setMessages] = useState([]);
    const [users, setUsers] = useState([]);
    const ENDPOINT = 'http://127.0.0.1:9999/';

    useEffect(()=>{
        const {name} = queryString.parse(location.search);
        socket = io(ENDPOINT);

        setName(name);
        room ="ROOM";
                         
        socket.emit( 'event msg' ,{ event: 'REG_MSG' , data:{ userName: name} },()=>{} );
        console.log({ event: 'REG_MSG' , data:{ userName: name}} );

    }, [ENDPOINT,location.search]);

    useEffect(()=>{
        const {name} = queryString.parse(location.search);

        const handleServerResponse = (message) =>{
            console.log("Server Response ");
            console.log(message);
            
            setMessages([...messages,message.data])
        }

        socket.on('server response',(message) =>{
            console.log(message);
            if(message.event === "REG_MSG_RESPONSE"){
                     alert("SuccessFully registered From admin") ;
                     socket.emit( 'event msg' ,{ event: 'EVENT_REQUEST_USERS' , data:{ userName: name} },()=>{} );

            }else if(message.event ==="EVENT_REQUEST_USERS_RESPONSE"){
                var listUser = message.data.msg.users;
                
                setUsers(listUser);
            }else{
                handleServerResponse(message)
            } 
        })

        return() =>{
            socket.emit("disconnect");
            socket.off();
        }

    },[messages]);

    const sendMessage = (event)=>{
        event.preventDefault();
        if(message){
            
            /*socket.emit('event msg',message,EVENT_PUB_MSG() =>setMessage('')); */                           
            let msg = { 
                event: 'EVENT_PUB_MSG' , 
                data:{ msg : message, sender: name}
            };

            console.log(msg)
            socket.emit('event msg',msg);
            setMessage('');
        }
    }

    return (
        <div className = "outerContainer">
            <div className = "container">
                <InfoBar room =  {room} />
                <Messages messages = {messages} name = {name}/>
                <Input message = {message} setMessage = {setMessage} sendMessage = {sendMessage}/>
            </div>
            <TextContainer users={users}/>
            
        </div>
    )
}

export default Chat;