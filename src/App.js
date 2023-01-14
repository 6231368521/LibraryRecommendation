import logo from './logo.svg';
import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Routes
} from "react-router-dom";
import { Main } from './pages/main';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/2" element={<Main />} />
      </Routes>
    </Router>
  );
}

export default App;
