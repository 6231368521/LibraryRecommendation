
import Card from 'react-bootstrap/Card';
import { faker } from '@faker-js/faker';
import { useEffect, useState } from 'react';
import {useNavigate } from 'react-router-dom'
export const CardCustom = (props)=>{

  //TODO get bookId, PORT and insert
  // useEffect(() => {
  //   fetch('localhost:${PORT}/item-base/${bookId}')
  //     .then((response) => response.json())
  //     .then((data) => setBooks(data))
  //     .catch((err) => {
  //       console.log(err);
  //     });
  // });

  // todo, display the books info and the item-based recommendations
const navigate = useNavigate()
  return(
    <Card style={{ width: '18rem',margin:'10px',height:'200px' }}>
      <Card.Body style={{ justifyContent:'space-between', display:'flex', flexDirection:'column'}}>
        <div>
          <Card.Title>{props?.name}</Card.Title>
          <Card.Subtitle className="mb-2 text-muted">Id</Card.Subtitle>
          <Card.Text>
            {props?.id}
          </Card.Text>
        </div>
        <Card.Link onClick={()=>navigate(`/book/${props?.id}`,{state: {name: props?.name, id: props?.id}})}>Link</Card.Link>
      </Card.Body>
    </Card>
  )
}