// Sidebar.js
const Sidebar = ({ files, onFileClick1, onFileClick2, onFileClick3, edits }) => {
  return (
    <div className="w-1/5 h-screen bg-gray-900 text-gray-100 border-r-2 border-gray-600">
      <div className="p-4 font-bold text-2xl">File Explorer</div>
      <div className="bg-gray-900 border-t border-gray-600 ">
        {files.map((file, index) => (
          <button
            key={index}
            className="block w-full px-4 py-2 text-left text-white hover:bg-gray-700 border-b border-gray-600 rounded-sm"
            onClick={() => {console.log(file);onFileClick1(file.content);onFileClick2(file.filetype);onFileClick3(file.filename)}}
          >
            {file.filename}
          </button>
        ))}
      </div>
      <div className="p-4 font-bold text-2xl">Edits</div>
      <div className="bg-gray-900 border-t border-gray-600 ">
        {edits.map((file, index) => (
          <button
            key={index}
            className="block w-full px-4 py-2 text-left text-white hover:bg-gray-700 border-b border-gray-600 rounded-sm"
            onClick={() => {console.log(file);onFileClick1(file.edited);onFileClick2(file.filetype);onFileClick3(file.filename)}}
          >
            {file.username}
          </button>
        ))}
      </div>
    </div>
  );
};

export default Sidebar;

