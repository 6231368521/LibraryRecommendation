import react from 'react'
import { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

export const Input =  () => {

  const subjectList = ["Law", "Romance", "Non-fiction"];
  console.log();
  const [id, setId] = useState("");
  const [inputs, setInputs] = useState(subjectList.reduce((a, v) => ({ ...a, [v]: false}), {}));


  function handleSubmit(event) {
    event.preventDefault();
    console.log(id);
    console.log(inputs);
  }

  const handleCheckboxChange = (event) => {
    const name = event.target.name;
    const value = event.target.checked;
    console.log(event);
    setInputs(values => ({...values, [name]: value}))
  }
  return (
    <div>
        <Form onSubmit={handleSubmit}>
            <Form.Group controlId='studentID'>
                <Form.Label>Please enter your student ID</Form.Label>
                <Form.Control as="textarea" value={id} onChange={(e) => setId(e.target.value)}></Form.Control>
            </Form.Group>

            {subjectList.map((subject) => (
                <Form.Check type='checkbox' 
                name={subject} 
                label={subject} 
                key={subject} 
                checked={inputs[subject]}
                onChange={handleCheckboxChange}
                ></Form.Check>
            ))}

            <Button variant='primary' type='submit'>Submit</Button>
        </Form>
    </div>
  );
}

