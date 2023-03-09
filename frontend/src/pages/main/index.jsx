import react, { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom';
import { CardCustom } from './component';
import axios from 'axios'

export const ListBook = ({title,list}) =>{
  return (
  <div style={{padding:'20px'}}>
  <div style={{width:'fit-content'}}>
  <p style={{ fontSize:'24px',padding:'10px', borderRadius:'10px', backgroundColor:'#dd5c8e', color:'white'}}>{title}</p>
  </div>
  <div style={{ overflow:'auto',width:'fit-content' }}>
    <div style={{ display:'flex',flexWrap:'wrap',height:'220px'}}>
      {list?.map((e)=>{
        return (
          <CardCustom name={e?.name} id={e?.id} />
        )
      })}
    </div>
  </div>
</div>
)
}
export const Main =  () => {
  const location = useLocation();
  const [books, setBooks] = useState([]);
  const subjects = location?.state?.subjects;
  const studentId = 2
  const a = 2

  //TODO insert PORT
  const PORT = 8000
  useEffect(() => {
    axios.get(`http://localhost:${PORT}/books/content-base/${studentId}`).then((response) => {
      console.log(response?.data);
      setBooks(response?.data);
    })
  },[]);
  return (
    <div style={{padding:'20px', backgroundColor:'#fee9e8', minHeight:'100vh'}}>
      {/* <ListBook title={'Trending Right Now'}/> */}
      {/* <ListBook title={'Based on faculty'}/> */}
      <ListBook title={'Personal Recommendation'} list={books}/>
      {/* <ListBook title={'Personal Recommendation by Catagory'}/> */}
    </div>
  );
}

