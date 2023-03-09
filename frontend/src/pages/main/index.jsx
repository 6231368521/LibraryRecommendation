import react from 'react'
import { CardCustom } from './component';

const ListBook = ({title}) =>{
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
  const a = 2
  return (
    <div style={{padding:'20px', backgroundColor:'#fee9e8'}}>
      <ListBook title={'Trending Right Now'}/>
      <ListBook title={'Based on faculty'}/>
      <ListBook title={'Personal Recommendation'}/>
      <ListBook title={'Personal Recommendation by Catagory'}/>
    </div>
  );
}

