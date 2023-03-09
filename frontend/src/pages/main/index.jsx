import react, { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom';
import { CardCustom } from './component';


export const ListBook = ({title}) =>{
  return (
  <div style={{padding:'20px'}}>
  <div style={{width:'fit-content'}}>
  <p style={{ fontSize:'24px',padding:'10px', borderRadius:'10px', backgroundColor:'#dd5c8e', color:'white'}}>{title}</p>
  </div>
  <div style={{ overflow:'auto',width:'fit-content' }}>
    <div style={{ display:'flex',flexWrap:'wrap',height:'220px'}}>
      <CardCustom/>
      <CardCustom/>
      <CardCustom/>
      <CardCustom/>
      <CardCustom/>
      <CardCustom/>
      <CardCustom/>
      <CardCustom/>
      <CardCustom/>
      <CardCustom/>
      <CardCustom/>
    </div>
  </div>
</div>
)
}
export const Main =  () => {
  const location = useLocation();
  const [books, setBooks] = useState([]);
  const subjects = location.state.subjects;
  const studentId = location.state.id;
  const a = 2

  //TODO insert PORT
  useEffect(() => {
    fetch(`localhost:${PORT}/content-base/${studentId}`)
      .then((response) => response.json())
      .then((data) => setBooks(data))
      .catch((err) => {
        console.log(err);
      });
  });
  return (
    <div style={{padding:'20px', backgroundColor:'#fee9e8'}}>
      <ListBook title={'Trending Right Now'}/>
      <ListBook title={'Based on faculty'}/>
      <ListBook title={'Personal Recommendation'}/>
      <ListBook title={'Personal Recommendation by Catagory'}/>
    </div>
  );
}

