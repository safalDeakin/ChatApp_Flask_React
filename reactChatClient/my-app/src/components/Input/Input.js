import React from 'react';

import './Input.css';

const Input = ({message, setMessage, sendMessage}) =>(
    <form className = "form">
        <input 
            className= "input"
            type = "text"
            placeholder = "Type a Message .. "
            value= {message}
            onChange = {({target : {value }}) => setMessage(value)}
            onKeyPress = {event => event.key === 'Enter' ? sendMessage(event) : null}
        />

        <buttom className = "sendButton" onClick = { event => sendMessage(event)}>
            Send
        </buttom>
    </form>
)

export default Input