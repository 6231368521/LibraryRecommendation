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
  console.log(location?.state);
  const [books, setBooks] = useState([]);
  const [popularBooks,setPopularBooks] = useState([])

  //TODO insert PORT
  const PORT = 8000
  useEffect(() => {
    axios.get(`http://localhost:${PORT}/books/content-base/${location?.state?.id}`).then((response) => {
      console.log(response?.data);
      setBooks(response?.data);
    })
    axios.get(`http://localhost:${PORT}/books/top-borrow`).then((response) => {
      console.log(response?.data);
      setPopularBooks(response?.data);
    })
  },[]);
  return (
    <div style={{padding:'20px', backgroundColor:'#fee9e8', minHeight:'100vh'}}>
      <ListBook title={'Trending Right Now'} list={popularBooks} />
      { location?.state?.isMember &&
      <>
        <ListBook title={'Personal Recommendation'} list={books}/>
        <ListBook title={'Based on faculty'}/>
        {/* <ListBook title={'Personal Recommendation by Catagory'}/> */}
      </>
      }
    </div>
  )
}

