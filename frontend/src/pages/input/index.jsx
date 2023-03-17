import react, { useState,useEffect } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { useNavigate } from 'react-router-dom';
import axios from 'axios'

export const Input =  () => {

  //TODO add correct subjects
  // const subjectList = ["Law", "Romance", "Non-fiction", "Shooter"];
  const [subjectList,setSubjectList] = useState([])
  console.log();
  const [id, setId] = useState("");
  const [inputs, setInputs] = useState(subjectList.reduce((a, v) => ({ ...a, [v]: false}), {}));
  const [selectedKey, setSelectedKey] = useState([])
  const [step,setStep] = useState(1)
  const navigate = useNavigate();


  function handleSubmit(event) {
    event.preventDefault();
    console.log(id);
    console.log(inputs);
    axios.get(`http://localhost:${8000}/users/${id}`).then((response) => {
      console.log(response?.data);
      if(response?.data?.code === 200){
        navigate('/books', {state: {subjects: inputs, id: id, isMember: true}});
      } else if (response?.data?.code === 402) {
        setStep(2)
      } else {
        alert('User not found')
      }
    })
  }

  const handleCheckboxChange = (id) => {
    if (selectedKey.includes(id)){
      setSelectedKey(selectedKey.filter((e)=> e !== id))  
      return
    }
    setSelectedKey([...selectedKey, id])
    return
  }

  useEffect(() => {
    console.log(`http://localhost:${8000}/subjects`)
    axios.get(`http://localhost:${8000}/subjects`).then((response) => {
      console.log(response?.data);
      setSubjectList(response?.data)
    })
  },[]);

  return (
    <div style={{padding:'20px',height:'100vh', backgroundColor:'#fee9e8', display:'flex', justifyContent:'center', alignItems:'center', flexDirection:'column'}}>
      {step === 1 && <div>
          <Form onSubmit={handleSubmit}>
              <Form.Group controlId='studentID'>
                  <Form.Label>Please enter your patron ID</Form.Label>
                  <Form.Control as="textarea" value={id} onChange={(e) => setId(e.target.value)} style={{ height:'40px'}}></Form.Control>
              </Form.Group>
              <Button variant='primary' type='submit'>Submit</Button>
          </Form>
      </div>
      }
      {step === 2  && <div>
        <Form onSubmit={handleSubmit}>
          <Form.Group controlId='studentID'>
            </Form.Group>
              <Form.Label>Please select your favourite catagory for good experience</Form.Label>
              <div style={{ display:'flex', width:'500px',flexWrap:'wrap', margin:'8px 0 8px 0'}}>
              {subjectList.map((subject) => (
                  <Form.Check type='checkbox'
                  style={{ margin:'0 8px 0 0'}}
                  name={subject?.name} 
                  label={subject?.name} 
                  key={subject?.id} 
                  checked={selectedKey.includes(subject?.id)}
                  onChange={()=>handleCheckboxChange(subject?.id)}
                  ></Form.Check>
              ))}
              </div>
            <Button onClick={()=> {
              axios.post(`http://localhost:${8000}/users/addNew`, {
                patronRecord:id,
                subject: selectedKey
              })
              .then((response) => {
                if( response?.status === 200){
                  navigate('/books', {state: {subjects: inputs, id: id, isMember: true}});
                }
              })
            }}>Submit</Button>
        </Form>
      </div>
      }
    </div>
  );
}

