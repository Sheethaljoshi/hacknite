import Monaco from "./Monaco";

// Editor.js
const Editor = ({ content,filetype }) => {
  return (
    <div className="w-4/5 bg-gray-800 text-gray-100">
      <div className="p-4 font-bold text-xxl">Editor</div>
      <div className="p-4">
        {/* Editor content */}
        <pre><Monaco theme="vs-dark" language={filetype} value={content} /></pre>
      </div>
    </div>
  );
};

export default Editor;

