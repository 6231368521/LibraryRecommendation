import react, { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { useNavigate } from 'react-router-dom';

export const MainPage =  () => {
  const navigate = useNavigate()
  //TODO add correct subjects
  return (
    <div style={{padding:'20px',height:'100vh', backgroundColor:'#fee9e8', display:'flex', justifyContent:'center', alignItems:'center', flexDirection:'column'}}>
        <p style={{ fontSize:'50px', fontWeight:'600'}}>Are you member?</p>
        <div style={{ display:'flex', justifyContent:'space-between', alignItems:'center' } }>
          <button onClick={()=> navigate('/input') } style={{ width:'200px', margin:'0 8px 0 0'}}>Yes</button>
          <button onClick={()=> navigate('/books',{state: {isMember: false}}) } style={{ width:'200px'}}>No</button>
        </div>
    </div>
  );
}

