
import Card from 'react-bootstrap/Card';
import { faker } from '@faker-js/faker';
import { useEffect, useState } from 'react';

export const CardCustom = (props)=>{

  const [books, setBooks] = useState([]);

  //TODO get bookId, PORT and insert
  useEffect(() => {
    fetch('localhost:${PORT}/item-base/${bookId}')
      .then((response) => response.json())
      .then((data) => setBooks(data))
      .catch((err) => {
        console.log(err);
      });
  });

  // todo, display the books info and the item-based recommendations

  return(
    <Card style={{ width: '18rem',margin:'10px',height:'200px' }}>
      <Card.Body>
        <Card.Title>{faker.name.fullName()}</Card.Title>
        <Card.Subtitle className="mb-2 text-muted">Catagory</Card.Subtitle>
        <Card.Text>
          {faker.music.genre()}
        </Card.Text>
        <Card.Link href="#">Card Link</Card.Link>
        <Card.Link href="#">Another Link</Card.Link>
      </Card.Body>
    </Card>
  )
}