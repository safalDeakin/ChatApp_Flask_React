import React, {useState} from  'react';
import { Link } from 'react-router-dom';
import './Join.css';

const Join = () =>{

    const [name,setName] = useState('');
    const [password,setPassword] = useState('');

    return (
        <div className="joinOuterContainer">
            <div className = "joinInnerContainer">
                <h1 className = "heading">Join Chat App</h1>
                <div><input placeholder="UserName" className="joinInput" type="text" onChange={(event) => setName(event.target.value)}/></div>
                <div><input placeholder="Password" className="joinInput mt-20" type="password" onChange={(event) => setPassword(event.target.value)}/></div>
                <Link onClick={ event=> (!name || !password) ? event.preventDefault() : null} to={`/chat?name=${name}&password=${password}`}>
                    <button className="button mt-20" type="submit">Sign In</button>
                </Link>
            </div>
        </div>
    )
}

export default Join;