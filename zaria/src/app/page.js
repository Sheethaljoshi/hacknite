// pages/index.js
import Sidebar from "../components/Sidebar";
import Editor from "../components/Editor";
import 'tailwindcss/tailwind.css'

const Home = () => {
  return (
    <div className="flex h-screen overflow-x-hidden w-screen max-w-full">
      <Sidebar />
      <Editor />
    </div>
  );
};

export default Home;
