import React from "react";
import Editor from "@monaco-editor/react";

const EditorPage = ({ content, filetype, handlechange }) => {
  return (
    <div className="w-4/5 bg-gray-800 text-gray-100">
      <div className="p-4 pl-8 font-bold text-2xl">Code Editor</div>
      <div className="ml-8 mr-8 shadow-2xl relative">

        <Editor
          height="85vh"
          language={filetype}
          theme="vs-dark"
          value={content}
          onChange={handlechange}
        />
        <div className="absolute bottom-0 right-0 p-4 pr-10">
          <button className="px-4 py-2 bg-gray-600 text-white rounded font-semibold hover:bg-blue-600">
            Submit
          </button>
        </div>
      </div>
    </div>
  );
};

export default EditorPage;


