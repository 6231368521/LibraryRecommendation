import react, { useEffect,useState } from 'react'
import { ListBook } from '.';
import { CardCustom } from './component';
import { useParams,useLocation } from 'react-router-dom'
import axios from 'axios'
const PORT = 8000
export const BookPage =  () => {
  const { id } = useParams()
  const location = useLocation();
  const [books,setBooks] = useState([])
  useEffect(() => {
    axios.get(`http://localhost:${PORT}/books/item-base/${id}`).then((response) => {
      console.log(response?.data);
      setBooks(response?.data)
      // setBooks(response?.data);
    })
  },[]);

  return (
    <div style={{padding:'20px',height:'100vh', backgroundColor:'#fee9e8'}}>
      <div style={{padding:'20px', backgroundColor:'white',display:'flex' , borderRadius:'12px'}}>
        <div style={{ margin:'0 24px 0 0'}}>
          <img src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1635827409l/20342617.jpg" alt=''/>
        </div>
        <div>
          <div>
          Title: {location?.state?.name}
          </div>
          <div>
            ID: {id}
          </div>
        </div>
      </div>
      <ListBook title={'Related'} list={books}/>
    </div>
  );
}

