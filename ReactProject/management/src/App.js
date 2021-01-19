import './App.css';
import Customer from './components/Customer';

const customers = [{
  'id' : 1,
  'image' : 'http://placeimg.com/200/200/1',
  'name' : '홍길동',
  'birthday' : '961222',
  'gender' : '남',
  'job' : '대학생'
},
{
  'id' : 2,
  'image' : 'http://placeimg.com/200/200/2',
  'name' : '이순신',
  'birthday' : '961112',
  'gender' : '남',
  'job' : '디자이너'
},
{
  'id' : 3,
  'image' : 'http://placeimg.com/200/200/3',
  'name' : '가나다',
  'birthday' : '960203',
  'gender' : '남',
  'job' : '대학생'
}]
function App() {
  return (
   <div>
     {customers.map(c =>{
         return(
           <Customer
           key={c.id}
           id={c.id}
           image={c.image}
           name={c.name}
           birthday={c.birthday}
           gender={c.gender}
           job={c.job}/>
         )
       })}
     
    </div>  
  );
}

export default App;
