import logo from './logo.svg';
import './App.css';
import "bootstrap/dist/css/bootstrap.min.css";

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Routes
} from "react-router-dom";
import { Main } from './pages/main';
import { Input } from './pages/input';
import { BookPage } from './pages/main/book';
import { MainPage } from './pages/input/member'
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/books" element={<Main />} />
        <Route path="/book/:id" element={<BookPage />} />
        <Route path="/input" element={<Input />} />
      </Routes>
    </Router>
  );
}

export default App;
