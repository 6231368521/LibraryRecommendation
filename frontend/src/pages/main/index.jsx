import react, { useEffect } from 'react'
import { useLocation } from 'react-router-dom';
import { CardCustom } from './component';


export const Main =  () => {
  const location = useLocation();
  const [books, setBooks] = useState([]);
  const subjects = location.state.subjects;
  const studentId = location.state.id;
  const a = 2

  //TODO insert PORT
  useEffect(() => {
    fetch('localhost:${PORT}/content-base/${studentId}')
      .then((response) => response.json())
      .then((data) => setBooks(data))
      .catch((err) => {
        console.log(err);
      });
  });
  return (
    <div style={{padding:'20px'}}>
      <div style={{padding:'20px'}}>
        <div>
        <p style={{ fontSize:'24px'}}>Trending Right Now</p>
        </div>
        <div style={{ backgroundColor:'blue',overflow:'auto',width:'68%'}}>
          <div style={{ display:'flex',flexWrap:'wrap',height:'220px'}}>
            {/* TODO each CardCustom will takes one book as prop*/}
            {/* When clicked, it will popup new page for book recommendation content item-based */}
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
      <div style={{padding:'20px'}}>
        <div>
          <p style={{ fontSize:'24px'}}>Based on faculty</p>
        </div>
        <div style={{ backgroundColor:'blue',overflow:'auto',width:'68%'}}>
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
      <div style={{padding:'20px'}}>
        <div>
          <p style={{ fontSize:'24px'}}>Personal Recommendation</p>
        </div>
        <div style={{ backgroundColor:'blue',overflow:'auto',width:'68%'}}>
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
      <div style={{padding:'20px'}}>
        <div>
          <p style={{ fontSize:'24px'}}>Personal Recommendation by Catagory</p>
          {/* use subject to filter here */}
        </div>
        <div style={{ backgroundColor:'blue',overflow:'auto',width:'68%'}}>
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
    </div>
  );
}

