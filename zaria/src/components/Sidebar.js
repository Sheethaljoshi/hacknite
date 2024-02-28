// Sidebar.js
const Sidebar = ({ files, onFileClick1, onFileClick2 }) => {
  return (
    <div className="w-1/5 h-screen bg-gray-900 text-gray-100 border-r border-gray-600">
      <div className="p-4 font-bold text-2xl">File Explorer</div>
      <div className="bg-gray-900 border-t border-gray-600 ">
        {files.map((file, index) => (
          <button
            key={index}
            className="block w-full px-4 py-2 text-left text-white hover:bg-gray-700 border-b border-gray-600 rounded-sm"
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

