import react from 'react'
import { ListBook } from '.';
import { CardCustom } from './component';

export const BookPage =  () => {
  return (
    <div style={{padding:'20px',height:'100vh', backgroundColor:'#fee9e8'}}>
      <div style={{padding:'20px', backgroundColor:'white',display:'flex' , borderRadius:'12px'}}>
        <div style={{ margin:'0 24px 0 0'}}>
          <img src="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1635827409l/20342617.jpg" alt=''/>
        </div>
        <div>
          <div>
          Title:
          </div>
          <div>
            Description:
          </div>
        </div>
      </div>
      <ListBook title={'Related'}/>
    </div>
  );
}

