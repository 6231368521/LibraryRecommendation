
import Card from 'react-bootstrap/Card';
import { faker } from '@faker-js/faker';

export const CardCustom = ()=>{
  return(
    <Card style={{ width: '18rem',margin:'10px',height:'200px' }}>
      <Card.Body style={{ justifyContent:'space-between', display:'flex', flexDirection:'column'}}>
        <div>
          <Card.Title>{faker.name.fullName()}</Card.Title>
          <Card.Subtitle className="mb-2 text-muted">Catagory</Card.Subtitle>
          <Card.Text>
            {faker.music.genre()}
          </Card.Text>
        </div>
        <Card.Link href="#">Another Link</Card.Link>
      </Card.Body>
    </Card>
  )
}