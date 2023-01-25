import react from 'react'
import { CardCustom } from './component';

export const Main =  () => {
  const a = 2
  return (
    <div style={{padding:'20px'}}>
      <div style={{padding:'20px'}}>
        <div>
        <p style={{ fontSize:'24px'}}>Trending Right Now</p>
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

