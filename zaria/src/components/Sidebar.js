// Sidebar.js
const Sidebar = ({ files, onFileClick1, onFileClick2 }) => {
  return (
    <div className="w-1/5 h-screen bg-gray-900 text-gray-100">
      <div className="p-4">File Explorer</div>
      <div className="bg-gray-800">
        {files.map((file, index) => (
          <button
            key={index}
            className="block w-full px-4 py-2 text-left text-white hover:bg-gray-700"
            onClick={() => {console.log(file);onFileClick1(file.content);onFileClick2(file.filetype)}}
          >
            {file.filename}
          </button>
        ))}
      </div>
    </div>
  );
};

export default Sidebar;

