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
  const [currentBook,setCurrentBook] = useState()
  useEffect(() => {
    axios.get(`http://localhost:${PORT}/books/item-base/${id}`).then((response) => {
      console.log(response?.data);
      setBooks(response?.data)
    })

    axios.get(`http://localhost:${PORT}/books/${id}`).then((response) => {
      setCurrentBook(response?.data)
    })
  },[]);
  return (
    <div style={{padding:'20px',height:'100vh', backgroundColor:'#fee9e8'}}>
      <div style={{padding:'20px', backgroundColor:'white',display:'flex' , borderRadius:'12px'}}>
        {/* <div style={{ margin:'0 24px 0 0'}}>
          <img src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1635827409l/20342617.jpg" alt=''/>
        </div> */}
        <div>
          <div>
          Title: {currentBook?.name}
          </div>
          <div style={{ display:'flex'}}>
            Subjects: 
            <div style={{ display:'flex', flexWrap:'wrap' }}>
              <div>{[...new Set(currentBook?.subjects.map((row)=> row.name))].join(', ')}</div>
            </div>
          </div>
        </div>
      </div>
      <ListBook title={'Related'} list={books}/>
    </div>
  );
}

