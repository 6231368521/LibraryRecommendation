import react, { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom';
import { CardCustom } from './component';
import axios from 'axios'

export const ListBook = ({title,list,select,select2}) =>{
  return (
  <div style={{padding:'20px'}}>
  <div style={{ display:'flex' }}>
    <div style={{width:'fit-content', margin:'0 16px 0 0'}}>
    <p style={{ fontSize:'24px',padding:'10px', borderRadius:'10px', backgroundColor:'#dd5c8e', color:'white'}}>{title}</p>
    </div>
    {select}
    {select2}
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
  const [books, setBooks] = useState([])
  const [allFaculty,setAllFaculty] = useState([])
  const [bookFaculty,setBookFaculty] = useState([])
  const [categoryOptions,setCategoryOptions] = useState()
  const [popularBooks,setPopularBooks] = useState([])
  const [selectListCategory,setSelectListCategory] = useState([])
  const [categoryBooks,setCategoryBooks] = useState([])
  //TODO insert PORT
  const PORT = 8000
  useEffect(()=>{
    console.log(allFaculty);
    axios.get(`http://localhost:${PORT}/books/recommendByFaculty/${allFaculty?.[0]?.id}`).then((response) => {
      setBookFaculty((response?.data).map((e)=> {
        return {
        name:e?.book?.name,
        id:e?.book?.id,
      }
    }))
    })
    
  },[allFaculty])


  useEffect(() => {
    axios.get(`http://localhost:${PORT}/books/content-base/${location?.state?.id}`).then((response) => {
      setBooks(response?.data);
    })
    axios.get(`http://localhost:${PORT}/books/top-borrow`).then((response) => {
      setPopularBooks(response?.data);
    })
    axios.get(`http://localhost:${PORT}/facultys`).then((response) => {
      setAllFaculty(response?.data);
    })
    axios.get(`http://localhost:${PORT}/users/${location?.state?.id}/category`).then((response) => {
      console.log('test',response?.data)
      setSelectListCategory(response?.data);
    })
  },[]);

  return (
    <div style={{padding:'20px', backgroundColor:'#fee9e8', minHeight:'100vh'}}>
      <ListBook title={'Top Borrow'} list={popularBooks} />
      { location?.state?.isMember &&
      <>
        <ListBook title={'Personal Recommendation'} list={books}/>
        <ListBook title={'Based on faculty'} list={bookFaculty} 
        select={
          <select
          class="form-select"
          aria-label="Default select example"
          style={{ width:'200px', height:'40px' }}
          onChange={(e)=> {
            axios.get(`http://localhost:${PORT}/facultys/${e?.target?.value}`).then((response) => {
              console.log(response)
              setCategoryOptions((response?.data).map((e)=> {
                return {
                name:e?.name,
                id:e?.id,
              }
            }));
            axios.get(`http://localhost:${PORT}/books/recommendByFaculty/${response?.data?.[0]?.id}`).then((response) => {
              setBookFaculty((response?.data).map((e)=> {
                return {
                  name:e?.book?.name,
                  id:e?.book?.id,
              }
            }));
          })
          })
        }}
          >
            {(allFaculty)?.map((e)=> {
            return (
              <option value={e?.id}>{e?.name}</option>
            )
            })}
          </select>
        }
        select2={
          <select
          class="form-select"
          aria-label="Default select example"
          style={{ width:'200px', height:'40px' }}
          onChange={(e)=> {
            axios.get(`http://localhost:${PORT}/books/recommendByFaculty/${e?.target?.value}`).then((response) => {
              console.log(response?.data,'response?.data')
              setBookFaculty((response?.data).map((e)=> {
                return {
                  name:e?.book?.name,
                  id:e?.book?.id,
              }
            }));
          })
        }}
          >
            {(categoryOptions)?.map((e)=> {
            return (
              <option value={e?.id}>{e?.name}</option>
            )
            })}
          </select>
        }
        />
        <ListBook
        title={'Recommend by Category'}
        list={categoryBooks}
        select={
          <select
          class="form-select"
          aria-label="Default select example"
          style={{ width:'200px', height:'40px' }}
          onChange={(e)=> {
            axios.get(`http://localhost:${PORT}/books/recommendByCategory/${location?.state?.id}?categoryId=${e?.target?.value}`).then((response) => {
              console.log(response)
              setCategoryBooks((response?.data).map((e)=> {
                return {
                name:e?.name,
                id:e?.id,
              }
            }));
          })
        }}
          >
            {(selectListCategory)?.map((e)=> {
            return (
              <option value={e?.id}>{e?.name}</option>
            )
            })}
          </select>
        }
        />
      </>
      }
    </div>
  )
}

